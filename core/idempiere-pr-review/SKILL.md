---
name: idempiere-pr-review
description: Review iDempiere core pull requests or local diffs in stages for correctness, generated migrations, compatibility and tests. Use an isolated worktree for authorized local PR testing; do not post findings automatically.
---

# Core PR review

## Scope and authority

Use only for the iDempiere core repository. Read the target checkout's AGENTS.md, matching .agents/skills and PR template first. Their applicable instructions and the project's official documentation govern; this central adaptation is not a replacement for newer local rules. Resolve the exact release, JDK, build and database baseline rather than importing another release's settings. See [the pinned upstream policy](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md).
## Gates

1. **Scope/code:** read ticket, PR body/commits and changed files; check one ticket/purpose, generated migration pairs, transaction ownership, bind parameters, tenant/role access, API compatibility, license/messages and all callers. Use [references/review-checklist.md](references/review-checklist.md). Report blockers before expensive verification.
2. **Build/tests:** only if scope/code allows useful testing, prepare an isolated worktree. The helper below verifies upstream, preserves the current checkout and refuses overwrite. Read its help and inspect the intended destination before running. It performs a local fetch/merge; it does not publish.
3. **Application:** after successful required build/tests, test the ticket and relevant non-happy/collateral scenarios on an authorized test instance. Missing infrastructure is an explicit limitation, not a pass.

```bash
bash <skill-dir>/scripts/review-pr.sh prepare <number> <absolute-new-worktree-path> [upstream]
bash <skill-dir>/scripts/review-pr.sh cleanup <absolute-worktree-path>
```

The prepared worktree contains upstream/master plus the PR merge to model integration. The local synthetic merge is review-only; never push it as a contribution commit. The helper records reviewed revisions; it never runs SyncDB/build/server automatically. Before SyncDB, inspect ALL pending migrations and verify destination/impact under the database/build skills.

Run a clean build with requested tests explicitly enabled. Attribute failures to the PR only after checking the relevant base when needed. Do not continue to application testing on a failed required build/test gate.

## Cleanup and reporting

The helper refuses cleanup of dirty worktrees, untracked files or additional commits; preserve useful work explicitly. It has no force-delete mode and never switches the original checkout. It does not revert database migrations or stop a server. Do not manually delete a directory to bypass refusal.

Return ticket/PR/base/head, files, severity-ranked findings with file:line and concrete failure scenario, suggested corrections, commands/tests/DB engines checked, and untested paths. Drafting findings does not authorize GitHub/Jira comments. Intentional breaking changes remain a finding for maintainers even when declared.
