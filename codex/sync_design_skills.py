#!/usr/bin/env python3
"""Keep portable versioned copies aligned with their shared source."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("idempiere-model-designer", "idempiere-plugin-designer", "idempiere-migration-review")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    differences = []
    for name in NAMES:
        source = ROOT / "shared" / name
        for item in sorted(source.rglob("*")):
            if not item.is_file():
                continue
            for version in (8, 10, 12, 13, 14):
                target = ROOT / f"idempiere-{version}" / name / item.relative_to(source)
                if not target.is_file() or target.read_bytes() != item.read_bytes():
                    differences.append(str(target.relative_to(ROOT)))
                    if not args.check:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copyfile(item, target)
    print(f"{'Out of sync' if args.check else 'Updated'}: {len(differences)} files")
    if args.check and differences:
        print("\n".join(differences))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
