---
name: idempiere-wlistbox-custom-editor
description: Customize rendering or editing of a WListbox column using WTableColumn editor providers and WEditor APIs supported by the target iDempiere release. Use for existing form columns, not general AD field editors.
---

# WListbox column editors

## Target and registration preflight

- Read the target repository instructions and exact release metadata. Confirm required classes and method signatures in that release's source or resolved target platform; a source file need not be present in the workspace if its dependency is resolved.
- Inspect the existing scaffold, factories, activator, MANIFEST.MF, build.properties and DS output. Reuse the existing mechanism; do not introduce a second registry or replace an activator just to match an example.
- Check AD prerequisites through available read-only tools, exported metadata or source. If required metadata cannot be verified, report the missing evidence. No particular connector or IDE is required.
- For core contributions, read the target core AGENTS.md and database-change skill before changing AD/schema. Agents specify and review generated migrations; they do not author scripts, IDs or UUIDs for core.
- Implement only supported APIs. For an unsupported API, retain a compatible existing pattern or report the limitation; placement in shared/ is not a claim of support on every release.
## Workflow

1. Locate the actual WListbox, renderer and stable column definition. Confirm the runtime implementation before casting an IMiniTable.
2. Verify WListItemRenderer.getColumn, WTableColumn.setEditorProvider and WEditor methods in the target release. If unavailable, use that release's existing renderer/editor extension point.
3. Install the editor provider after the column model is initialized. Ensure refresh/rebuild does not discard it or register repeated listeners.
4. Preserve read-only status, editability, data type, precision, locale and change-event propagation. Customize the display component when only appearance is needed; do not change persistence behavior unnecessarily.
5. Reset reused component styles for every row, including null/default values. Never derive an unsafe HTML/style fragment from unchecked input.
6. Test null/zero/positive/negative values as relevant, sorting, editing, read-only rows, refresh and keyboard behavior. Styling must not leak from one row into another.

## Verification and output

Report the chosen mechanism, verified release/API source, affected files, registration and AD requirements, build/test commands and results, and remaining runtime checks. Validate compilation and packaged DS/resources with the actual builder. Distinguish compilation, OSGi activation, database behavior and UI/REST execution. Do not claim an unexecuted check passed. Implementation does not authorize installation, PackIn, database changes or publication.
