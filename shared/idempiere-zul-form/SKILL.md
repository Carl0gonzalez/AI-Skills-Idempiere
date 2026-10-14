---
name: idempiere-zul-form
description: Create or modify iDempiere ZK forms using CustomForm, IFormController, ZUL resources and component wiring. Verify the target release and existing form registration before choosing a mapped or annotation-based factory.
---

# ZUL forms

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Decide whether the task needs a custom form or can use AD configuration. Separate visual structure/wiring from controller behavior without creating unnecessary layers.
2. Select the existing IFormFactory, AnnotationBasedFormFactory or IMappedFormFactory pattern after verifying its availability. A form must not be registered by multiple mechanisms.
3. Create a minimal CustomForm/ADForm and IFormController as required by the selected pattern. Constructors must match the final class names; replace all example names consistently.
4. Store only required ZUL resources in the bundle's proven classpath location and include them in build.properties. With Executions.createComponents, verify the ~./ resource path and restore the thread context classloader in finally after switching it.
5. Wire components after creating the view. Register @Listen handlers once and verify nested ID spaces. Translate labels and messages with target-version APIs.
6. Preserve client/org/role filtering, owning trxName and document lifecycle in controller actions. Release listeners/resources when the form closes. Consider paging and background execution for substantial data loads.
7. Test open, action, cancellation, error and close/reopen paths, missing resources and narrow/wide layouts. Verify AD_Form/menu/role requirements separately from code registration.

Read [references/minimal-form.md](references/minimal-form.md) for wiring and naming checks. Large business forms are examples to inspect, not templates to copy wholesale.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
