#!/usr/bin/env python3
"""Read-only validation of metadata, local resources and version inventory."""
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
skills = sorted(ROOT.glob('*/*/SKILL.md'))
by_group = {}
for path in skills:
    relative = path.relative_to(ROOT)
    text = path.read_text()
    if not text.startswith('---\n'):
        errors.append(f'{relative}: missing YAML frontmatter')
        continue
    try:
        metadata = yaml.safe_load(text.split('---', 2)[1])
        if not isinstance(metadata, dict):
            raise ValueError('metadata must be a mapping')
        if metadata.get('name') != path.parent.name:
            raise ValueError('name does not match directory')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', metadata['name']) or len(metadata['name']) > 64:
            raise ValueError('invalid skill name')
        if not isinstance(metadata.get('description'), str) or not metadata['description'].strip():
            raise ValueError('missing description')
    except (yaml.YAMLError, ValueError, KeyError, IndexError) as exc:
        errors.append(f'{relative}: {exc}')
    by_group.setdefault(relative.parts[0], set()).add(path.parent.name)
for path in ROOT.rglob('*.md'):
    if '.git' in path.parts:
        continue
    # Remove fenced code: example paths/snippets are not resource links.
    text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
    text = re.sub(r'`[^`]*`', '', text)
    for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        target = target.split('#', 1)[0].strip().strip('<>')
        if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        target = target.split(' "', 1)[0]
        if not (path.parent / target).exists():
            errors.append(f'{path.relative_to(ROOT)}: missing local link {target}')
versions = [by_group.get(f'idempiere-{v}', set()) for v in (8, 10, 12, 13)]
if any(names != versions[0] for names in versions[1:]):
    errors.append('Version directories contain different skill inventories')
for group in ('shared', 'core'):
    duplicate = by_group.get(group, set()) & versions[0]
    if duplicate:
        errors.append(f'{group}: duplicate versioned skill names {sorted(duplicate)}')
if by_group.get('shared', set()) & by_group.get('core', set()):
    errors.append('shared/core name collision')
for group, names in sorted(by_group.items()):
    print(f'{group}: {len(names)} skills')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(skills)} entries; metadata, resource links and inventories are consistent.')
