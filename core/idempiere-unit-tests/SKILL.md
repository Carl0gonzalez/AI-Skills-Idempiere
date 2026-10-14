---
name: idempiere-unit-tests
description: Write or run tests in the iDempiere core org.idempiere.test bundle using its declared framework, GardenWorld fixtures and transaction lifecycle. Use for core regression tests, not arbitrary plugin test projects.
---

# Core tests

## Scope and authority

Use only for the iDempiere core repository. Read the target checkout's AGENTS.md, matching .agents/skills and PR template first. Their applicable instructions and the project's official documentation govern; this central adaptation is not a replacement for newer local rules. Resolve the exact release, JDK, build and database baseline rather than importing another release's settings. See [the pinned upstream policy](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/AGENTS.md).
## Design

- Inspect org.idempiere.test, AbstractTestCase, DictionaryIDs, target dependencies and nearby tests before selecting a test base or mocking API.
- Test observable business behavior; for bug fixes reproduce the failure before the correction when feasible. UI-only work may need manual scenarios instead of contrived unit tests.
- Extend the existing core base where framework/database behavior is essential. Its GardenWorld context and per-test transaction are target-version facts to verify. Pass getTrxName() everywhere and verify rollback/cleanup.
- Use existing DictionaryIDs constants. For missing fixture constants, look up real existing ID/UUID values read-only; do not invent them.
- Do not update shared seed products, client info, SysConfig or conversion rates to prepare a scenario. Prefer own transactional rows or scoped mocks supported by the existing dependencies. Restore mocks and any committed data.
- Fix dates and ordering explicitly. Avoid reliance on test sequence or unbounded data queries. Assert specific values/statuses and meaningful errors.
- Exercise document completion/void through target-version workflow/engine APIs; inspect returned ProcessInfo errors and reload the PO in its transaction before assertions.
- Prefer adding cases to the existing subject test. New files use the target GPLv2 header. Do not refactor public APIs just to accommodate mocks.

## Execution

Inspect the target POM first. In the pinned core reference tests are skipped by default:

```bash
./mvnw verify -DskipTests=false -Dtest=SubjectTest
./mvnw verify -DskipTests=false -Dtest='SubjectTest#regressionMethod'
./mvnw verify -DskipTests=false
```

Replace illustrative test names with actual ones. Confirm a compatible migrated test DB and configuration without printing credentials. Core SyncDB writes require verified destination/impact and authorization. Run the focused test while iterating, then the required suite or report it unexecuted. Check new Surefire reports, executed counts and exit status; stale reports and zero executed tests are not a pass.

## Output

Return cases, fixtures/isolation, exact commands, executed counts/results and limitations. Separate compile-only, focused suite, full suite, PostgreSQL and Oracle results; establish baseline failures where relevant.
