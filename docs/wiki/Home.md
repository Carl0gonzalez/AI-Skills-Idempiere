# AI Skills for iDempiere

**English** | [Español](Inicio.md)

This library gives AI agents reusable instructions for iDempiere development. It brings plugin workflows, architecture, environment guidance and core-contribution rules into one repository, while keeping their scopes distinct. It is a skill catalog, not an OSGi plugin installed in the ERP.

- **Owner:** Carlo González, as recorded in the repository license.
- **License:** [MIT](../../LICENSE).
- **Source:** [AI-Skills-Idempiere](https://github.com/Carl0gonzalez/AI-Skills-Idempiere).
- **Status:** local documentation and content inventory; no release number or runtime certification is assigned here.

## How the catalog is organized

| Directory | Skills | Use |
|---|---:|---|
| idempiere-8, idempiere-10, idempiere-12, idempiere-13 | 15 in each | Select the actual project's target line |
| shared | 11 | Architecture, quality, environments and specialized components |
| core | 7 | Contribute to iDempiere core under the actual checkout's rules |

There are **78 entries and 33 distinct names**. A version directory expresses a target platform; it does not prove that every API or example was compiled for that version. Read [versioning](../VERSIONING.md) and [the exact per-skill revision inventory](../skill-versions.json).

## Versioned plugin workflows

Links below use the iDempiere 13 copy for browsing. Select the actual target version before applying a skill.

| Skill | Purpose |
|---|---|
| [idempiere-local-postgres](../../idempiere-13/idempiere-local-postgres/SKILL.md) | Read-only PostgreSQL diagnosis and explicit write controls. |
| [idempiere-migration-review](../../idempiere-13/idempiere-migration-review/SKILL.md) | Audit model, schema, AD and Java/OSGi consistency. |
| [idempiere-model-designer](../../idempiere-13/idempiere-model-designer/SKILL.md) | Specify entities, references, lifecycle and dictionary requirements. |
| [idempiere-pipo-integrity-review](../../idempiere-13/idempiere-pipo-integrity-review/SKILL.md) | Review dictionary/physical types and PackOut dependencies. |
| [idempiere-plugin-compiler](../../idempiere-13/idempiere-plugin-compiler/SKILL.md) | Discover the real target-platform builder and report artifacts. |
| [idempiere-plugin-version-upgrader](../../idempiere-13/idempiere-plugin-version-upgrader/SKILL.md) | Plan and verify existing-plugin upgrades on isolated release branches. |
| [idempiere-plugin-component-developer](../../idempiere-13/idempiere-plugin-component-developer/SKILL.md) | Implement processes, callouts, events and factories with compatible registration. |
| [idempiere-plugin-designer](../../idempiere-13/idempiere-plugin-designer/SKILL.md) | Translate functional requirements into minimal Java/OSGi designs. |
| [idempiere-plugin-manual-generator](../../idempiere-13/idempiere-plugin-manual-generator/SKILL.md) | Derive English functional manuals and test guides from actual code/metadata. |
| [idempiere-plugin-readme](../../idempiere-13/idempiere-plugin-readme/SKILL.md) | Write English plugin README files using repository evidence. |
| [idempiere-plugin-wiki-page](../../idempiere-13/idempiere-plugin-wiki-page/SKILL.md) | Prepare evidence-based MediaWiki pages for iDempiere plugins. |
| [idempiere-plugin-test-developer](../../idempiere-13/idempiere-plugin-test-developer/SKILL.md) | Write regression tests with the existing framework and isolated fixtures. |
| [jenkinsfile-developer](../../idempiere-13/jenkinsfile-developer/SKILL.md) | Maintain release-aware Jenkins builds and documentation pipelines. |
| [skill-architect](../../idempiere-13/skill-architect/SKILL.md) | Design focused reusable skills when an existing workflow cannot cover the task. |
| [skill-reviewer](../../idempiere-13/skill-reviewer/SKILL.md) | Review activation, scope, overlap, structure and instruction quality. |

## Shared workflows

| Skill | Purpose |
|---|---|
| [idempiere-architecture-patterns](../../shared/idempiere-architecture-patterns/SKILL.md) | Choose the smallest compatible mechanism and distinguish core, plugin and environment. |
| [idempiere-plugin-quality-gate](../../shared/idempiere-plugin-quality-gate/SKILL.md) | Coordinate test execution, coverage and honest quality evidence. |
| [crear-entornos-idempiere-envrc](../../shared/crear-entornos-idempiere-envrc/SKILL.md) | Create and review isolated direnv environments with static checks. |
| [documentar-entornos-idempiere-envrc](../../shared/documentar-entornos-idempiere-envrc/SKILL.md) | Document the operational contract of an actual .envrc. |
| [gestionar-tareas](../../shared/gestionar-tareas/SKILL.md) | Maintain an existing task registry when explicitly requested. |
| [idempiere-event-annotation](../../shared/idempiere-event-annotation/SKILL.md) | Implement focused annotated delegates using target-version APIs. |
| [idempiere-rest-resource](../../shared/idempiere-rest-resource/SKILL.md) | Define REST contracts, access checks and ResourceExtension registration. |
| [idempiere-window-validator](../../shared/idempiere-window-validator/SKILL.md) | Intercept window actions with complete callback paths. |
| [idempiere-zul-form](../../shared/idempiere-zul-form/SKILL.md) | Build ZUL forms, controllers, wiring and packaged resources. |
| [idempiere-grouped-listbox](../../shared/idempiere-grouped-listbox/SKILL.md) | Implement grouped list models, renderers and bounded data access. |
| [idempiere-wlistbox-custom-editor](../../shared/idempiere-wlistbox-custom-editor/SKILL.md) | Customize existing WListbox column editors/display behavior. |

## Core contributions

| Skill | Purpose |
|---|---|
| [idempiere-contribution-workflow](../../core/idempiere-contribution-workflow/SKILL.md) | Prepare Jira-linked branches, focused commits, documentation and PRs. |
| [idempiere-core-coding-standards](../../core/idempiere-core-coding-standards/SKILL.md) | Preserve transactions, role access, API compatibility and dual-database behavior. |
| [idempiere-database-changes](../../core/idempiere-database-changes/SKILL.md) | Specify UI changes and review developer-generated Centralized-ID migrations. |
| [idempiere-unit-tests](../../core/idempiere-unit-tests/SKILL.md) | Write/run core regression tests using declared GardenWorld fixtures. |
| [idempiere-headless-build-run](../../core/idempiere-headless-build-run/SKILL.md) | Build core and handle authorized SyncDB/server operations with exact evidence. |
| [idempiere-pr-review](../../core/idempiere-pr-review/SKILL.md) | Review in gates and test integration in an isolated worktree. |
| [idempiere-jira-tickets](../../core/idempiere-jira-tickets/SKILL.md) | Draft reproducible bug/feature reports and private security reports. |

## Selecting and using skills

1. Determine whether the work concerns a plugin, core contribution or environment.
2. Confirm the target iDempiere release, JDK, build and existing registration mechanism.
3. Read the appropriate versioned workflow, then architecture or specialized shared guidance when it adds useful detail.
4. For core, read the target AGENTS.md and its task skills first. The central adaptations never replace newer checkout rules.
5. Keep generated models unchanged; preserve owning transactions, role/client/org access and actual document lifecycle.
6. Report source/build/test/runtime evidence separately. Installation is a later decision; do not replace an existing installed skill silently.

Examples:

- A callout in an existing plugin uses architecture plus the target component skill and its established factory.
- A ZUL form uses the ZUL skill after checking the actual form API and resource packaging.
- A core bug uses the contribution, coding, test and PR-review workflows appropriate to the ticket.
- A core dictionary change is specified for human UI generation with Centralized IDs; agents review the generated scripts rather than authoring replacements.

## Requirements and validation

Reading skills needs an agent that can access Markdown and local resources. No Gemini CLI, Eclipse or specific connector is required merely to read the catalog. Implementation/build requirements come from the target project. Catalog validation uses Python 3 and PyYAML; the PR helper uses Git 2.31+, Bash 3.2+ and a local Git identity.

From the repository root:

```bash
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
python3 tests/test_review_pr.py
```

The adoption review records 78 validated entries and ten passing local Git-helper scenarios. Those checks do not compile Java, activate OSGi, import 2Pack or validate PostgreSQL/Oracle/UI behavior. See [the review](../ADOPTION_REVIEW.es.md) for the precise boundaries.

## Revision policy

Skill content revisions are SHA-256 digests of instructions and resources. Target iDempiere lines, content revisions, upstream source commits and published releases are separate concepts. No “Tested with release” status is inferred from this repository's version directories or main branch. Future releases need an agreed tag and explicit evidence.

## Sources and maintenance

[Provenance](../SOURCES.md) records the existing catalog, installed custom skills, Hengsin's component pack and the seven upstream core workflows. Public GitHub links identify the source repository; local additions require a separate commit/push before appearing remotely.

The catalog is MIT-licensed. Follow the target core/plugin license headers when implementing code. A future update should check scope/overlap, review all affected version copies, validate resources and refresh the content inventory.

## Documentation

- [Root README](../../README.md).
- [Version selection and revisions](../VERSIONING.md).
- [Shared catalog](../../shared/README.md) and [core catalog](../../core/README.md).
- [Installed custom-skill snapshot](../INSTALLED_SKILLS_INVENTORY.md).
- [Local wiki formats and publication state](README.md).
