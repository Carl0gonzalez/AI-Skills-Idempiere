#!/usr/bin/env python3
"""Selective, collision-safe local install. Dry run unless --apply is passed."""
import argparse
import hashlib
import json
from pathlib import Path
import os
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plan(root, home):
    entries = []
    for source in sorted((root / "skills").iterdir()):
        if (source / "SKILL.md").is_file():
            entries.append({"kind": "skill", "source": str(source.resolve()),
                            "destination": str(home / ".agents/skills" / source.name)})
    for source in sorted((root / "agents").glob("*.toml")):
        entries.append({"kind": "agent", "source": str(source.resolve()),
                        "destination": str(home / ".codex/agents" / source.name),
                        "sha256": sha(source)})
    return entries


def matches(entry):
    dst = Path(entry["destination"])
    if entry["kind"] == "skill":
        return dst.is_symlink() and os.readlink(dst) == entry["source"]
    return dst.is_file() and not dst.is_symlink() and sha(dst) == entry["sha256"]


def state_path(root, home):
    key = hashlib.sha256(str(home).encode()).hexdigest()[:16]
    return root / ".local-state" / (key + ".json")


def create_file(destination, content):
    """Publish complete content exclusively; never truncate an existing file."""
    name = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as handle:
            name = Path(handle.name)
            handle.write(content)
        os.link(name, destination)
    finally:
        if name is not None:
            name.unlink(missing_ok=True)


def install(root, home, apply=False):
    entries = plan(root, home)
    state = state_path(root, home)
    previous = json.loads(state.read_text()) if state.exists() else None
    if previous and (previous["home"] != str(home) or previous["entries"] != entries):
        raise ValueError("Installed manifest differs; review/update explicitly before replacing files")
    # Preflight all destinations before performing any mutation.
    for entry in entries:
        dst = Path(entry["destination"])
        if dst.exists() or dst.is_symlink():
            if not previous or not matches(entry):
                raise ValueError("Destination collision (left unchanged): " + str(dst))
    if not apply:
        return {"action": "dry_run", "home": str(home), "entries": entries}
    created = []
    try:
        for entry in entries:
            dst = Path(entry["destination"])
            if dst.exists() or dst.is_symlink():
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            if entry["kind"] == "skill":
                dst.symlink_to(entry["source"], target_is_directory=True)
            else:
                create_file(dst, Path(entry["source"]).read_bytes())
            created.append(entry)
        state.parent.mkdir(parents=True, exist_ok=True)
        # Do not rewrite a manifest on an idempotent repeat.
        if previous is None:
            payload = json.dumps({"home": str(home), "entries": entries}, ensure_ascii=False, indent=2)
            create_file(state, (payload + "\n").encode())
    except Exception:
        for entry in reversed(created):
            if matches(entry):
                Path(entry["destination"]).unlink()
        raise
    return {"action": "installed", "new_entries": len(created), "total": len(entries),
            "manifest": str(state)}


def uninstall(root, home, apply=False):
    state = state_path(root, home)
    if not state.exists():
        raise ValueError("No installation manifest for this home")
    previous = json.loads(state.read_text())
    # Validate against the fixed destinations, not arbitrary paths from a manifest.
    expected = {(e["kind"], e["source"], e["destination"]) for e in plan(root, home)}
    entries = previous["entries"]
    if previous["home"] != str(home) or len(entries) != len(expected) or {
        (e["kind"], e["source"], e["destination"]) for e in entries
    } != expected:
        raise ValueError("Manifest scope does not match this package")
    for entry in entries:
        dst = Path(entry["destination"])
        if (dst.exists() or dst.is_symlink()) and not matches(entry):
            raise ValueError("Installed entry was changed; preserved: " + str(dst))
    if not apply:
        return {"action": "uninstall_dry_run", "entries": entries}
    for entry in entries:
        dst = Path(entry["destination"])
        if dst.exists() or dst.is_symlink():
            dst.unlink()
    state.unlink()
    return {"action": "uninstalled", "entries": len(entries)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--uninstall", action="store_true")
    args = parser.parse_args()
    home = args.home.expanduser().resolve()
    try:
        result = (uninstall if args.uninstall else install)(ROOT, home, args.apply)
    except (OSError, ValueError, KeyError) as exc:
        parser.exit(2, str(exc) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
