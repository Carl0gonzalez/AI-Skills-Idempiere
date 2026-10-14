# Core contribution guidance

**English** | [Español](README.es.md)

The **seven core workflows** are local adaptations of upstream commit 75ad26081a1745ab64831567861ad8f9f6f78d36. Read the actual core AGENTS.md, matching skills and official documentation first. They do not impose core Jira/ID/migration policies on this library or on private plugins.

| Skill | Purpose |
|---|---|
| [idempiere-contribution-workflow](idempiere-contribution-workflow/SKILL.md) | Prepare Jira-linked branches, focused commits, documentation and PRs. |
| [idempiere-core-coding-standards](idempiere-core-coding-standards/SKILL.md) | Preserve transactions, role access, API compatibility and dual-database behavior. |
| [idempiere-database-changes](idempiere-database-changes/SKILL.md) | Specify UI changes and review developer-generated Centralized-ID migrations. |
| [idempiere-unit-tests](idempiere-unit-tests/SKILL.md) | Write/run core regression tests using declared GardenWorld fixtures. |
| [idempiere-headless-build-run](idempiere-headless-build-run/SKILL.md) | Build core and handle authorized SyncDB/server operations with exact evidence. |
| [idempiere-pr-review](idempiere-pr-review/SKILL.md) | Review in gates and test integration in an isolated worktree. |
| [idempiere-jira-tickets](idempiere-jira-tickets/SKILL.md) | Draft reproducible bug/feature reports and private security reports. |

## Execution boundaries

Core migration scripts, AD IDs/UUIDs and regenerated models are produced by the developer under upstream rules. Agents specify and review them. Commits, pushing, PR/ticket publication, SyncDB and server execution are separate actions governed by the user's authorization.

## Local PR helper

The helper uses an isolated detached worktree, checks the effective official upstream URL and preserves the original checkout. It refuses cleanup with tracked/untracked/ignored work or changed HEAD and has no force-delete mode. It does not revert DB migrations or stop servers.

Requirements: Git 2.31+ (worktrees/--path-format), Bash 3.2+, local identity for the synthetic unpublished review merge. Windows uses Git Bash. Tests use temporary local fixture transport; no live GitHub PR is claimed tested.

```bash
python3 tests/test_review_pr.py
```

Read [policy](CORE_POLICY.md) and the PR-review skill before preparing a worktree.

## Revisions and references

See [versioning](../docs/VERSIONING.md), [sources](../docs/SOURCES.md), [adoption review](../docs/ADOPTION_REVIEW.es.md) and the [wiki](../docs/wiki/Home.md). These instructions do not install skills or publish pages to a remote wiki.
