---
name: idempiere-plugin-test-developer
description: Write regression tests and fixtures for iDempiere plugin components using the existing test project and declared framework. Use for test implementation and isolation; use the quality gate for broader execution and reporting.
---

# Plugin regression tests

Inspect the test fragment/project, target release, framework, dependencies and nearby cases. Do not assume JUnit 5 or Mockito exists; do not add dependencies or create another reactor just to fit a template.

## Select the test level

- Pure rules: use the declared unit framework and narrow mocks if needed.
- Framework/domain lifecycle: use the existing iDempiere test base and real APIs when meaningful.
- SQL, locking or persistence semantics: database-backed tests are needed; mocks cannot prove these paths.
- UI-only behavior: define manual scenarios unless a real UI test harness exists.

For core contributions, read its unit-test/database skills. Verify AbstractTestCase/GardenWorld/DictionaryIDs in that release; look up real fixture IDs read-only and never invent them or generate migrations.

## Fixtures and isolation

Create own records in the test transaction and pass its trxName throughout. Do not change shared seed products, conversion rates, client settings or SysConfig. Scoped static mocks are appropriate only when the declared dependencies support them; close them and restore state. Do not use generic reflection to mutate global static fields.

Fix dates and ordering. Avoid implicit dependence on current date, test order or random existing rows. Commit only when behavior truly requires committed data, and then provide cleanup and authorization for the isolated test DB.

Extract a small pure helper only if it improves actual coupling and preserves API/behavior. Do not create service/interface layers solely for mocking. Use real workflow/engine actions for document tests where relevant.

## Assertions and execution

Assert observable behavior, specific errors/statuses and affected records. SvrProcess may capture exceptions into ProcessInfo; inspect the target startProcess result and ProcessInfo error/summary rather than assuming assertThrows proves failure. Check that the regression fails before and passes after the fix when feasible.

Run the documented builder with tests explicitly enabled and inspect fresh reports/counts. In the referenced core verify skips tests by default; use -DskipTests=false. Run focused cases while iterating and the required wider suite, or state it was not run. Keep compilation, test execution, supported DB engines and runtime activation distinct.

## Output

Return test paths, cases and fixtures, minimal refactor if required, exact commands, executed counts/results, cleanup evidence and limitations. No test pass without execution; no database compatibility claim from mocks alone.
