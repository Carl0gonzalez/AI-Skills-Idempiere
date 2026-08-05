---
name: idempiere-migration-review
description: Reviews and audits iDempiere 13 module proposals (logical models, DDL, AD, and Java/OSGi) for consistency, naming standards, prefix compliance, and ERP compatibility.
---

# Purpose

Review and audit technical proposals for custom iDempiere 13 modules before implementation. This skill evaluates logical models, PostgreSQL DDL scripts, Application Dictionary (AD) configurations, and Java OSGi plugin designs for cross-artifact consistency, naming standards, prefix enforcement, and safety best practices to prevent performance issues or breaking standard ERP logic.

# Activation Guidance

Trigger this skill when the user asks to:
- Review or audit an iDempiere module proposal or design.
- Validate a technical design, database migration schema, or AD mapping before implementation.
- Check for naming, prefix, or type inconsistencies between database scripts, UI designs, and Java code.
- Audit SQL scripts and dictionary settings for custom iDempiere tables.

Do NOT trigger this skill to generate code, write SQL DDL, or design UI metadata from scratch. This skill acts strictly as an auditor, providing feedback, validation reports, and correction suggestions.

# Review Principles and Checklist

Evaluate proposals against the following criteria:

## 1. Naming & Prefixes
- **Tables**: Must follow the target project's table-name casing and designated Entity Type/prefix. Derive that convention from the proposal or repository before flagging a name (e.g. `CDS_Asset`, `XX_Transfer`).
- **Columns**: Must use PascalCase (e.g. `DocumentNo`, `Processed`).
- **Constraints & Indexes**: Must be lowercase. Primary key must be `tablename_key`. Foreign keys must be `fk_tablename_referencedtable`. Indexes must be `tablename_column_idx`.

## 2. Model & DDL Alignment
- **Audit Columns**: Ensure the 7 mandatory iDempiere columns (`AD_Client_ID`, `AD_Org_ID`, `IsActive`, `Created`, `CreatedBy`, `Updated`, `UpdatedBy`) are present in both the logical design and DDL script.
- **Data Types**: Check that IDs use `numeric(10)` and flags use `char(1)` with a check constraint (e.g. `CHECK (IsActive IN ('Y', 'N'))`). Ensure no raw Postgres `boolean` or auto-incrementing serial types are used for IDs.
- **Foreign Key Indexes**: Verify that every foreign key column has a corresponding performance index.

## 3. Cross-Artifact Consistency
- **Table Names**: Compare table names across the logical model, DDL, AD mapping, and PO class names (e.g. table `CDS_Asset_Transfer` must match AD metadata and map to PO class `MAssetTransfer` extending `X_CDS_Asset_Transfer`).
- **Data References**: Check that columns marked as references (like Warehouses, Partners, Users) point to the correct tables and use Search/TableDir reference types in the AD proposal.

## 4. UI/AD Quality
- **Hierarchy**: Verify parent-child tabs have link columns defined.
- **Display Logic**: Check that Display Logic and Read-Only syntax matches iDempiere standards (e.g. `@Processed@='N'`).
- **Fields**: Ensure internal audit columns are not exposed on tabs unless strictly required as read-only.

## 5. Plugin Architecture & ERP Safety
- **Standard Logic Preservation**: Ensure the design does not override core standard database tables or columns without strong justification.
- **Org Scope**: Confirm `AD_Org_ID` is used only for administrative/accounting partitions, not geographic positions.
- **Factories**: Verify factories (Model, Process, Callout, Event) are correctly structured and listed for OSGi registration.

# Required Output Format

When reviewing a proposal, return the following structured sections:

## 1. Review Result
- **Result Status**: One of `Approve`, `Approve with minor fixes`, `Revise before use`, or `Reject`.

## 2. Findings
Categorized bullet list of issues found during the audit:
- **Critical Issues** (e.g. missing audit columns, boolean fields, missing foreign key indexes, breaking standard logic).
- **Naming & Prefix Gaps** (e.g. lowercase tables, missing `CDS_` prefixes, inconsistent constraint names).
- **Inconsistencies** (e.g. data type mismatch between logical model and DDL, mismatch in PO class name).

## 3. Suggested Fixes
- Provide the exact corrected SQL snippets, AD configurations, or class mapping definitions to resolve the findings.

## 4. Final Recommendation
- Clear instruction on whether to proceed with DDL execution, AD registration, or plugin creation, including any high-risk areas to monitor (e.g. table locking).

# Example Triggers

- "review this iDempiere module proposal"
- "validate this technical design before implementation"
- "audit this SQL and dictionary"
- "detect inconsistencies between model, DDL, and plugin"
