#!/usr/bin/env python3
"""Validate package structure, TOML agents, skill frontmatter and local resources."""
import ast
from pathlib import Path
import re
import sys
import tomllib
import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    skills = list((root / "skills").glob("*/SKILL.md"))
    agents = list((root / "agents").glob("*.toml"))
    if len(skills) != 7 or len(agents) != 6:
        errors.append("Expected 7 skills and 6 agents")
    for path in skills:
        text = path.read_text()
        try:
            meta = yaml.safe_load(text.split("---", 2)[1])
            assert meta["name"] == path.parent.name
            assert isinstance(meta["description"], str) and 0 < len(meta["description"]) <= 1024
            assert set(meta) <= {"name", "description", "license", "metadata"}
        except (AssertionError, IndexError, TypeError, KeyError, yaml.YAMLError) as exc:
            errors.append(str(path) + ": invalid skill metadata: " + str(exc))
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if "://" not in target and not (path.parent / target.split("#")[0]).exists():
                errors.append(str(path) + ": missing resource " + target)
    for path in agents:
        try:
            data = tomllib.loads(path.read_text())
            assert data["name"] == path.stem
            assert set(data) == {"name", "description", "developer_instructions"}
            assert all(isinstance(v, str) and v for v in data.values())
        except (AssertionError, tomllib.TOMLDecodeError, KeyError) as exc:
            errors.append(str(path) + ": invalid agent: " + str(exc))
    for path in root.rglob("*.py"):
        try:
            ast.parse(path.read_bytes(), filename=str(path))
        except SyntaxError as exc:
            errors.append(str(exc))
    return {"skills": len(skills), "agents": len(agents), "errors": errors}


if __name__ == "__main__":
    result = validate()
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    sys.exit(bool(result["errors"]))
