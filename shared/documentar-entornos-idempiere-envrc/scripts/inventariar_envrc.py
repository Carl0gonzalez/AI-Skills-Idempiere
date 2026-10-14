#!/usr/bin/env python3
"""Extrae hechos documentables de un .envrc sin evaluarlo."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


INTERESTING = (
    "IDEMPIERE_BRANCH_EXPECTED",
    "IDEMPIERE_OFFICIAL_URL",
    "IDEMPIERE_GIT_CONFIG",
    "IDEMPIERE_HOME",
    "IDEMPIERE_REPOSITORY",
    "SOURCES_DIR",
    "ECLIPSE_HOME",
    "ECLIPSE_WORKSPACE",
    "ECLIPSE_P2",
    "MAVEN_HOME",
    "MAVEN_USER_HOME",
    "MVN_LOCAL_REPO",
    "MAVEN_USER_SETTINGS",
    "MAVEN_OPTS",
    "BIN_DIR",
    "JAVA_HOME",
)


def clean_value(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def inventory(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    assignments: dict[str, str] = {}
    assignment_re = re.compile(
        r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)=(.*)$", re.M
    )
    for name, value in assignment_re.findall(text):
        if (name in INTERESTING or name.endswith("_ROOT")) and name not in assignments:
            assignments[name] = clean_value(value)

    wrappers = re.findall(
        r"cat\s*>\s*[\"']?\$BIN_DIR/([^\"'\s]+)[\"']?", text
    )
    java_candidates = re.findall(r"[\"'](/usr/lib/jvm/[^\"']+)[\"']", text)
    path_mentions = []
    for marker in (".m2", ".p2", ".local-bin", "eclipse", "workspace", "sources"):
        if marker in text:
            path_mentions.append(marker)

    return {
        "file": str(path),
        "lines": len(text.splitlines()),
        "variables": assignments,
        "commands": list(dict.fromkeys(wrappers)),
        "java_candidates": list(dict.fromkeys(java_candidates)),
        "mentioned_path_markers": path_mentions,
        "features": {
            "direnv": "expand_path" in text or "PATH_add" in text,
            "maven_wrapper": "mvnw" in text,
            "local_maven_distribution": "MAVEN_HOME" in assignments,
            "git_modes": "IDEMPIERE_GIT_MODE" in text,
            "persistent_git_config": ".idempiere-git.env" in text,
            "doctor": "idempiere-doctor" in text,
            "separate_workspace": "ECLIPSE_WORKSPACE" in text and "SOURCES_DIR" in text,
        },
    }


def markdown(data: dict[str, object]) -> str:
    variables = data["variables"]
    features = data["features"]
    rows = [
        f"# Inventario de `{data['file']}`",
        "",
        f"- Líneas: {data['lines']}",
        "- Comandos: " + (", ".join(f"`{x}`" for x in data["commands"]) or "ninguno"),
        "- Marcadores de rutas mencionados: "
        + (", ".join(data["mentioned_path_markers"]) or "ninguno"),
        "",
        "## Variables relevantes",
        "",
        "| Variable | Expresión en `.envrc` |",
        "|---|---|",
    ]
    rows.extend(f"| `{key}` | `{value}` |" for key, value in variables.items())
    rows.extend(["", "## Capacidades detectadas", ""])
    rows.extend(f"- {key}: {'sí' if value else 'no'}" for key, value in features.items())
    if data["java_candidates"]:
        rows.extend(["", "## Candidatos de Java", ""])
        rows.extend(f"- `{value}`" for value in data["java_candidates"])
    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("envrc", type=Path)
    parser.add_argument("--json", action="store_true", help="emitir JSON")
    args = parser.parse_args()
    if not args.envrc.is_file():
        parser.error(f"no existe el archivo: {args.envrc}")
    data = inventory(args.envrc)
    print(json.dumps(data, indent=2, ensure_ascii=False) if args.json else markdown(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
