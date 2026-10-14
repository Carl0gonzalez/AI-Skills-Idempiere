---
name: idempiere-event-annotation
description: Create or modify annotation-based iDempiere event delegates and managers when the target release supports them. Use for model, document, login or facts events; preserve the existing bundle registration.
---

# Annotation-based events

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Select the actual event: PO persistence, document action, login or facts validation. Verify topic, base class and delegate signature from target-version core; do not infer signatures from an event name.
2. Reuse the bundle's AnnotationBasedEventManager when present. Add only the delegate package to its scan; create one manager only if this registration pattern is supported and none exists.
3. Implement a focused delegate using EventTopicDelegate and the relevant ModelEventTopic/annotation. ModelEventDelegate, AfterLoginEventDelegate and FactsValidateDelegate are possible bases, subject to release verification.
4. Preserve the event's transaction/context. No hidden commits, null-transaction mixing or state shared through static mutable fields. Per-event instances do not make external caches or services automatically thread-safe.
5. Register only the topics the requirement needs. Check recursion, duplicate execution, ordering and repeated document actions. Business invariants that apply to all entry points must not live only in UI.
6. Test the triggering and non-triggering topics, failure/veto behavior where supported, rollback and duplicate handling. Confirm package scanning and DS activation separately.

See [references/event-selection.md](references/event-selection.md) when choosing a delegate.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
