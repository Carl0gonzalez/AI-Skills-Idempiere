# Core contribution skills

**English** | [Español](README.es.md)

Seven workflows for contributions to iDempiere core. Read the target checkout's AGENTS.md, local skills and official documentation first. Core contribution policies do not automatically apply to private plugins.

| Skill | Purpose |
|---|---|
| [idempiere-contribution-workflow](idempiere-contribution-workflow/SKILL.md) | Prepare Jira-linked branches, focused commits, documentation and PRs. |
| [idempiere-core-coding-standards](idempiere-core-coding-standards/SKILL.md) | Preserve transactions, role access, API compatibility and dual-database behavior. |
| [idempiere-database-changes](idempiere-database-changes/SKILL.md) | Specify UI changes and review developer-generated Centralized-ID migrations. |
| [idempiere-unit-tests](idempiere-unit-tests/SKILL.md) | Write/run core regression tests using declared GardenWorld fixtures. |
| [idempiere-headless-build-run](idempiere-headless-build-run/SKILL.md) | Build core and handle authorized SyncDB/server operations with exact evidence. |
| [idempiere-pr-review](idempiere-pr-review/SKILL.md) | Review in gates and test integration in an isolated worktree. |
| [idempiere-jira-tickets](idempiere-jira-tickets/SKILL.md) | Draft reproducible bug/feature reports and private security reports. |

## PR review helper

The PR-review skill includes an isolated-worktree helper. It preserves the original checkout and refuses cleanup when the review worktree contains additional work. Requirements: Git 2.31+, Bash 3.2+ and a configured local Git identity; Windows uses Git Bash. Read the skill before running the helper. See [core policy](CORE_POLICY.md).


See the [repository catalog](../README.md) and [version selection](../docs/VERSIONING.md).
