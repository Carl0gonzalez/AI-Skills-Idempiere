# Implementation and review checklist

Use proportionally; do not turn a one-line bug fix into a ceremony.

## Context and compatibility

- Core versus private plugin established; actual repository policies read.
- Core migration/AD work is developer-generated, not authored by the agent.
- Callers of changed public/protected APIs and collateral scenarios reviewed.
- User-visible messages translated; role access reviewed as well as tenant/org filters.
- Supported database engines stated and tested/unverified evidence separated.

## Baseline

- Exact iDempiere and Java versions established.
- Maven/Tycho/target platform and actual build command identified.
- Affected bundles, fragments, features, AD/PackIn and working-tree state inspected.
- Scaffold, customs/overlays, generated sources, and recent similar plugins checked.

## Design

- Requirement classified as simple, medium, or complex.
- AD/configuration considered before Java.
- Existing model/API/factory/extension point reused where appropriate.
- Every new abstraction has a present justification.
- Entry point matches the behavior: UX, invariant, cross-entry reaction, explicit process, transport, or trigger.
- Change set is minimal and unrelated refactors are excluded.

## Domain and persistence

- Generated `I_*`/`X_*` sources are untouched or regenerated from their source.
- Document lifecycle is respected; no manual completion/status bypass.
- Transaction ownership and `trxName` propagation are explicit.
- Queries bind parameters; SQL is justified and scoped.
- Client/org isolation and configurable values are not hardcoded.
- PackOut/PackIn portability does not rely on accidental database IDs.

## Runtime architecture

- OSGi imports/bundles/services and registration mechanism match the actual project.
- Existing scaffold factories and test fragments are reused, not duplicated.
- Recursion, double execution, concurrency, idempotency, and retry behavior are addressed where relevant.
- No global mutable state or manual singleton/registry without a concrete need.
- External calls do not leak into UI/domain layers or unsafe transaction loops.

## Quality

- Happy path, regression, validation failures, boundaries, and relevant concurrency/idempotency cases are covered.
- Obvious N+1, unbounded scans, looped queries/calls, and excessive logs checked.
- Exceptions preserve causes; no silent catches, `System.out`, or sensitive logs.
- Scaffold placeholders such as `${...}`, `{{...}}`, `__NAME__`, `PLUGIN_ID`, `PACKAGE_NAME`, example URLs, and temporary IDs are absent.
- Bundle ID, artifact/group/version, packages, feature references, fragment host, and repository references are consistent.
- Real build and tests executed, or explicitly marked unavailable.

## Final simplification pass

- Could any new layer or file be removed without losing correctness, reuse, testability, or isolation?
- Is there an iDempiere API or existing component that makes custom code unnecessary?
- Does the result modify more files than the requirement needs?
- Are deployment, database, OSGi activation, PackIn, and UAT claims limited to actual evidence?
