# iDempiere Skills Repository

**English** | [Español](README.es.md)

> A versioned library of reusable AI-agent skills for designing, developing, validating, and operating iDempiere solutions.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![iDempiere 8](https://img.shields.io/badge/iDempiere-8-4B7BEC)](idempiere-8/)
[![iDempiere 10](https://img.shields.io/badge/iDempiere-10-20BF6B)](idempiere-10/)
[![iDempiere 12](https://img.shields.io/badge/iDempiere-12-8854D0)](idempiere-12/)
[![iDempiere 13](https://img.shields.io/badge/iDempiere-13-E67E22)](idempiere-13/)

This repository centralizes reusable instructions for AI development assistants. It keeps guidance consistent and separates it by major iDempiere version, reducing the risk of applying assumptions, build settings, or platform-specific instructions to an incompatible codebase.

The catalog covers OSGi plugins, version upgrades, the Application Dictionary, PIPO/2Pack, PostgreSQL, Jenkins, testing, and functional documentation.

## At a glance

| | |
|---|---|
| **Versioned sets** | iDempiere 8, 10, 12, and 13; shared APIs require target-release verification |
| **Catalog** | 15 skills per version + 11 shared skills + 7 core-contribution skills (33 distinct names) |
| **Primary format** | Self-contained `SKILL.md` directories |
| **Installation** | Select one target set and relevant shared/core skills; review existing-name conflicts first |
| **Optional companion** | [`idempiere-dev-environments`](https://github.com/Carl0gonzalez/idempiere-dev-environments) for isolated development environments |
| **Safety baseline** | Version isolation, portable instructions, validation, and read-only database access by default |

## Contents

- [Repository structure](#repository-structure)
- [Organization rules](#organization-rules)
- [Available skills](#available-skills)
- [Meta-skills: creating and reviewing skills](#meta-skills-creating-and-reviewing-skills)
- [Plugin version upgrade workflow](#plugin-version-upgrade-workflow)
- [Shared skills and core contributions](#shared-skills-and-core-contributions)
- [Skill revisions and bilingual wiki](#skill-revisions-and-bilingual-wiki)
- [Version matrix](#version-matrix)
- [Installing from a local clone](#installing-from-a-local-clone)
- [Using isolated environments with direnv](#using-isolated-environments-with-direnv)
- [PostgreSQL safety policy](#postgresql-safety-policy)
- [Contributing and maintenance](#contributing-and-maintenance)
- [License](#license)

## Repository structure

```text
.
├── idempiere-8/                 # Skills for iDempiere 8 repositories
├── idempiere-10/                # Skills for iDempiere 10 repositories
├── idempiere-12/                # Skills for iDempiere 12 repositories
├── idempiere-13/                # Skills for iDempiere 13 repositories
├── shared/                      # Cross-version skills; verify target APIs
├── core/                        # Core contribution adaptations
├── docs/                        # Adoption review and provenance
├── scripts/                     # Read-only catalog validation
├── tests/                       # Local helper behavior checks
├── LICENSE                      # MIT License
├── README.es.md                 # Spanish documentation
└── README.md                    # English catalog and usage guide
```

Each version directory retains its 15 self-contained skill entries. shared/ centralizes cross-version workflows with explicit API checks; core/ centralizes contribution guidance tied to upstream policy. A directory label does not establish compilation or runtime compatibility.

| Directory | Scope | Recommended use |
|---|---|---|
| [`idempiere-8`](idempiere-8/README.md) | iDempiere 8 | Projects, plugins, and target platforms based on v8. |
| [`idempiere-10`](idempiere-10/README.md) | iDempiere 10 | Projects, plugins, and target platforms based on v10. |
| [`idempiere-12`](idempiere-12/README.md) | iDempiere 12 | Projects, plugins, and target platforms based on v12. |
| [`idempiere-13`](idempiere-13/README.md) | iDempiere 13 | Projects, plugins, and target platforms based on v13. |

## Organization rules

Every contribution should follow these rules to keep the catalog clear, reusable, and safe:

| Rule | Requirement |
|---|---|
| **Dedicated directories** | Each skill lives in its own directory and contains a `SKILL.md` file. |
| **Clear metadata** | Frontmatter includes `name` and `description`, describing both the capability and its activation criteria. |
| **Focused scope** | A skill solves one reusable capability rather than grouping unrelated tasks. |
| **Version separation** | Platform-specific skills are placed under each compatible iDempiere version. |
| **Portability** | Skills do not contain personal paths, usernames, credentials, hosts, ports, or assumptions tied to one machine. |
| **Validation** | Every changed skill is validated before it is added to the repository. |
| **No duplication** | Update an existing skill when it already covers the intended purpose. |

### Minimum skill structure

```text
skill-name/
└── SKILL.md
```

A skill may include `scripts/`, `references/`, or `assets/` only when those resources support a repeatable or deterministic workflow.

## Available skills

The following skills are available in each version directory unless a future platform difference requires a specialized variant. Links below point to the iDempiere 12 copies as representative examples.

| Skill | Capability | Primary purpose |
|---|---|---|
| [`idempiere-local-postgres`](idempiere-12/idempiere-local-postgres/SKILL.md) | Safe PostgreSQL diagnostics for iDempiere. | Inspects data, schema, and configuration with read-only sessions by default. |
| [`idempiere-migration-review`](idempiere-12/idempiere-migration-review/SKILL.md) | Reviews migration and module proposals. | Audits models, DDL, the Application Dictionary, and OSGi consistency. |
| [`idempiere-model-designer`](idempiere-12/idempiere-model-designer/SKILL.md) | Designs data models and functional architecture. | Defines entities, relationships, documents, and ERP rules. |
| [`idempiere-pipo-integrity-review`](idempiere-12/idempiere-pipo-integrity-review/SKILL.md) | Runs PackOut/PIPO preflight checks. | Verifies dependencies and compatibility between the dictionary and database. |
| [`idempiere-plugin-compiler`](idempiere-12/idempiere-plugin-compiler/SKILL.md) | Builds OSGi plugins. | Discovers the repository builder and reports generated artifacts. |
| [`idempiere-plugin-version-upgrader`](idempiere-12/idempiere-plugin-version-upgrader/SKILL.md) | Upgrades existing OSGi plugins between iDempiere releases. | Uses a version branch from `master`, aligns Java/PostgreSQL/build compatibility, compiles locally, and gates the PR on review. |
| [`idempiere-plugin-component-developer`](idempiere-12/idempiere-plugin-component-developer/SKILL.md) | Develops internal plugin components. | Implements processes, callouts, validators, and factories. |
| [`idempiere-plugin-designer`](idempiere-12/idempiere-plugin-designer/SKILL.md) | Designs plugin implementations. | Converts functional designs into Java and OSGi specifications. |
| [`idempiere-plugin-manual-generator`](idempiere-12/idempiere-plugin-manual-generator/SKILL.md) | Generates functional manuals. | Produces user documentation and test guides from code and metadata. |
| [`idempiere-plugin-readme`](idempiere-12/idempiere-plugin-readme/SKILL.md) | Documents plugin repositories. | Creates and updates English README files based on the actual project contents. |
| [`idempiere-plugin-wiki-page`](idempiere-12/idempiere-plugin-wiki-page/SKILL.md) | Documents plugins in the iDempiere wiki. | Normalizes Available Plugins pages from README content verified against code and metadata. |
| [`idempiere-plugin-test-developer`](idempiere-12/idempiere-plugin-test-developer/SKILL.md) | Develops plugin tests. | Defines unit tests, mocks, and isolation strategies. |
| [`jenkinsfile-developer`](idempiere-12/jenkinsfile-developer/SKILL.md) | Maintains Jenkins pipelines. | Standardizes version-aware builds and documentation publishing. |
| [`skill-architect`](idempiere-12/skill-architect/SKILL.md) | Designs new skills. | Creates focused capabilities when no suitable skill exists. |
| [`skill-reviewer`](idempiere-12/skill-reviewer/SKILL.md) | Reviews skills before adoption. | Evaluates naming, activation, scope, structure, and duplication risk. |

## Meta-skills: creating and reviewing skills

`skill-architect` and `skill-reviewer` are platform-independent meta-skills that maintain the quality of the catalog itself. They are included in all four version directories so each isolated environment can create or assess capabilities without loading another platform's dependencies.

| Skill | Function | When to use it | Expected result |
|---|---|---|---|
| [`skill-architect`](idempiere-12/skill-architect/SKILL.md) | Designs and structures a reusable skill. | A repeatable workflow is not covered by an existing skill. | A focused name, description, location, structure, and complete `SKILL.md`. |
| [`skill-reviewer`](idempiere-12/skill-reviewer/SKILL.md) | Audits a skill before it is added or changed. | Before committing or installing a skill, or when its scope or overlap is unclear. | A verdict, findings, proposed corrections, and final recommendation. |

### How they work together

```text
Repeatable need
      │
      ▼
skill-architect ──► Does an equivalent skill exist?
      │                         │
      │ no                      └── yes: reuse or update it
      ▼
Design and create a focused skill
      │
      ▼
skill-reviewer ───► Review naming, activation, scope, and structure
      │
      ▼
Apply required corrections or approve for adoption
```

`skill-architect` should not generate a skill for a one-off, ambiguous, or already covered activity. It first checks for overlap, proposes a lowercase hyphenated name, writes a description that explains when the skill activates, and limits supporting files to those the workflow actually needs.

`skill-reviewer` does not change files by default. It first determines whether the skill is specific, reusable, and discoverable by an agent. Its verdict classifies the result as approved, approved with minor changes, revision required, or rejected because of duplication or excessive scope. It rewrites the skill only when explicitly requested.

### Example: create a skill

Use this prompt to turn a repeated procedure into a skill:

```text
I want to create a reusable skill for reviewing SQL migration scripts before execution.

It must detect destructive operations, validate naming conventions, and require a rollback strategy. First review the available skills to avoid duplication. If a new skill is appropriate, propose its name, description, minimum structure, and the complete contents of SKILL.md. Do not add scripts or supporting directories unless they are necessary.
```

The expected result is a proposal such as `sql-migration-safety-review`, with clear activation criteria, safety boundaries, a review workflow, and an output contract.

### Example: review a skill before adoption

Use this prompt to validate an existing skill:

```text
Review the skill located at <skill-path> before adding it to the catalog.

Evaluate its name, frontmatter, activation criteria, scope, duplication risk, instructions, and file structure. Return a verdict, concrete findings, suggested corrections, revised frontmatter when applicable, and a final recommendation. Do not modify files yet.
```

> Recommended workflow: create or update the skill with `skill-architect`, review it with `skill-reviewer`, apply the accepted corrections, and validate the result before committing it.

## Shared skills and core contributions

Select one version set plus the relevant shared skills. Select core skills only for core contributions; the actual core checkout's AGENTS.md and task skills take precedence. Do not install all version copies with the same name together, and do not overwrite installed skills automatically. This catalog update does not install anything.

shared/ contains portable workflows, not a claim that every annotation, mapped service or ZK API exists in every release. If an API is absent, retain the compatible existing mechanism or report the limitation.

| Skill | Purpose |
|---|---|
| [`idempiere-architecture-patterns`](shared/idempiere-architecture-patterns/SKILL.md) | Architecture and core/plugin/environment routing. |
| [`idempiere-plugin-quality-gate`](shared/idempiere-plugin-quality-gate/SKILL.md) | Execution and evidence for plugin tests and quality. |
| [`crear-entornos-idempiere-envrc`](shared/crear-entornos-idempiere-envrc/SKILL.md) | Create/review isolated direnv environments. |
| [`documentar-entornos-idempiere-envrc`](shared/documentar-entornos-idempiere-envrc/SKILL.md) | Document actual environment behavior. |
| [`gestionar-tareas`](shared/gestionar-tareas/SKILL.md) | Manage an existing explicit task registry. |
| [`idempiere-event-annotation`](shared/idempiere-event-annotation/SKILL.md) | Annotation-based model/document/login/facts delegates. |
| [`idempiere-rest-resource`](shared/idempiere-rest-resource/SKILL.md) | REST contracts and ResourceExtension registration. |
| [`idempiere-window-validator`](shared/idempiere-window-validator/SKILL.md) | Window interception with complete callback paths. |
| [`idempiere-zul-form`](shared/idempiere-zul-form/SKILL.md) | ZUL forms, controllers, wiring and resources. |
| [`idempiere-grouped-listbox`](shared/idempiere-grouped-listbox/SKILL.md) | Grouped models, renderers and bounded data loading. |
| [`idempiere-wlistbox-custom-editor`](shared/idempiere-wlistbox-custom-editor/SKILL.md) | Column editor providers and display customization. |

The seven core skills and their execution boundaries are indexed in [core/README.md](core/README.md). See [shared/README.md](shared/README.md), [provenance](docs/SOURCES.md), [installed/custom-skill inventory](docs/INSTALLED_SKILLS_INVENTORY.md) and the [two-pass adoption review](docs/ADOPTION_REVIEW.es.md).

Validation requires Python 3 and PyYAML: `python3 scripts/validate_catalog.py`. The local PR-helper checks run with `python3 tests/test_review_pr.py`; they use temporary Git repositories and no network/database.


## Plugin version upgrade workflow

`idempiere-plugin-version-upgrader` provides a controlled path for moving an existing plugin to another major iDempiere release:

1. Inspect the repository, source release, official target branch, migration notes, Java level, PostgreSQL support, and build system without changing files.
2. Present the compatibility findings, exact files expected to change, branch name, build command, and PostgreSQL validation plan for approval.
3. Create the corresponding version branch, such as `12.0.0`, from the verified `master` base and apply the upgrade only there.
4. Align Maven/Tycho, OSGi, target-platform, Java, JDBC, and SQL code with the target release.
5. Compile every updated plugin, fragment, feature, dependency, and test bundle locally with the target JDK and target platform.
6. Review all SQL/JDBC statically and execute affected paths against a supported local or disposable PostgreSQL instance when database behavior is involved.
7. Present the final diff, build evidence, PostgreSQL evidence, generated artifacts, and remaining limitations.
8. Push the branch and create a PR targeting `master` only after explicit approval of that reviewable result.

A successful Maven/Tycho build verifies Java and OSGi resolution for the compiled paths. PostgreSQL compatibility requires database-backed tests; when no suitable target database is available, the result must be reported as static review only.

## Skill revisions and bilingual wiki

Target iDempiere versions and skill content revisions are different. The catalog has four target sets (8/10/12/13), shared workflows and core-only workflows. No published release or tested runtime status is inferred from a directory name.

- [Versioning and compatibility matrix](docs/VERSIONING.md).
- [Exact revisions of all 78 skill entries](docs/skill-versions.json).
- [English wiki](docs/wiki/Home.md) and [Spanish wiki](docs/wiki/Inicio.md).
- [MediaWiki editions and publication state](docs/wiki/README.md).
- Each version, shared and core README has an English/Spanish language switch.

After an intended skill/resource change, review it and run `python3 scripts/catalog_versions.py --write`. Use `python3 scripts/catalog_versions.py --check` to verify the recorded revisions without writing. This tracks the repository contents, not the installed skill library.

## Version matrix

This matrix shows documented workflow coverage, not tested runtime support. Exact APIs/build requirements are verified in the target project.

| Area | iDempiere 8 | iDempiere 10 | iDempiere 12 | iDempiere 13 |
|---|:---:|:---:|:---:|:---:|
| Modeling, migrations, and PIPO | ✓ | ✓ | ✓ | ✓ |
| Plugin design, development, and testing | ✓ | ✓ | ✓ | ✓ |
| Controlled plugin version upgrades | ✓ | ✓ | ✓ | ✓ |
| Documentation and user manuals | ✓ | ✓ | ✓ | ✓ |
| Safe PostgreSQL diagnostics | ✓ | ✓ | ✓ | ✓ |
| Version-aware Jenkins support | ✓ | ✓ | ✓ | ✓ |
| Builder and target-platform branch | Verify in the target repository | Verify in the target repository | Based on the target repository configuration | Verify in the target repository |

> Never reuse a Docker image or target-platform branch from another major iDempiere version automatically. The Jenkins skill requires discovery and configuration of the builder used by the target project.

## Installing from a local clone

Clone this repository and ask an AI assistant to install the skills from the local version directory. This approach keeps a versioned copy, makes the target iDempiere line explicit, and lets the agent use the installation mechanism supported by its environment.

1. Clone the repository in a location you control.
2. Select one required version directory and relevant `shared/` skills. Add `core/` only for core work; do not load duplicate names from multiple version sets.
3. Copy the prompt below and replace the values inside `<...>`.

```text
I need to install a local set of skills for my AI agent.

Skill source: <local-clone-path>/idempiere-<8|10|12|13>/
Target iDempiere version: <8|10|12|13>

Inspect that directory, identify every skill containing a SKILL.md file, and propose copying or linking them into the skill library used by this environment. Before modifying files, tell me:
1. Which skills you found and the destination path you will use.
2. Whether a skill with the same name already exists and how you will handle the conflict.
3. Whether you will copy files or create symbolic links, including the implications of each option.

Do not overwrite or remove an existing skill without my explicit confirmation. Limit the installation to the specified iDempiere version and confirm which skills are available when finished.
```

The prompt does not assume a specific provider or installation path. It can be used with Codex, ChatGPT, Claude, Gemini, Cursor, Windsurf, or another agent with local filesystem access.

| Benefit | Result |
|---|---|
| No fixed paths | The user chooses where to keep the clone. |
| Controlled selection | Only the version compatible with the project is installed. |
| Safe installation | The agent reports conflicts before overwriting anything. |
| Simple updates | Pull the latest changes and repeat the copy or linking process. |

> Always verify that the selected version matches the iDempiere repository where the skills will be used.

## Using isolated environments with direnv

Use `direnv` to load only the skills for the iDempiere version used by the current repository. This reduces the risk of compiling, designing, or diagnosing a project with assumptions from another major version.

This skills repository was originally designed for projects that keep their iDempiere development environments separate. That design is why every supported major version has its own complete skill set instead of sharing one global set with mixed assumptions.

The companion [`idempiere-dev-environments`](https://github.com/Carl0gonzalez/idempiere-dev-environments) repository can be used to create and maintain those isolated environments. It is optional: these skills can also be installed in any compatible setup, but using both repositories together provides a clear boundary between iDempiere versions and their associated agent instructions.

### Example `.envrc`

Create an `.envrc` in the target repository:

```sh
# Load only the version used by this repository.
export IDEMPIERE_VERSION=12

# Keep the agent state isolated by project.
export CODEX_HOME="$PWD/.codex"

# Define this variable outside the repository or through direnv configuration.
export SKILLS_BACKUP_ROOT="${SKILLS_BACKUP_ROOT:?Set SKILLS_BACKUP_ROOT before allowing this .envrc}"

mkdir -p "$CODEX_HOME/skills"

for skill_dir in "$SKILLS_BACKUP_ROOT/idempiere-$IDEMPIERE_VERSION"/*; do
  [ -f "$skill_dir/SKILL.md" ] || continue
  skill_destination="$CODEX_HOME/skills/$(basename "$skill_dir")"
  if [ -e "$skill_destination" ] || [ -L "$skill_destination" ]; then
    printf 'Existing skill preserved: %s\n' "$skill_destination"
    continue
  fi
  ln -s "$skill_dir" "$skill_destination"
done
```

Then run:

```sh
direnv allow
```

### Isolation benefits

| Benefit | Result |
|---|---|
| Explicit version selection | Each project loads skills that match its platform. |
| Less context contamination | Instructions, builders, and patterns from other versions stay out of the project. |
| Portable configuration | An environment variable supplies the backup location. |
| Reproducibility | Teams can share an `.envrc.example` without publishing personal paths or credentials. |

## PostgreSQL safety policy

The `idempiere-local-postgres` skill applies a conservative data-access policy:

| Control | Behavior |
|---|---|
| Default mode | Every connection starts in read-only mode. |
| Allowed queries | `SELECT`, `SHOW`, and `EXPLAIN`. |
| Write operations | `INSERT`, `UPDATE`, `DELETE`, `MERGE`, DDL, and functions with side effects. |
| First verification | Report the database, target, proposed SQL, and possible impact. |
| Final verification | Request final confirmation for the exact operation before writing. |
| Scope changes | Any change to SQL, filters, destination, or impact restarts both verification steps. |

This policy supports safe diagnosis and reduces the chance of accidental changes to iDempiere databases.

## Contributing and maintenance

Before adding or updating a skill:

1. Confirm that an equivalent skill does not already exist and should be updated instead.
2. Identify every iDempiere version to which the change applies.
3. Keep instructions concise, operational, and free of local information.
4. Validate the frontmatter and directory structure.
5. Check for personal paths, credentials, or machine-specific configuration.
6. Update both README languages, the wiki and `docs/skill-versions.json` when the catalog changes.

For complex changes, use `skill-reviewer` before adopting the skill.

## License

Distributed under the [MIT License](LICENSE).

Copyright © 2026 Carlo González.
