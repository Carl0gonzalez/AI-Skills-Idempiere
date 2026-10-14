# Calibration scenarios

These examples calibrate decisions; they are not templates to copy blindly.

## A. Recalculate a field after another field changes

If the behavior is interactive only, use the existing Callout registration mechanism and update the dependent field. Keep the rule local; do not introduce Service, Interface, Factory, or DTO. If the calculation must also hold for REST/import/process execution, place the reusable rule in the smallest domain/helper unit and call it from the Callout and non-UI entry points.

## B. Create a related record whenever an invoice completes

Use an EventHandler/model validator on the appropriate document-completion event so REST, UI, import, and process execution behave consistently. Check duplicate events, reversals, recursion, and the owning transaction. Extract a Service only when the creation rules are substantial, reused, or need meaningful isolation.

## C. Replicate an invoice to another iDempiere

An explicit process may orchestrate selection/request while a reusable replication service owns business orchestration and a remote client/REST adapter owns protocol. Define idempotency, correlation, bounded retry, secret handling, local transaction boundaries, and durable Outbox only if delivery must survive commits/restarts. Do not hold a database transaction open across remote calls without a deliberate reason.

## D. Add and display a new field

Start with Application Dictionary, schema/PackOut portability, reference, field placement, display/validation logic, and generated-model source. Add Java only if executable behavior remains. Do not create a custom model merely to expose a column already handled by generated PO classes.

## E. Correct a condition in an existing process

Patch the condition and add a regression test using the existing test fragment. Preserve packages, public APIs, factories, process registration, and unrelated behavior. Refactor only the smallest testability seam if the defect cannot be covered otherwise.

## Expected review behavior

For each scenario, explain the chosen mechanism, rejected unnecessary layers, relevant version/scaffold evidence, transaction or lifecycle concerns, and validation boundary. A different solution is valid when the inspected project proves a different convention or constraint.
