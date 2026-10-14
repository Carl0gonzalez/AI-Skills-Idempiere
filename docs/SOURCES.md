# Sources and attribution

## Existing local catalog and installed custom skills

The versioned catalog and pre-existing changes were retained. Installed architecture, quality-gate, environment-creation, environment-documentation and task-registry skills were copied with their complete resources into shared/. The installed wiki skill's newer contributor convention was synchronized into all four version copies. Generic platform-bundled skills (documents, spreadsheets, OpenAI product guidance, etc.) are outside this iDempiere catalog and were not vendored.

## Component-pattern inspiration

Reference: [hengsin/idempiere-skills at a7ec5db](https://github.com/hengsin/idempiere-skills/tree/a7ec5db8f7459ad67fd0753e0f314ba69021a9cb), local baseline dated 2026-03-07.

The 11 original task areas were evaluated. Process annotation/mapped-process and callout/event-handler patterns were integrated into versioned component guidance; mapped model registration into model guidance. Event delegates, REST, window validation, ZUL forms, grouped listboxes and WListbox editors became six original adapted workflows in shared/.

Descriptions/workflows were authored for this catalog. Upstream assets and unlicensed example files were not copied wholesale or relicensed as MIT. Small API-shape examples here are explanatory and require target-source verification, not compiled upstream templates. Source concepts do not establish compatibility across releases.

## Core contribution policy

Reference: [idempiere/idempiere at 75ad260](https://github.com/idempiere/idempiere/tree/75ad26081a1745ab64831567861ad8f9f6f78d36/.agents/skills), including root AGENTS.md and the seven named skills/resources.

Core entries are original local adaptations of its documented workflow requirements, not verbatim upstream files. The original PR script was not copied: the local implementation uses isolated worktrees and refuses destructive cleanup. No upstream Java/GPL templates were copied into the MIT catalog. Follow upstream source headers/licenses when implementing code in a target core/plugin.

Policy changes incorporated: explicit context routing, exact-release discovery, no unauthorized fork push/publication, verified SyncDB destination/pending impact, tests explicitly enabled, self-contained resources and preserved user work. Upstream rules/documentation from the actual checkout remain authoritative.

## Maintenance

Review upstream changes before updating these adaptations. Keep source commit, adoption decisions and executed checks visible. Do not treat a fetched document, a skill validator or local Git fixture tests as Java compilation, DB compatibility or production readiness.
