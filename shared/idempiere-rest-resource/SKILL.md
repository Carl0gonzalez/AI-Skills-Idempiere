---
name: idempiere-rest-resource
description: Create or modify custom iDempiere REST endpoints using ResourceExtension and the REST plugin installed in the target project. Use for transport contracts and endpoint registration, not for replacing existing integration orchestration.
---

# REST resource extensions

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Discover the installed REST bundle/version, ApplicationV1 conventions, JAX-RS namespace (javax or jakarta), ResourceExtension interface and existing route prefixes. REST is an external plugin dependency, not an assumed core API.
2. Define method/path, authentication, role/client/org access, request fields, success/error schema and transaction ownership. Define idempotency for repeated writes when needed.
3. Reuse an existing ResourceExtension service and add the resource class to getResourceClasses(). Create a service only if the bundle has none. Preserve dispatcher, handlers, mappings and Outbox in existing integrations.
4. Use the installed REST model/security APIs where appropriate. Do not expose arbitrary records through direct SQL that bypasses role access. Bind values and validate input; do not reveal secrets or cross-tenant data.
5. Implement the actual response mapping. An empty ObjectNode with a success status is not a completed endpoint unless the contract explicitly requires an empty object. Preserve failure statuses and causes without leaking internals.
6. Validate dependency metadata, DS packaging, service activation and registration. Diagnose route 404 separately from auth 401/403; a RESOLVED bundle is not proof of an ACTIVE component.
7. Test authorized/unauthorized access, absent records, another client's records, malformed input, serialization and the operation's failure path. Verify retries/rollback for writes when applicable.

See [references/resource-registration.md](references/resource-registration.md) for the minimal registration shape.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
