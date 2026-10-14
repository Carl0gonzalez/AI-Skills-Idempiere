#!/usr/bin/env python3
"""Auditoría estática y no destructiva de uno o más archivos .envrc."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path


ISOLATION_MARKERS = {
    "Maven local": (".m2", "MVN_LOCAL_REPO", "MAVEN_USER_HOME"),
    "P2 local": (".p2", "ECLIPSE_P2"),
    "workspace": ("ECLIPSE_WORKSPACE", "workspace-"),
    "fuentes": ("SOURCES_DIR", "sources/"),
    "wrappers": ("BIN_DIR", ".local-bin"),
}

DANGEROUS = {
    "reset destructivo": re.compile(r"\bgit\s+reset\s+--hard\b"),
    "limpieza destructiva": re.compile(r"\bgit\s+clean\s+-[^\n]*f"),
    "push forzado": re.compile(r"\bgit\s+push\s+[^\n]*(?:--force|-f(?:\s|$))"),
    "borrado recursivo": re.compile(r"\brm\s+-[^\n]*(?:r[^\n]*f|f[^\n]*r)"),
}


def line_numbers(text: str, pattern: re.Pattern[str]) -> list[int]:
    return [i for i, line in enumerate(text.splitlines(), 1) if pattern.search(line)]


def inspect(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    warnings: list[str] = []

    syntax = subprocess.run(
        ["bash", "-n", str(path)], capture_output=True, text=True, check=False
    )
    if syntax.returncode:
        errors.append(f"bash -n: {syntax.stderr.strip() or 'error de sintaxis'}")

    for label, pattern in DANGEROUS.items():
        matches = line_numbers(text, pattern)
        if matches:
            errors.append(f"{label} en línea(s) {', '.join(map(str, matches))}")

    hardcoded_home = re.compile(r"/home/[A-Za-z0-9._-]+/")
    for number, line in enumerate(lines, 1):
        if hardcoded_home.search(line) and not line.lstrip().startswith("#"):
            warnings.append(f"ruta personal hardcodeada en línea {number}")

    pre_wrappers = text.split("cat >", 1)[0]
    strict = line_numbers(pre_wrappers, re.compile(r"^\s*set\s+-[^\n]*(?:e|u)"))
    if strict:
        warnings.append(
            "modo estricto activado en el cuerpo evaluado por direnv "
            f"(línea(s) {', '.join(map(str, strict))})"
        )

    missing = [
        label
        for label, markers in ISOLATION_MARKERS.items()
        if not any(marker in text for marker in markers)
    ]
    if missing:
        warnings.append("sin marcador de aislamiento para: " + ", ".join(missing))

    if "MAVEN_HOME" not in text and "mvnw" not in text:
        warnings.append("no se detectó Maven local ni Maven Wrapper")
    if "JAVA_HOME" not in text:
        warnings.append("no se detectó configuración de JAVA_HOME")
    if "PATH_add" not in text:
        warnings.append("no se detectó PATH_add")

    accumulating_opts = re.compile(
        r'^\s*export\s+MAVEN_OPTS=["\']\$\{MAVEN_OPTS:-\}[^"\']*["\']', re.M
    )
    if accumulating_opts.search(text):
        warnings.append("MAVEN_OPTS puede acumular opciones en recargas sucesivas")

    sourced_config = re.compile(
        r'^\s*(?:source|\.)\s+["\']?\$\{?IDEMPIERE_GIT_CONFIG\}?', re.M
    )
    if sourced_config.search(text):
        warnings.append("la configuración Git persistida se evalúa como código shell")

    wildcard_chmod = line_numbers(text, re.compile(r"\bchmod\s+[^\n]*\*"))
    if wildcard_chmod:
        warnings.append(
            "chmod usa comodín en línea(s) " + ", ".join(map(str, wildcard_chmod))
        )

    wrappers = re.findall(
        r"cat\s*>\s*[\"']?\$BIN_DIR/([^\"'\s]+)[\"']?", text
    )
    exports = re.findall(r"^\s*export\s+([A-Za-z_][A-Za-z0-9_]*)=", text, re.M)

    return {
        "path": str(path),
        "lines": len(lines),
        "bash_syntax": "ok" if syntax.returncode == 0 else "error",
        "exports": sorted(set(exports)),
        "wrappers": list(dict.fromkeys(wrappers)),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("envrc", nargs="+", type=Path)
    parser.add_argument("--json", action="store_true", help="emitir JSON")
    parser.add_argument(
        "--strict", action="store_true", help="tratar advertencias como fallo"
    )
    args = parser.parse_args()

    results = []
    missing = False
    for path in args.envrc:
        if not path.is_file():
            results.append({"path": str(path), "errors": ["archivo inexistente"], "warnings": []})
            missing = True
        else:
            results.append(inspect(path))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for result in results:
            print(f"{result['path']}: {result.get('bash_syntax', 'n/a')}")
            wrappers = result.get("wrappers", [])
            print("  wrappers: " + (", ".join(wrappers) if wrappers else "ninguno"))
            for item in result["errors"]:
                print(f"  ERROR: {item}")
            for item in result["warnings"]:
                print(f"  AVISO: {item}")

    has_errors = missing or any(result["errors"] for result in results)
    has_warnings = any(result["warnings"] for result in results)
    return 2 if has_errors else (1 if args.strict and has_warnings else 0)


if __name__ == "__main__":
    raise SystemExit(main())
