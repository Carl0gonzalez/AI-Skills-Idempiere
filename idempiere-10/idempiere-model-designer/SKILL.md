---
name: idempiere-model-designer
description: Design iDempiere entities, relationships, Application Dictionary specifications and document lifecycles from business requirements. Use for functional/data design, with the actual project release; not implementation or SQL execution.
---

# Functional and data design

Establish the target checkout, release, plugin/core scope, Entity Type, supported databases and relevant repository instructions. Inspect only the affected entities and one useful local precedent. Treat version labels as hints; verify release-specific APIs and metadata in the target. If a missing fact affects correctness, label it unresolved and continue independent design work.

1. Map requirements to standard entities before proposing tables. Explain why an extension or new entity is necessary. Identify tenant/org ownership, access and invariants across UI, REST, imports and processes.
2. Specify changed/custom entities with column name, AD reference, length/precision, mandatory/default rules, PK/FK, uniqueness and business purpose. Include `AD_Client_ID`, `AD_Org_ID`, `IsActive`, `Created`, `CreatedBy`, `Updated`, `UpdatedBy`; verify PK, UUID and generated-model requirements against this release. A shared audit-column definition can be referenced by several tables instead of repeated.
3. Derive prefix/casing from the plugin and Entity Type. Map physical types only for supported engines. Do not impose PostgreSQL types on Oracle. Foreign keys may reference standard or custom entities; define cardinality, parent links and deletion policy. Justify indexes by access paths and existing indexes.
4. Use `AD_Org_ID` for administrative/accounting scope; use Warehouse, Locator or Location for physical placement. Define AD windows/tabs, references, validation, access and field behavior only where required.
5. For documents, specify supported actions, transitions, rollback/reversal and traceability. Use the normal document engine; do not simulate completion by assigning `DocStatus`. For integration boundaries, cover duplicate requests and atomicity proportionally to the requirement.

Core changes follow the target repository's database policy: specify UI changes and review developer-generated artifacts; do not author core DDL/migrations, AD IDs/UUIDs or edit generated `I_*`/`X_*` sources. Private plugins follow their own export/migration policy. A design does not authorize database writes.

Read [model-registration.md](references/model-registration.md) only when PO registration affects the design. For substantial Java decisions, use `idempiere-plugin-designer` if available; do not load it just to produce a data specification.

Return the relevant entity/column specification, relationships, lifecycle, decisions and unresolved facts with source paths. Scale the output to the requested change; diagrams and full-module documents are optional. Distinguish proposed metadata from metadata actually inspected.
