---
name: idempiere-headless-build-run
description: Build, synchronize a confirmed development database or run the iDempiere core server from the terminal using the target checkout configuration. Not a replacement for a plugin-specific builder or environment setup skill.
---

# Core build and run

## Scope and authority

Use only for the iDempiere core repository. Read the target checkout's AGENTS.md, matching .agents/skills and PR template first. Their applicable instructions and the project's official documentation govern; this central adaptation is not a replacement for newer local rules. Resolve the exact release, JDK, build and database baseline rather than importing another release's settings. See [the pinned upstream policy](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md).
## Build

1. Verify JDK and Maven Wrapper from the target release/POM, plus target-platform requirements. The reference commit uses Java 17; do not hard-code it for every release.
2. Use the repository wrapper and reactor from its documented root. A full build verifies cross-bundle compilation; a targeted build must be supported by the actual Tycho workflow.
3. `./mvnw verify` may skip tests. Enable requested tests with `-DskipTests=false` and inspect executed reports/counts.
4. After switching reviewed revisions, clean derived build outputs in the isolated review workspace before verifying. Do not delete unrelated artifacts/work or change repository URLs to hide network failures.
5. Classify failures: compilation, JDK, OSGi/target resolution, network, database, fixture or test. Do not weaken dependency checks to obtain BUILD SUCCESS.

## SyncDB

RUN_SyncDBDev.sh applies all pending migration scripts, not necessarily only the current ticket. Before executing: verify host, port, instance/database and development/disposable status; list the pending scripts through read-only evidence; show impact and obtain authorization if absent. Never print idempiere.properties/idempiereEnv.properties, passwords or connection URLs. If safe inspection cannot establish the destination, ask for non-secret details.

Follow the database skill for script generation/review. Inspect script help and target behavior; run only against the authorized destination. Record errors/log locations and re-query migration state. Branch/worktree cleanup does not roll back a migrated database.

## Server

Find the product actually produced for the current OS/architecture rather than assuming a fixed Eclipse.app path. Use its setup/server scripts with authorized configuration. Respect an existing Eclipse/server instance, ports and JVM. Starting a server requires authorization for that runtime action; track its process and stop only the instance started for the task when appropriate. Do not expose debug ports by default.

## Output

Report release/JDK/wrapper, build command and artifacts, executed/skipped tests, SyncDB target/pending/applied state, server process/ports/logs and actual UI verification. Build success is not runtime readiness.
