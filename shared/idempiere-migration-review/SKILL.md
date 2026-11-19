---
name: idempiere-migration-review
description: Review iDempiere proposals and changes for consistency across data models, SQL, Application Dictionary and Java/OSGi. Use for evidence-based design or migration review across target releases; not execution, implementation or a substitute for runtime tests.
---

# Cross-artifact review

Establish the target release, plugin/core scope, supported engines, Entity Type and exact artifacts/diff under review. Read repository instructions and relevant neighboring code; do not scan unrelated modules. Review the supplied evidence independently, including a design's assumptions.

Check what applies:

- Model/AD/physical schema agree on names, types, lengths, nullability, defaults, keys, references and uniqueness. Audit/tenant columns, PK/UUID and generated-model expectations match the target release. Foreign keys may reference custom entities.
- Prefix, casing, constraint names and registrations follow actual conventions. Do not classify a name, missing per-FK index or annotation choice as defective merely because another project does it differently. Assess indexes against workload and existing composite indexes.
- AD tabs have correct parent links, access, references and target-supported display/read-only/mandatory logic. UI restrictions are not the sole enforcement of cross-entry invariants.
- Java/OSGi registration uses existing factories or supported mapped/DS mechanisms. Verify event topics and APIs locally; there is no generic requirement to add an Event Factory.
- Tenant/org isolation, transaction ownership, document actions, retry/rollback, concurrency and API compatibility are preserved where affected. Standard documents are completed through normal processing.
- If PackOut/PackIn is relevant, use the matching project's `idempiere-pipo-integrity-review` when available. Report unavailable tooling/evidence instead of claiming package validation.

For core, read the target database-change rules (or `idempiere-database-changes` when available). Review developer-generated migrations and required engine equivalents; provide UI correction specifications without inventing SQL/AD IDs or editing generated models. Private-plugin corrections follow their supported engines and migration policy.

This is a read-only review unless the user separately requests fixes. Do not execute DDL, PackIn, SyncDB or deployment to prove a static finding. Use `idempiere-plugin-quality-gate` only for requested or necessary executable validation within authorized resources; do not run its entire workflow for a design review.

Return a verdict (`no blocking findings`, `revise before use`, or `insufficient evidence`) and findings with severity, artifact path/line, concrete trigger, impact and minimum correction. Separate verified defects from questions and optional improvements. State coverage and tests actually run; an approval of a design is neither runtime validation nor authorization to apply it. If there are no findings, say so without filling a checklist with generic advice.
