---
name: idempiere-pipo-integrity-review
description: Performs an iDempiere PackOut preflight by comparing Application Dictionary columns with physical PostgreSQL or Oracle types and checking PIPO dependencies before export.
---

# Purpose

Review iDempiere Application Dictionary infrastructure before creating or installing a 2Pack/PIPO package. The review must run before every export; correct the source dictionary rather than repairing a ZIP after export.

Use this skill to verify that a module's windows, tabs, fields, tables, columns, elements, references, validation rules, and Pack Out lines are internally consistent and exportable. The main goal is to prevent PackIn failures such as `Unresolved elements`, especially unresolved `AD_Tab_ID`, `AD_Table_ID`, `AD_Column_ID`, `AD_Reference_ID`, or `AD_Val_Rule_ID`.

This skill is based on the local iDempiere PIPO behavior in:

- `org.adempiere.pipo2.AbstractElementHandler`
- `org.adempiere.pipo2.handler.WindowElementHandler`
- `org.adempiere.pipo2.handler.TabElementHandler`
- `org.adempiere.pipo2.handler.FieldElementHandler`
- `org.adempiere.pipo2.handler.TableElementHandler`
- `org.adempiere.pipo2.handler.ColumnElementHandler`
- `org.adempiere.pipo2.handler.ReferenceElementHandler`

The preflight prevents type mismatches where `ColumnElementHandler` generates an Oracle statement such as:

```sql
ALTER TABLE XX_CustomTable MODIFY xx_related_id VARCHAR2(10 CHAR)
```

when the physical column is an Oracle `NUMBER` or PostgreSQL `numeric`.

# Activation Guidance

Trigger this skill when the user asks to:

- Review a Pack Out before exporting from iDempiere.
- Diagnose PackIn or 2Pack errors with `Unresolved elements`.
- Verify iDempiere windows, tabs, fields, tables, columns, elements, references, or validation rules before migration.
- Check whether a custom Application Dictionary object will be included in a Pack Out.
- Fix metadata exported from PostgreSQL iDempiere and imported into Oracle iDempiere.

# Constraints

- Use read-only SQL first.
- Do not execute `UPDATE`, `INSERT`, `DELETE`, `CREATE`, `ALTER`, `DROP`, or restore/import operations without explicit user approval.
- Do not assume the remote target database is available. Validate the source Pack Out and source dictionary first.
- Do not mark Dictionary (`D`) records as custom unless they are truly custom records incorrectly created with `EntityType='D'`.
- Prefer fixing the underlying AD metadata over masking the problem by enabling broad dictionary export.
- Never print database passwords or secret connection strings.
- Never declare a PackOut ready based only on the XML or only on `AD_COLUMN`; both dictionary metadata and physical columns must agree.
- Never silently change metadata during a review. Report the exact approved fix separately; updates require explicit user approval.
- A failed preflight blocks export. Do not generate or recommend a 2Pack while any blocking finding remains.

# Mandatory Preflight

Run this section before reviewing windows or exporting any PackOut. It is the required gate for every package containing custom tables.

## 1. Resolve package tables

List every table included by `AD_PACKAGE_EXP_DETAIL` and include tables nested under package windows. Do not validate only the table named in the latest error.

```sql
SELECT DISTINCT d.ad_table_id, t.tablename, t.entitytype
FROM ad_package_exp_detail d
JOIN ad_table t ON t.ad_table_id = d.ad_table_id
WHERE d.ad_package_exp_id = <AD_Package_Exp_ID>
ORDER BY t.tablename;
```

## 2. Compare dictionary columns to physical columns

For PostgreSQL:

```sql
SELECT t.tablename,
       c.columnname,
       c.ad_column_id,
       c.ad_column_uu,
       c.ad_element_id,
       c.ad_reference_id,
       r.name AS reference_name,
       c.ad_reference_value_id,
       c.fieldlength,
       ic.data_type,
       ic.udt_name,
       ic.character_maximum_length,
       ic.numeric_precision,
       ic.numeric_scale
FROM ad_column c
JOIN ad_table t ON t.ad_table_id = c.ad_table_id
LEFT JOIN ad_reference r ON r.ad_reference_id = c.ad_reference_id
LEFT JOIN information_schema.columns ic
  ON lower(ic.table_name) = lower(t.tablename)
 AND lower(ic.column_name) = lower(c.columnname)
WHERE t.ad_table_id IN (<package_table_ids>)
ORDER BY t.tablename, c.columnname;
```

For Oracle:

```sql
SELECT t.tablename,
       c.columnname,
       c.ad_column_id,
       c.ad_column_uu,
       c.ad_element_id,
       c.ad_reference_id,
       r.name AS reference_name,
       c.ad_reference_value_id,
       c.fieldlength,
       uc.data_type,
       uc.data_length,
       uc.data_precision,
       uc.data_scale
FROM ad_column c
JOIN ad_table t ON t.ad_table_id = c.ad_table_id
LEFT JOIN ad_reference r ON r.ad_reference_id = c.ad_reference_id
LEFT JOIN user_tab_columns uc
  ON upper(uc.table_name) = upper(t.tablename)
 AND upper(uc.column_name) = upper(c.columnname)
WHERE t.ad_table_id IN (<package_table_ids>)
ORDER BY t.tablename, c.columnname;
```

## 3. Blocking column rules

Flag `BLOCKER` when any of these conditions is true:

- A physical column is numeric (`NUMBER` or `numeric`) but its dictionary definition would produce a text type. In particular, a custom `*_ID` column with `AD_REFERENCE_ID=18` and `FieldLength=10` must be reviewed; this exact combination produced the ORA-02267 failure.
- A physical column is text but the dictionary reference is an ID/table reference that produces a numeric type.
- `AD_COLUMN.FIELDLENGTH` is incompatible with the physical type or expected iDempiere ID convention. Custom numeric IDs should normally use `FieldLength=22`.
- A package column has no physical counterpart when `IsSyncDatabase='Y'`, unless it is intentionally created by a documented SQLMandatory step.
- The XML or source metadata contains duplicate columns for the same table and column name.
- `AD_ELEMENT_ID`, `AD_COLUMN_UU`, or `AD_TABLE_ID` is missing for a custom column.
- A reference ID or reference value is missing from the source package and is not already present in the destination contract.

## 4. Project ID policy

Derive expected references, field lengths, and physical types from the project DDL and Application Dictionary. Record every intentional exception in the review result; do not infer types from a display name.

## 5. PackOut XML verification

After the source dictionary passes, export a temporary PackOut and inspect `dict/PackOut.xml`. For every blocking column, verify the XML contains the expected `FieldLength` and `AD_Reference_ID`. The ZIP must also use forward-slash paths (`/`) so it can be unpacked on Debian. A valid source database does not make an old ZIP valid.

Example check:

```bash
unzip -p <packout.zip> '*/dict/PackOut.xml' \\
  | grep -A35 -B5 '<column-name>'
```

Reject the ZIP if it contains a dictionary value inconsistent with the approved project policy or uses Windows backslash paths.

The deterministic XML gate is available at:

```powershell
& <skill-directory>/scripts/Validate-PackOutXml.ps1 -ZipPath '<packout.zip>'
```

Only `RESULT=READY blockers=0` permits installation. Any `BLOCKER` or exit code `2` means the source metadata or ZIP must be corrected and exported again.

Run any repository-provided UUID ownership gate as a second validator. Do not distribute or install the package unless every applicable validator returns `RESULT=READY`.

# PIPO Rules To Validate

1. `EntityType` controls exportability.
   - PIPO skips Dictionary (`D`) and official extension entity types when the package is not exporting dictionary entities.
   - A custom window, tab, field, table, column, reference, or element should normally use the same custom entity type, such as `U` or a project-specific entity type.

2. A window Pack Out line exports nested tabs and fields.
   - `WindowElementHandler` exports the window, then all tabs in `AD_Tab` for that window.
   - `TabElementHandler` exports a tab only if it passes `isPackOutElement`.
   - `TabElementHandler` still iterates and exports fields, so mismatched entity types can create fields whose parent tab is missing from the XML.

3. Every exported field must have resolvable parents.
   - `AD_Field.AD_Tab_ID` must resolve to an exported or pre-existing `AD_Tab`.
   - `AD_Field.AD_Column_ID` must resolve to an exported or pre-existing `AD_Column`.

4. Every exported column must have resolvable dependencies.
   - `AD_Column.AD_Table_ID` must resolve to `AD_Table`.
   - `AD_Column.AD_Element_ID` must resolve to `AD_Element`.
   - Table, Search, and List references must have their `AD_Reference` or reference values present when custom.

5. Tabs in child levels should be checked for parent linkage.
   - Detail tabs should have a reliable parent relationship through `Parent_Column_ID` or a valid FK column pattern.
   - Missing `Parent_Column_ID` may not always break PackIn, but it can break window behavior after import.

# Workflow

Follow these steps in order.

## Step 1: Identify The Package

Find the target `AD_Package_Exp` by name or ID.

Recommended SQL:

```sql
SELECT ad_package_exp_id, name, ad_package_type, pk_version, version, releaseno,
       isexportdictionaryentity, isincludeorganizationid, processed, processing
FROM ad_package_exp
WHERE lower(name) LIKE lower('%<name>%')
ORDER BY updated DESC;
```

## Step 2: Inspect Pack Out Lines

List package lines in execution order and identify windows, tables, references, processes, and SQL statements.

```sql
SELECT d.ad_package_exp_detail_id, d.line, d.type, d.name2,
       d.ad_window_id, w.name AS window_name,
       d.ad_table_id, t.tablename,
       d.ad_reference_id, r.name AS reference_name,
       d.sqlstatement
FROM ad_package_exp_detail d
LEFT JOIN ad_window w ON w.ad_window_id = d.ad_window_id
LEFT JOIN ad_table t ON t.ad_table_id = d.ad_table_id
LEFT JOIN ad_reference r ON r.ad_reference_id = d.ad_reference_id
WHERE d.ad_package_exp_id = <AD_Package_Exp_ID>
ORDER BY d.line, d.ad_package_exp_detail_id;
```

## Step 3: Validate Window Infrastructure

For each package window, list all tabs and their table/entity alignment.

```sql
SELECT tb.ad_tab_id, tb.ad_tab_uu, tb.name AS tab_name, tb.seqno, tb.tablevel,
       tb.entitytype AS tab_entitytype,
       w.entitytype AS window_entitytype,
       t.ad_table_id, t.tablename, t.entitytype AS table_entitytype,
       tb.parent_column_id, pc.columnname AS parent_column
FROM ad_tab tb
JOIN ad_window w ON w.ad_window_id = tb.ad_window_id
JOIN ad_table t ON t.ad_table_id = tb.ad_table_id
LEFT JOIN ad_column pc ON pc.ad_column_id = tb.parent_column_id
WHERE tb.ad_window_id = <AD_Window_ID>
ORDER BY tb.seqno;
```

Flag:

- Custom tabs with `EntityType='D'`.
- Tabs whose `EntityType` differs from their custom window and fields.
- Child tabs with missing or suspicious parent linkage.

## Step 4: Validate Field And Column Dependencies

```sql
SELECT tb.name AS tab_name, f.ad_field_id, f.ad_field_uu, f.name AS field_name,
       f.entitytype AS field_entitytype,
       tb.entitytype AS tab_entitytype,
       c.ad_column_id, c.ad_column_uu, c.columnname,
       c.entitytype AS column_entitytype,
       t.tablename
FROM ad_field f
JOIN ad_tab tb ON tb.ad_tab_id = f.ad_tab_id
JOIN ad_column c ON c.ad_column_id = f.ad_column_id
JOIN ad_table t ON t.ad_table_id = c.ad_table_id
WHERE tb.ad_window_id = <AD_Window_ID>
ORDER BY tb.seqno, f.seqno, f.ad_field_id;
```

Flag:

- Fields whose tab exists in source but will not export due to `EntityType`.
- Fields referencing columns outside the exported table set.
- Columns without UUIDs when IDs are custom.

## Step 5: Validate Elements And References

```sql
SELECT t.tablename, c.columnname, c.ad_column_id, c.ad_element_id,
       e.columnname AS element_columnname,
       c.ad_reference_id, rt.name AS reference_type,
       c.ad_reference_value_id, rv.name AS reference_name,
       c.ad_val_rule_id, vr.name AS val_rule_name
FROM ad_column c
JOIN ad_table t ON t.ad_table_id = c.ad_table_id
LEFT JOIN ad_element e ON e.ad_element_id = c.ad_element_id
LEFT JOIN ad_reference rt ON rt.ad_reference_id = c.ad_reference_id
LEFT JOIN ad_reference rv ON rv.ad_reference_id = c.ad_reference_value_id
LEFT JOIN ad_val_rule vr ON vr.ad_val_rule_id = c.ad_val_rule_id
WHERE t.ad_table_id IN (
  SELECT ad_table_id FROM ad_tab WHERE ad_window_id = <AD_Window_ID>
)
ORDER BY t.tablename, c.columnname;
```

Flag:

- Custom elements not included or with wrong `EntityType`.
- Custom references missing from Pack Out.
- Custom validation rules missing from Pack Out.

## Step 6: Recommend Minimal Fixes

Prioritize fixes in this order:

1. Correct wrong `EntityType` on custom AD records.
2. Add missing Pack Out lines for windows, tables, references, processes, or SQL mandatory steps.
3. Correct missing tab parent linkage or invalid field/column references.
4. Use `IsExportDictionaryEntity='Y'` only when the package intentionally exports dictionary-maintained records.

# Output Contract

Return:

1. **Review Result**: `READY`, `NEEDS METADATA FIX`, or `BLOCKED - DO NOT EXPORT`.
2. **Root Cause**: Short explanation of the specific missing or mismatched infrastructure.
3. **Evidence**: Key SQL result rows, with IDs and UUIDs.
4. **Recommended Fix**: Exact SQL if a metadata change is required, but do not execute it without approval.
5. **Re-export Instructions**: What the user should do in Pack Out after the fix.
6. **Residual Risks**: Anything that may still fail on the target, such as missing physical tables or remote DB schema differences.

The output must include a compact column preflight table with:

`table | column | AD reference | field length | dictionary type | physical type | status | reason`

Do not report `READY` unless every package table has passed the preflight and the exported XML has been inspected.

# Example Trigger Prompts

- "Revisa este Pack Out antes de exportarlo."
- "PackIn me da unresolved AD_Tab_ID."
- "Validate this iDempiere window infrastructure."
- "Ensure tables, windows, tabs, columns, and references are exported."
- "Diagnostica por que mi 2Pack exportado de PostgreSQL falla al importar en Oracle."
