#!/usr/bin/env python3
"""Inspect local iDempiere test/coverage evidence without network or DB calls."""

from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sys
import xml.etree.ElementTree as ET

SECRETS = ("PGPASSWORD", "SONAR_TOKEN", "COVERALLS_REPO_TOKEN", "GRAFANA_SERVICE_ACCOUNT_TOKEN")
ENDPOINTS = ("SONAR_HOST_URL", "PROMETHEUS_PUSHGATEWAY_URL", "GRAFANA_URL")


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def java_count(root: Path) -> int:
    return sum(1 for _ in root.rglob("*.java")) if root.exists() else 0


def bundle(plugin: Path) -> tuple[str, str | None]:
    value = read(plugin / "META-INF" / "MANIFEST.MF")
    name = re.search(r"^Bundle-SymbolicName:\s*([^;\r\n]+)", value, re.M)
    version = re.search(r"^Bundle-Version:\s*([^\r\n]+)", value, re.M)
    return (name.group(1).strip() if name else plugin.name, version.group(1).strip() if version else None)


def test_projects(plugin: Path, repo: Path, name: str) -> list[Path]:
    names = {f"{plugin.name}.test", f"{plugin.name}.tests", f"{name}.test", f"{name}.tests"}
    roots = (plugin.parent, repo / "sources" / "plugins", repo / "sources" / "tests")
    found = {root / candidate for root in roots for candidate in names if (root / candidate).is_dir()}
    source_root = repo / "sources"
    if source_root.is_dir():
        fragment_pattern = re.compile(rf"^Fragment-Host:\s*{re.escape(name)}(?:;|\s*$)", re.M)
        for manifest in source_root.glob("**/META-INF/MANIFEST.MF"):
            if fragment_pattern.search(read(manifest)):
                found.add(manifest.parent.parent)
    return sorted(path.resolve() for path in found if path.resolve() != plugin.resolve())


def reports(roots: list[Path]) -> dict[str, list[str]]:
    patterns = {
        "surefire_xml": "**/surefire-reports/TEST-*.xml",
        "failsafe_xml": "**/failsafe-reports/TEST-*.xml",
        "jacoco_xml": "**/jacoco*.xml",
    }
    return {key: sorted({str(path.resolve()) for root in roots for path in root.glob(pattern) if path.is_file()})
            for key, pattern in patterns.items()}


def test_totals(paths: list[str]) -> dict[str, float | int]:
    result: dict[str, float | int] = {"tests": 0, "failures": 0, "errors": 0, "skipped": 0, "time_seconds": 0.0}
    for path in paths:
        try:
            root = ET.parse(path).getroot()
        except (ET.ParseError, OSError):
            continue
        suites = [root] if root.tag.endswith("testsuite") else root.findall(".//testsuite")
        for suite in suites:
            for key in ("tests", "failures", "errors", "skipped"):
                result[key] += int(float(suite.attrib.get(key, "0")))
            result["time_seconds"] += float(suite.attrib.get("time", "0"))
    result["time_seconds"] = round(float(result["time_seconds"]), 6)
    return result


def coverage(paths: list[str]) -> dict[str, dict[str, float | int]]:
    if not paths:
        return {}
    try:
        root = ET.parse(paths[0]).getroot()
    except (ET.ParseError, OSError):
        return {}
    result = {}
    for node in root.findall("counter"):
        missed, covered = int(node.get("missed", 0)), int(node.get("covered", 0))
        total = missed + covered
        result[node.get("type", "unknown").lower()] = {
            "missed": missed, "covered": covered, "total": total,
            "ratio": round(covered / total, 6) if total else 0.0,
        }
    return result


def inspect(plugin: Path, repo: Path, environment: str) -> dict[str, object]:
    name, version = bundle(plugin)
    tests = test_projects(plugin, repo, name)
    found = reports([plugin, *tests])
    configs = [plugin / "pom.xml", plugin / "Jenkinsfile", plugin / "sonar-project.properties"]
    configs += [path / filename for path in tests for filename in ("pom.xml", "Jenkinsfile", "sonar-project.properties")]
    corpus = "\n".join(read(path).lower() for path in configs if path.is_file())
    return {
        "environment_id": environment,
        "plugin": {"path": str(plugin), "symbolic_name": name, "version": version,
                   "java_sources": java_count(plugin / "src"), "has_pom": (plugin / "pom.xml").is_file(),
                   "has_jenkinsfile": (plugin / "Jenkinsfile").is_file()},
        "test_projects": [{"path": str(path), "java_tests": java_count(path / "src")} for path in tests],
        "configuration": {"jacoco": "jacoco" in corpus, "sonarqube": "sonar" in corpus,
                          "coveralls": "coveralls" in corpus, "grafana": "grafana" in corpus,
                          "prometheus_or_pushgateway": "prometheus" in corpus or "pushgateway" in corpus},
        "tools": {name: shutil.which(name) for name in ("mvn", "sonar-scanner", "psql", "curl", "java", "docker")},
        "environment": {"secrets_present": {name: bool(os.getenv(name)) for name in SECRETS},
                        "endpoints_present": {name: bool(os.getenv(name)) for name in ENDPOINTS}},
        "reports": found,
        "tests": test_totals(found["surefire_xml"] + found["failsafe_xml"]),
        "coverage": coverage(found["jacoco_xml"]),
    }


def prometheus_label(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


def prometheus(data: dict[str, object]) -> str:
    plugin = prometheus_label(data["plugin"]["symbolic_name"])  # type: ignore[index]
    environment = prometheus_label(data["environment_id"])
    identity = f'environment="{environment}",plugin="{plugin}"'
    tests = data["tests"]  # type: ignore[assignment]
    cov = data["coverage"]  # type: ignore[assignment]
    found = data["reports"]  # type: ignore[assignment]
    passed = max(0, tests["tests"] - tests["failures"] - tests["errors"] - tests["skipped"])
    lines = ["# TYPE idempiere_plugin_tests_total gauge",
             f'idempiere_plugin_tests_total{{{identity},status="passed"}} {passed}',
             f'idempiere_plugin_tests_total{{{identity},status="failed"}} {tests["failures"] + tests["errors"]}',
             f'idempiere_plugin_tests_total{{{identity},status="skipped"}} {tests["skipped"]}',
             "# TYPE idempiere_plugin_test_time_seconds gauge",
             f'idempiere_plugin_test_time_seconds{{{identity}}} {tests["time_seconds"]}',
             "# TYPE idempiere_plugin_coverage_ratio gauge"]
    lines += [f'idempiere_plugin_coverage_ratio{{{identity},counter="{key}"}} {value["ratio"]}'
              for key, value in sorted(cov.items())]
    lines += ["# TYPE idempiere_plugin_artifact_present gauge",
              f'idempiere_plugin_artifact_present{{{identity},artifact="jacoco_xml"}} {int(bool(found["jacoco_xml"]))}',
              f'idempiere_plugin_artifact_present{{{identity},artifact="test_xml"}} {int(bool(found["surefire_xml"] or found["failsafe_xml"]))}']
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin_dir", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--environment", help="Stable environment id; defaults to the repository directory name")
    parser.add_argument("--format", choices=("json", "prometheus"), default="json")
    args = parser.parse_args()
    plugin, repo = args.plugin_dir.resolve(), args.repo_root.resolve()
    if not plugin.is_dir() or not (plugin / "META-INF" / "MANIFEST.MF").is_file():
        parser.error(f"invalid OSGi plugin directory: {plugin}")
    environment = args.environment or repo.name
    data = inspect(plugin, repo, environment)
    sys.stdout.write(prometheus(data) if args.format == "prometheus" else json.dumps(data, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
