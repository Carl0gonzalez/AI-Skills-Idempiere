# iDempiere 14 Skills

**English** | [Español](README.es.md)

This directory contains **15 skills targeting iDempiere 14 projects**. It identifies the intended platform, not the release number of each skill or proof of Java/OSGi/database compatibility. Inspect the actual project APIs, scaffold and build before applying a workflow.

## Catalog

| Skill | Purpose |
|---|---|
| [idempiere-local-postgres](idempiere-local-postgres/SKILL.md) | Read-only PostgreSQL diagnosis and explicit write controls. |
| [idempiere-migration-review](idempiere-migration-review/SKILL.md) | Audit model, schema, AD and Java/OSGi consistency. |
| [idempiere-model-designer](idempiere-model-designer/SKILL.md) | Specify entities, references, lifecycle and dictionary requirements. |
| [idempiere-pipo-integrity-review](idempiere-pipo-integrity-review/SKILL.md) | Review dictionary/physical types and PackOut dependencies. |
| [idempiere-plugin-compiler](idempiere-plugin-compiler/SKILL.md) | Discover the real target-platform builder and report artifacts. |
| [idempiere-plugin-version-upgrader](idempiere-plugin-version-upgrader/SKILL.md) | Plan and verify existing-plugin upgrades on isolated release branches. |
| [idempiere-plugin-component-developer](idempiere-plugin-component-developer/SKILL.md) | Implement processes, callouts, events and factories with compatible registration. |
| [idempiere-plugin-designer](idempiere-plugin-designer/SKILL.md) | Translate functional requirements into minimal Java/OSGi designs. |
| [idempiere-plugin-manual-generator](idempiere-plugin-manual-generator/SKILL.md) | Derive English functional manuals and test guides from actual code/metadata. |
| [idempiere-plugin-readme](idempiere-plugin-readme/SKILL.md) | Write English plugin README files using repository evidence. |
| [idempiere-plugin-wiki-page](idempiere-plugin-wiki-page/SKILL.md) | Prepare evidence-based MediaWiki pages for iDempiere plugins. |
| [idempiere-plugin-test-developer](idempiere-plugin-test-developer/SKILL.md) | Write regression tests with the existing framework and isolated fixtures. |
| [jenkinsfile-developer](jenkinsfile-developer/SKILL.md) | Maintain release-aware Jenkins builds and documentation pipelines. |
| [skill-architect](skill-architect/SKILL.md) | Design focused reusable skills when an existing workflow cannot cover the task. |
| [skill-reviewer](skill-reviewer/SKILL.md) | Review activation, scope, overlap, structure and instruction quality. |

## Selecting complementary skills

Select this version set once. Add relevant [shared skills](../shared/README.md) for architecture, quality, environments, REST and ZK. Read [core guidance](../core/README.md) only for core contributions; the actual checkout's AGENTS.md and local skills take precedence. Do not install multiple version copies with the same name together.

## Revisions and maintenance

See [skill versioning](../docs/VERSIONING.md) and [the exact content inventory](../docs/skill-versions.json). Version-specific entrypoints and resources are tracked separately. Changes common to releases must be reviewed in all affected copies; APIs must not be propagated blindly. Use repository validation before considering installation.

## Use and validation

Ask the agent to read the relevant SKILL.md and only the necessary resources. Each skill lives in its own directory and has name/description metadata. Installing, committing, publishing or applying database changes is a separate authorized action.

From the repository root:

```bash
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
```

See the [English wiki](../docs/wiki/Home.md), [root README](../README.md) and [adoption review](../docs/ADOPTION_REVIEW.es.md). This documentation update does not install skills.
