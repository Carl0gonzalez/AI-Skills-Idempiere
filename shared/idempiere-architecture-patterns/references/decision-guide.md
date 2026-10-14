# Decision guide

Use this reference when the correct entry point, abstraction, or iDempiere mechanism is not obvious.

## Before Java

Check whether Application Dictionary can express the behavior through columns, fields, references, validation rules, display/read-only/mandatory logic, processes, workflows, callouts, parameters, SysConfig, preferences, or role/data access. Choose Java only when metadata is insufficient or the behavior belongs in executable domain logic.

## Entry point map

| Need | First candidate | Key boundary |
|---|---|---|
| Interactive default/recalculation | Callout | Do not make it the only enforcement of a critical rule. |
| Invariant natural to a record | Existing/custom `M*` | Do not edit generated `X_*`. |
| Rule independent of UI/REST/import | EventHandler/model validator | Check recursion, order, double execution, and transaction scope. |
| Explicit user/batch operation | `SvrProcess` | Keep `prepare()` for parameters and `doIt()` as a focused orchestrator. |
| Shared non-trivial rules | Service | Justify with reuse, complexity, orchestration, or testability. |
| Multiple real implementations | Interface/Strategy | One hypothetical future implementation is insufficient. |
| External protocol/system | Adapter/Port | Keep transport mapping outside domain logic. |
| Lookup/persistence | PO/`Query`/core API | Use SQL only for a measured or expressiveness reason. |

When Callout, Process, Event, and REST share a rule, centralize the rule once. Do not create a Service merely because two classes exist; extract the smallest reusable unit that represents the shared behavior.

## Abstraction test

Before adding a layer, answer:

1. Does it remove observed duplication across entry points?
2. Does it isolate non-trivial logic for testing?
3. Does it isolate a real external dependency?
4. Does it represent an extension point or multiple implementations that exist now?
5. Does it fix harmful coupling?
6. Is it already the project's established pattern?

If every answer is no, keep the logic in the appropriate existing component.

## Version and OSGi compatibility

- Confirm APIs in the exact release source or target platform; do not backport a modern example by assumption.
- Confirm Java execution environment and compiler level before using language/JDK APIs.
- A Maven dependency does not automatically make a package visible to OSGi. Check `Require-Bundle`, `Import-Package`, exports, feature/P2 membership, and runtime bundle availability.
- Preserve the registration mechanism already packaged by the bundle. A scaffold-provided factory is an extension point to reuse, not a reason to create a second factory package.
- Before renaming or moving classes/packages/services/bundle IDs, search consumers, fragments, features, AD class names, Jenkins, migrations, and PackOut/PackIn artifacts.

## Transactions and documents

For one atomic unit, propagate the same `trxName` through entry point, service, models, and queries. Create a separate transaction only for a clear boundary such as durable Outbox/Inbox reservation, and define what survives each failure.

For documents, identify the valid action and lifecycle state. Use document processing APIs and resulting generated documents. Direct status changes are not a substitute for lifecycle execution.

## External integrations

Introduce only the reliability mechanisms demanded by failure modes:

- idempotency key when retries can duplicate effects;
- correlation ID when work crosses systems or asynchronous boundaries;
- bounded retry/backoff for transient failures;
- durable state when process restarts must not lose work;
- locking/claiming when parallel workers can select the same work;
- Outbox when a local commit must reliably lead to later delivery.

State the consistency boundary and the recovery path. Do not claim distributed atomicity where none exists.
