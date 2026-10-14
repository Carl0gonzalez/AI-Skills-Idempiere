# Skill versions and target platforms

**English** | [Español](VERSIONING.es.md)

Three different identifiers must remain distinct:

| Identifier | Meaning | Evidence |
|---|---|---|
| iDempiere target line | Project family the instructions target: 8, 10, 12, 13 or 14 | Version directory and actual target checkout |
| Skill content revision | Exact instructions plus scripts, references, assets and UI metadata | SHA-256 in [skill-versions.json](skill-versions.json) |
| Published catalog release | A repository release/tag deliberately issued by the maintainer | Git tag/release; none is assigned by this documentation update |

The local branch is `main`; no local release tags or semantic release branches were found during the 2026-10-14 documentation review. The five version directories are target sets, not five software releases. In particular, the presence of an iDempiere 13 directory does not justify “Tested with release 13.0.0”.

## Catalog matrix

| Scope | Entries | Intended use | Compatibility evidence |
|---|---:|---|---|
| [idempiere-8](../idempiere-8/README.md) | 15 | Projects targeting iDempiere 8 | Discover/verify actual release APIs and build |
| [idempiere-10](../idempiere-10/README.md) | 15 | Projects targeting iDempiere 10 | Discover/verify actual release APIs and build |
| [idempiere-12](../idempiere-12/README.md) | 15 | Projects targeting iDempiere 12 | Discover/verify actual release APIs and build |
| [idempiere-13](../idempiere-13/README.md) | 15 | Projects targeting iDempiere 13 | Discover/verify actual release APIs and build |
| [idempiere-14](../idempiere-14/README.md) | 15 | Projects targeting iDempiere 14 development | Discover/verify actual release APIs and build |
| [shared](../shared/README.md) | 11 | Architecture, quality, environments, tasks and specialized components | No blanket release support; check every required API |
| [core](../core/README.md) | 7 | Contributions to the actual core checkout | Actual core rules and release prevail over the pinned adaptation |

Total: **93 entries, 33 distinct names**. Duplicate names across version sets are intentional copies. Install only one target copy of a given name in an agent library.

## Exact per-skill revisions

The machine-readable inventory lists every entry's name, path, scope, target line, resource count and full content digest. The digest covers relative resource names and file contents, including `SKILL.md`. Moving a resource or changing an asset changes that skill's revision; changing only a repository README does not.

The catalog digest also covers entry paths, so it identifies the complete distribution. It is a content identifier, not semantic versioning or a claim of compatibility. Equivalent files in different target folders may share a skill digest while remaining distinct catalog entries.

From the repository root, with Python 3:

```bash
python3 scripts/catalog_versions.py --check
```

After reviewing an intended skill/resource change:

```bash
python3 scripts/catalog_versions.py --write
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
```

`--check` is read-only. `--write` updates only `docs/skill-versions.json`; it does not install, commit or publish anything. The catalog validator additionally needs PyYAML.

## Source baselines and future releases

The adapted core workflows reference upstream commit `75ad26081a1745ab64831567861ad8f9f6f78d36`. Component guidance was reviewed against Hengsin's pack at `a7ec5db8f7459ad67fd0753e0f314ba69021a9cb`. These are upstream source baselines, not release numbers of this catalog. See [sources](SOURCES.md).

Before issuing a release, review changed workflows, validate resources/scripts, update the content inventory and documentation, and agree on a tag and release notes. A future version number must not be inferred from an iDempiere directory name. Published compatibility claims need separate build/runtime evidence.

## Installed versus versioned state

[The installed custom-skill snapshot](INSTALLED_SKILLS_INVENTORY.md) records earlier installed entrypoint hashes. This content inventory records the current repository skills and all their resources. They serve different purposes. Repository improvements do not automatically update installed skills; installation conflicts and target selection are reviewed separately.

## iDempiere 14 development baseline

The new set contains 15 instruction workflows, including the previously adopted Hengsin/core improvements. [14.0.0-SNAPSHOT, JDK 17, Tycho 4.0.8](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/org.idempiere.parent/pom.xml). The builder/CI guidance discovers actual compatible images; no source-release-14 tag is assumed.
