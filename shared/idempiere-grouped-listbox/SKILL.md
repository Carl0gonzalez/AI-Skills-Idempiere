---
name: idempiere-grouped-listbox
description: Implement grouped ZK Listbox models and renderers in an existing iDempiere form. Use for group headers, rows and footers; verify the target ZK and iDempiere APIs and reuse existing form registration.
---

# Grouped listboxes

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Define record, header and footer types, group key, sort order, aggregation and selection semantics. Reuse the containing form; use a form-creation skill only if a new form is required.
2. Verify SimpleGroupsModel generic arity/constructors and AbstractGroupListitemRenderer signatures in the target ZK/core. Do not assume APIs from another release.
3. Align group data, headers and optional footers by index. Implement render methods with the correct number/spans of columns; distinguish a real ZK Listbox from WListbox.
4. Fetch tenant/role-filtered data using existing model/Query APIs. Limit result volume; use the target-supported paging/lazy-load strategy for large datasets and avoid N+1 queries in renderers.
5. Compute totals with the appropriate decimal precision. Rendering must not mutate or save business records. Render text safely rather than concatenating untrusted HTML.
6. Test empty data, one/many groups, absent footer, sorting, collapsed groups, selection and repeated refresh. Check header/footer totals and layout independently.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
