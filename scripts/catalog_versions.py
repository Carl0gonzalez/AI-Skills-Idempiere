#!/usr/bin/env python3
"""Record or verify exact skill-directory content revisions, without release claims."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / 'docs/skill-versions.json'

def inventory():
    entries = []
    for entry in sorted(ROOT.glob('*/*/SKILL.md')):
        folder = entry.parent
        group = folder.parent.name
        digest = hashlib.sha256()
        files = sorted(p for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')
        for file in files:
            if file.is_symlink():
                raise ValueError(f'Skill resource must be self-contained: {file.relative_to(ROOT)}')
            digest.update(file.relative_to(folder).as_posix().encode() + b'\0')
            digest.update(hashlib.sha256(file.read_bytes()).digest())
        target = group.split('-', 1)[1] if group.startswith('idempiere-') else 'discover-from-target-checkout'
        entries.append({'name': folder.name, 'path': folder.relative_to(ROOT).as_posix(),
                        'scope': group, 'target_idempiere': target,
                        'content_revision': 'sha256:' + digest.hexdigest(), 'resource_count': len(files)})
    total = hashlib.sha256(json.dumps(entries, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return {'schema_version': 1, 'revision_scheme': 'SHA-256 over relative file names and file digests',
            'status': 'content inventory; not a published release or runtime compatibility certification',
            'catalog_revision': 'sha256:' + total, 'distinct_names': len({e['name'] for e in entries}),
            'entry_count': len(entries), 'skills': entries}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true', help='update the local tracked inventory file')
    mode.add_argument('--check', action='store_true', help='read-only check against current skill resources')
    args = parser.parse_args()
    data = inventory()
    if args.write:
        DESTINATION.parent.mkdir(parents=True, exist_ok=True)
        DESTINATION.write_text(json.dumps(data, indent=2) + '\n')
        print(f'Wrote {data["entry_count"]} content revisions to {DESTINATION.relative_to(ROOT)}')
    else:
        if not DESTINATION.is_file() or json.loads(DESTINATION.read_text()) != data:
            print('Skill inventory is missing or stale; review changes then run --write.', file=sys.stderr)
            return 1
        print(f'PASS: {data["entry_count"]} content revisions match the skill resources.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
