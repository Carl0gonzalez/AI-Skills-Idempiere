---
name: idempiere-window-validator
description: Implement iDempiere ZK WindowValidator services for window-level process or document-action interception, when supported by the target release. Use for UI confirmation and validation, not as the sole enforcement of cross-entry business invariants.
---

# Window validation

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Identify the actual window UUID and event with read-only AD evidence; do not invent IDs/UUIDs. Use exports or database inspection if a window-list connector is unavailable.
2. Verify WindowValidator, WindowValidatorEvent, event names/data types and callback contract in target-version core.
3. Reuse existing validators or register a focused service through the bundle's proven DS mechanism, scoped by AD_Window_UU and events. Do not conflate WindowValidator with IModelValidator.
4. Complete the callback exactly once on every path, including unsupported events, rejection, exceptions and asynchronous dialog results. Avoid a default callback after dispatching an asynchronous confirmation.
5. Use translated messages. Keep shared business invariants in a model/event or reusable domain component so REST, imports and batch processes cannot bypass them.
6. Test acceptance, rejection, user cancellation and errors. Confirm unrelated windows/events are unaffected and the UI does not remain waiting for a callback.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
