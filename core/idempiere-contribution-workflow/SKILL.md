---
name: idempiere-contribution-workflow
description: Plan and prepare Jira-linked branches, commits and pull requests for the iDempiere core repository. Use for core contributions and review feedback, not private-plugin release workflows.
---

# Core contributions

## Scope and authority

Use only for the iDempiere core repository. Read the target checkout's AGENTS.md, matching .agents/skills and PR template first. Their applicable instructions and the project's official documentation govern; this central adaptation is not a replacement for newer local rules. Resolve the exact release, JDK, build and database baseline rather than importing another release's settings. See [the pinned upstream policy](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md).
## Workflow

1. Confirm the real IDEMPIERE ticket. Do not invent one; draft missing ticket text with the Jira skill while continuing independent diagnosis. A ticket is required before contribution coding/commits under the target rules.
2. Inspect worktree status, branches and remotes without printing credential-bearing URLs. Identify fork/upstream by evidence, not by name alone. Preserve untracked work and existing checkouts; prefer an isolated worktree for independent work.
3. Fetch upstream only when needed. Sync local master by fast-forward only if authorized and clean; divergence requires diagnosis. Never commit to master. Fetching/local synchronization does not authorize pushing the fork's master.
4. Work on IDEMPIERE-<real-ticket>-<short-description>. One ticket per PR. Inspect an existing branch before reusing it; never overwrite it or stash user work automatically.
5. If AD/schema changes are needed, follow the database skill: specification, human UI generation with Centralized IDs, review and model regeneration. Do not author core migrations.
6. Make focused changes with separate refactoring/fix commits when committing is authorized. Every commit references the ticket. Stage exact files; inspect staged diff for unrelated work, IDE/build outputs and secrets.
7. Self-review with the PR review skill. Record build, explicitly enabled tests, PostgreSQL/Oracle evidence, callers and manual scenarios. A successful verify with skipped tests is a build result only.
8. Prepare a PR body using the target template: Jira link first, problem/behavior, reproduction, impact, test commands/results, unavailable checks, collateral scenarios and generated metadata. Documentation for features, breaking changes and user-visible behavior belongs in the project docs repo under its own instructions; link the docs PR when applicable.
9. Commit, push, PR creation and comments are distinct external/persistent actions. Perform only what the user authorized; show the concrete diff/body before a remaining approval. Never force-push or rewrite published history without explicit direction.
10. Evaluate reviewer feedback on its merits and prepare corrections on the same ticket branch. Do not send public replies without authorization.

## Output

Report ticket, repository, base/branch, scoped changes, validation, prepared commit/PR text, documentation requirements and actual publication state. Do not report a draft as posted.
