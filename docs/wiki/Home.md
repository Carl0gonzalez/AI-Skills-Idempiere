# AI Skills for iDempiere

**English** | [Español](Inicio.md)

Reusable skills for iDempiere plugin development, data modeling, testing, documentation, environments and core contributions.

## Organization

| Directory | Entries | Scope |
|---|---:|---|
| [idempiere-8](../../idempiere-8/README.md) | 15 | iDempiere 8 |
| [idempiere-10](../../idempiere-10/README.md) | 15 | iDempiere 10 |
| [idempiere-12](../../idempiere-12/README.md) | 15 | iDempiere 12 |
| [idempiere-13](../../idempiere-13/README.md) | 15 | iDempiere 13 |
| [idempiere-14](../../idempiere-14/README.md) | 15 | iDempiere 14 development |
| [shared](../../shared/README.md) | 11 | Common workflows |
| [core](../../core/README.md) | 7 | Core contributions |

**93 entries and 33 distinct skill names.** Each versioned set contains the same 15 workflow names.

## Plugin skills

| Skill | Purpose |
|---|---|
| [idempiere-local-postgres](../../idempiere-14/idempiere-local-postgres/SKILL.md) | Read-only PostgreSQL diagnosis and explicit write controls. |
| [idempiere-migration-review](../../idempiere-14/idempiere-migration-review/SKILL.md) | Audit model, schema, AD and Java/OSGi consistency. |
| [idempiere-model-designer](../../idempiere-14/idempiere-model-designer/SKILL.md) | Specify entities, references, lifecycle and dictionary requirements. |
| [idempiere-pipo-integrity-review](../../idempiere-14/idempiere-pipo-integrity-review/SKILL.md) | Review dictionary/physical types and PackOut dependencies. |
| [idempiere-plugin-compiler](../../idempiere-14/idempiere-plugin-compiler/SKILL.md) | Discover the real target-platform builder and report artifacts. |
| [idempiere-plugin-version-upgrader](../../idempiere-14/idempiere-plugin-version-upgrader/SKILL.md) | Plan and verify existing-plugin upgrades on isolated release branches. |
| [idempiere-plugin-component-developer](../../idempiere-14/idempiere-plugin-component-developer/SKILL.md) | Implement processes, callouts, events and factories with compatible registration. |
| [idempiere-plugin-designer](../../idempiere-14/idempiere-plugin-designer/SKILL.md) | Translate functional requirements into minimal Java/OSGi designs. |
| [idempiere-plugin-manual-generator](../../idempiere-14/idempiere-plugin-manual-generator/SKILL.md) | Derive English functional manuals and test guides from actual code/metadata. |
| [idempiere-plugin-readme](../../idempiere-14/idempiere-plugin-readme/SKILL.md) | Write English plugin README files using repository evidence. |
| [idempiere-plugin-wiki-page](../../idempiere-14/idempiere-plugin-wiki-page/SKILL.md) | Prepare evidence-based MediaWiki pages for iDempiere plugins. |
| [idempiere-plugin-test-developer](../../idempiere-14/idempiere-plugin-test-developer/SKILL.md) | Write regression tests with the existing framework and isolated fixtures. |
| [jenkinsfile-developer](../../idempiere-14/jenkinsfile-developer/SKILL.md) | Maintain release-aware Jenkins builds and documentation pipelines. |
| [skill-architect](../../idempiere-14/skill-architect/SKILL.md) | Design focused reusable skills when an existing workflow cannot cover the task. |
| [skill-reviewer](../../idempiere-14/skill-reviewer/SKILL.md) | Review activation, scope, overlap, structure and instruction quality. |

The links above point to the iDempiere 14 set. Select the directory matching the project version.

## Shared skills

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

## Core contribution skills

| Skill | Purpose |
|---|---|
| [idempiere-contribution-workflow](../../core/idempiere-contribution-workflow/SKILL.md) | Prepare Jira-linked branches, focused commits, documentation and PRs. |
| [idempiere-core-coding-standards](../../core/idempiere-core-coding-standards/SKILL.md) | Preserve transactions, role access, API compatibility and dual-database behavior. |
| [idempiere-database-changes](../../core/idempiere-database-changes/SKILL.md) | Specify UI changes and review developer-generated Centralized-ID migrations. |
| [idempiere-unit-tests](../../core/idempiere-unit-tests/SKILL.md) | Write/run core regression tests using declared GardenWorld fixtures. |
| [idempiere-headless-build-run](../../core/idempiere-headless-build-run/SKILL.md) | Build core and handle authorized SyncDB/server operations with exact evidence. |
| [idempiere-pr-review](../../core/idempiere-pr-review/SKILL.md) | Review in gates and test integration in an isolated worktree. |
| [idempiere-jira-tickets](../../core/idempiere-jira-tickets/SKILL.md) | Draft reproducible bug/feature reports and private security reports. |

## Usage

1. Select the versioned directory matching the iDempiere project.
2. Add the shared workflows needed for architecture, quality, REST, ZK or environment work.
3. Use core workflows only for core contributions. The target checkout's AGENTS.md and local instructions take precedence.
4. Read SKILL.md and the referenced resources before performing the task.

For Codex, copy each selected skill directory into the project's `.agents/skills/`. Shared/core skills can be placed in the user's global skill library. Copy the entire directory, including scripts, references and assets. Do not load multiple version copies of the same skill name or overwrite existing customizations without reviewing them.

## Target versions

The version folders identify the intended iDempiere line. The project source, JDK, APIs, target platform and builder determine actual compatibility. iDempiere 14 targets development sources; inspect the selected source revision before building.

Skill revisions are maintained through Git history. See [version selection](../../docs/VERSIONING.md). The companion [idempiere-dev-environments repository](https://github.com/Carl0gonzalez/idempiere-dev-environments) provides isolated development-environment guidance.

## Documentation

- [English wiki](https://github.com/Carl0gonzalez/AI-Skills-Idempiere/wiki/Home).
- [Spanish wiki](https://github.com/Carl0gonzalez/AI-Skills-Idempiere/wiki/Inicio).
- [Wiki source files](../../docs/wiki/README.md).
- [Sources](../../docs/SOURCES.md).

## Maintenance

Keep skill names and activation criteria specific. Reuse existing workflows before adding another skill. Keep required resources inside the skill directory. Review affected version copies when changing shared behavior and update the English/Spanish catalogs together.

## License

[MIT](../../LICENSE). Copyright © 2026 Carlo González.
