# Core policy and source precedence

This directory centralizes adapted guidance for iDempiere core contributions. It is not an AGENTS.md for this skills-library repository and does not impose core restrictions on private plugins.

Read the actual core checkout's AGENTS.md and .agents/skills first. The core documentation is its human-facing authority. Resolve conflicts with those sources and the user's authorized scope; do not infer authorization to publish, mutate a DB or start a server from a workflow example.

Core invariants: Jira-linked ticket branch/commits; never commit to master; focused diffs; PostgreSQL and Oracle; no handwritten migration/DDL/AD IDs or generated models; public/protected API compatibility; English code and target GPLv2 headers; translated messages; honest testing; no credentials in output.

Reference baseline: [AGENTS.md at 75ad260](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md). [Core contribution documentation](https://docs.idempiere.org/docs/basic-development/contributing-to-core/contributing-to-idempiere).

Centralized-ID/UI generation restrictions apply to core. For a private plugin, discover its Entity Type, export/migration policy and supported databases. Avoid inventing database facts in either context.
