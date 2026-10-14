---
name: idempiere-plugin-component-developer
description: Implement processes, callouts, validators and factories in an existing iDempiere plugin, preserving target-version APIs, transaction ownership and OSGi registration. Use for component code, not new plugin scaffolds.
---

# Plugin components

Inspect the actual release, source/dependencies, scaffold, AD metadata, MANIFEST.MF, build.properties and registration before writing code. Keep working behavior and use the smallest mechanism that meets the requirement.

## Context and boundaries

- For core contributions, read the actual core AGENTS.md and matching skills. Do not author core migration scripts, DDL, AD IDs/UUIDs or generated models. Specify UI work and review human-generated artifacts. For private plugins use their Entity Type/export policy instead.
- Preserve existing project layout and unrelated work. Necessary registration/build changes are part of an authorized implementation when required; avoid unrelated scaffold changes. Report required metadata that remains outside the authorized scope.
- Prefer existing M* APIs, then Query, DB helpers and finally JDBC with closed resources. Bind values and preserve role/client/org access.
- Pass the owning trxName; never commit/rollback someone else's transaction or mix null into an active operation. Use real document engine/workflow actions, not direct completed-status updates.
- Preserve public/protected APIs, translate user-facing messages, use compatible exceptions/logging and follow target license/header conventions. Never edit generated I_*/X_* sources.

## Select one registration mechanism

Read [references/registration-patterns.md](references/registration-patterns.md) for concrete patterns and required checks.

- **Process:** existing IProcessFactory, AnnotationBasedProcessFactory or IMappedProcessFactory scan, according to actual support. SvrProcess owns prepare/doIt; @Parameter injection must match real AD parameters and supported types.
- **Callout:** preserve an existing CalloutEngine registration or IColumnCallout factory. AnnotationBasedColumnCalloutFactory/@Callout are alternatives only where supported. UI callouts alone cannot enforce invariants on REST/import/batch entry points.
- **Events:** use existing AbstractEventHandler/DS topics or annotation manager/delegates. Verify timing, veto/error behavior, recursion and duplicate execution. Do not introduce a generic IEventFactory without an actual target API.
- **Models:** use existing IModelFactory or verified IMappedModelFactory scanning. Reuse an activator/factory; an Incremental2PackActivator is not mandatory merely to scan classes.

## Implement and verify

1. Verify table/column/model names through read-only AD, metadata or resolved target source; no IDE/connector-specific requirement.
2. Implement the focused rule using target-compatible signatures. Reuse an existing factory and add only necessary scan packages or mappings; never register the same class twice.
3. Package DS XML/annotation output, imports and resources under the proven build convention. An annotation in source does not prove a service is packaged or activated.
4. Add focused regression tests where useful; preserve dates/fixtures/transaction isolation. Compile through the project's actual builder and verify required tests were enabled and executed.
5. Check callers and affected document types, tenant/org boundaries, currencies and accounting schemas. Validate SQL on each supported database; core requires PostgreSQL and Oracle. Report unavailable engines separately.

## Output

Return paths and scoped implementation, chosen registration and release evidence, AD requirements, commands/results and remaining runtime checks. Separate source, build, OSGi activation, PackIn and functional execution. Do not claim deployment or publication from compilation.
