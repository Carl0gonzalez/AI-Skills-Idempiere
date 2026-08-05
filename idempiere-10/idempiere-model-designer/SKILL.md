---
name: idempiere-model-designer
description: Designs data models, entities, relationships, and functional architectures for iDempiere 10 modules using standard ERP conventions and metadata patterns.
---

# Purpose

Guide the functional and relational design of new modules, entities, and extensions for iDempiere 10. This skill focuses on logical design, mapping business requirements to iDempiere Application Dictionary concepts, enforcing standard ERP relational patterns, and establishing clean data structures before code implementation or SQL generation.

# Activation Guidance

Trigger this skill when the user asks to:
- Design the data model or tables for an iDempiere module.
- Propose entities, columns, and relationships for custom iDempiere functionality.
- Define business rules, constraints, or document lifecycles for iDempiere 10.
- Architect custom additions to fixed assets, inventory, Master Catalogs, logistics, or custom transactional modules.

Do NOT trigger this skill for general non-ERP database modeling or raw SQL/Java generation tasks unless requested as minor examples.

# Constraints and Architecture Standards

1. **Mandatory iDempiere Columns**: Every proposed custom table must contain the 7 standard audit and tenant columns:
   - `AD_Client_ID` (numeric(10)): Client/Tenant.
   - `AD_Org_ID` (numeric(10)): Administrative Organization.
   - `IsActive` (char(1)): Flag (Y/N).
   - `Created` (timestamp): Record creation timestamp.
   - `CreatedBy` (numeric(10)): User ID who created the record.
   - `Updated` (timestamp): Record update timestamp.
   - `UpdatedBy` (numeric(10)): User ID who updated the record.
2. **Naming Conventions**:
   - Derive table-name casing and the module prefix from the target plugin, its Entity Type, and repository conventions before proposing names. Use a specific, non-generic prefix consistently (e.g., `XX_Asset_Transfer`).
   - Primary keys must end with `_ID` and match the table name (e.g., `XX_Asset_Transfer_ID`).
   - Foreign keys must point to standard iDempiere entities (e.g., `M_Product_ID`, `C_BPartner_ID`, `AD_User_ID`).
3. **Administrative vs. Physical Scope**:
   - Do not misuse `AD_Org_ID` to track physical positions or inventory locations. Use physical entities like Warehouses (`M_Warehouse`), Locators (`M_Locator`), or Locations (`C_Location`) for geographical attributes. Use `AD_Org_ID` solely for administrative and accounting scoping.
4. **No Placeholders**:
   - Column types and relationships must be fully specified (e.g., numeric, varchar, char(1), timestamp). Do not leave vague descriptors like "details" or "extra information" without proposing concrete schemas.

# Workflow

Follow these steps in sequence when the skill triggers:

## Step 1: Requirements and Standard Entity Mapping
1. Analyze the functional requirements provided by the user.
2. Identify existing standard iDempiere tables that can be reused, extended, or linked (e.g. `A_Asset`, `M_Product`, `C_BPartner`, `M_Inventory`).
3. Separate the model into:
   - **Standard Entities**: Reused or referenced tables.
   - **Custom Entities**: New tables to be created.

## Step 2: Propose the Relational Schema
1. List each proposed table with its name, purpose, and columns.
2. Specify for each column:
   - Name and Data Type (e.g., `numeric(10)`, `varchar(60)`, `char(1)`, `numeric`, `timestamp`).
   - Whether it is a Primary Key (PK), Foreign Key (FK), Mandatory, or Optional.
   - Description or functional purpose.
3. Explicitly list the 7 mandatory iDempiere columns for every table.

## Step 3: Define Relationships and Keys
1. Propose the relationship card/multiplicity (e.g., One-to-Many, Many-to-Many).
2. Explicitly define parent-child relationships (e.g. Header to Line) and describe cascade deletion rules (`Cascade`, `Restrict`, or `Set Null` in the Application Dictionary context).

## Step 4: Map Lifecycle, States, and Traceability
1. If the entity behaves as a transactional document, define the Document Status fields:
   - `DocStatus` (char(2)) and `DocAction` (char(2)).
   - Describe the workflow states (e.g., Drafted `DR`, In Progress `IP`, Completed `CO`, Closed `CL`).
2. Identify how historical changes or traceability is maintained (e.g. creating log tables, audit records, or referencing standard transaction tables like `M_Transaction`).

## Step 5: Document Functional Architecture & Risks
1. Summarize key design decisions (e.g. choosing a custom table over a standard attribute extension).
2. Detail risks (e.g., performance bottlenecks with large volume transaction tables, lock contentions) and propose mitigation strategies.

# Output Contract

Produce a technical design document containing:
1. **Module Overview**: Purpose, standard iDempiere dependencies, and context.
2. **Entity List**: Details of each proposed table, including columns, types, keys, and validations.
3. **Relationship Diagram / Map**: Textual representation or Mermaid diagram of entity relationships.
4. **Lifecycle and Traceability Design**: Workflow states, transitions, and change log patterns.
5. **Architectural Rationale**: Key decisions, why custom entities were chosen over standard modifications, risks, and mitigations.

# Example Triggers

- "Design the data model for the custom asset maintenance module in iDempiere."
- "Propose entities and relationships for tracking return logistics in iDempiere 10."
- "Define tables and business rules for a custom quality control module linked to inventory."
- "Architect a logical model for tracking external project expenses on standard work orders."
