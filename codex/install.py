#!/usr/bin/env python3
"""Install the local specialist pilot; dry-run unless --apply is supplied."""
import argparse
import json
import os
from pathlib import Path
import sys
import tomllib

REPO = Path(__file__).resolve().parents[1]
SKILLS = ("idempiere-model-designer", "idempiere-plugin-designer", "idempiere-migration-review")


def plan(home):
    result = []
    for name in SKILLS:
        source = REPO / "shared" / name
        if not (source / "SKILL.md").is_file():
            raise ValueError(f"Missing skill: {source}")
        # Avoid a second user-level registration in the legacy location.
        legacy = home / ".codex/skills" / name
        if os.path.lexists(legacy):
            raise ValueError(f"Existing legacy skill; review before installing: {legacy}")
        result.append((home / ".agents/skills" / name, source, None))
    for source in sorted((REPO / "codex/agents").glob("*.toml")):
        data = tomllib.loads(source.read_text())
        instructions = data["developer_instructions"].replace("__SKILLS_ROOT__", str(REPO / "shared"))
        content = "\n".join(f"{key} = {json.dumps(value, ensure_ascii=False)}" for key, value in (
            ("name", data["name"]), ("description", data["description"]),
            ("developer_instructions", instructions))) + "\n"
        tomllib.loads(content)
        result.append((home / ".codex/agents" / source.name, None, content))
    return result


def same(path, source, content):
    if source is not None:
        return path.is_symlink() and path.resolve() == source.resolve()
    return not path.is_symlink() and path.is_file() and path.read_text() == content


def run(home, apply=False, uninstall=False):
    entries = plan(home)
    # Preflight every conflict before making any changes. Never overwrite custom files.
    for path, source, content in entries:
        if os.path.lexists(path) and not same(path, source, content):
            raise ValueError(f"Conflict; unchanged: {path}")
    for path, source, content in entries:
        exists = os.path.lexists(path)
        action = "remove" if uninstall and exists else "keep" if exists or uninstall else "create"
        print(f"{action}: {path}")
        if not apply or action == "keep":
            continue
        if uninstall:
            path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            if source is not None:
                path.symlink_to(source, target_is_directory=True)
            else:
                # Exclusive creation also protects against a late file conflict.
                with path.open("x") as stream:
                    stream.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home(), help="User home (or isolated test home)")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()
    try:
        run(args.home.expanduser().resolve(), args.apply, args.uninstall)
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
