---
name: idempiere-jira-tickets
description: Draft iDempiere core bug reports and feature proposals with reproducible evidence and decide core versus plugin scope. Use for ticket preparation or suspected vulnerabilities; never invent IDs or publish automatically.
---

# Core Jira drafts

## Scope and authority

Use only for the iDempiere core repository. Read the target checkout's AGENTS.md, matching .agents/skills and PR template first. Their applicable instructions and the project's official documentation govern; this central adaptation is not a replacement for newer local rules. Resolve the exact release, JDK, build and database baseline rather than importing another release's settings. See [the pinned upstream policy](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md).
## Workflow

1. Identify version/build, OS, database/JDK and reproducibility. Prefer current supported/relevant core and GardenWorld reproduction; report unavailable environments honestly.
2. Search existing tickets when access is available, or give the developer precise search terms. Follow current project rules for an equivalent closed ticket; do not invent a ticket number.
3. For bugs, write a searchable condition-specific summary, ordered steps with actual values, explicit expected/actual behavior, frequency, regression version and sanitized logs/screenshots/performance measurements.
4. For enhancements, explain the problem first, proposed behavior with examples, community benefit, affected areas, compatibility/migration/training and alternatives. Check project direction/forum feedback where relevant; company-specific needs may belong in a plugin.
5. Draft only. Publication/comments require user authorization and must also respect the target core rule assigning ticket submission to the developer. Continue contribution workflow after a real ticket exists.

## Suspected vulnerabilities

Do not disclose reproduction/exploit details in a public ticket, PR or commit. Verify the current official private reporting channel in project documentation; the pinned reference names security at idempiere dot com. Help prepare a private report with version, reproduction, impact and disclosure coordination. Drafting a private report does not authorize sending it.

## Output

Return a paste-ready ticket/private-report draft, evidence and missing details, core/plugin rationale, duplicates searched and draft/publication state. Never claim delivery without evidence.
