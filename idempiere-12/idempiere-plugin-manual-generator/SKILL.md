---
name: idempiere-plugin-manual-generator
description: Analyzes Java code and dictionary metadata of an iDempiere plugin to generate an English functional user manual and test guide.
---

# Purpose

This skill guides the agent in analyzing an iDempiere OSGi plugin (examining Java source code for business logic and UI interactions, along with Application Dictionary metadata) to document its functional behavior in a user-friendly manual and test guide.

# Activation Guidance

Activate this skill when requested to:
- Design, generate, or write a user manual or functional documentation for an iDempiere plugin.
- Document functional workflows, test guides, or screen walkthroughs for ERP components based on plugin code.
- Analyze what a plugin does and translate it into clear steps for business analysts or end-users.
- Generate QA or training materials based on plugin source code.

# Constraints

- **Functional Focus**: The resulting manual must be clear for end-users. Avoid internal code jargon (Java classes, interfaces, callbacks) in titles or main text, keeping them only in support mapping tables.
- **No Assumptions**: If Java code contains complex conditions or optional parameters where the business flow is ambiguous, ask the user or document them in a "Questions or Pending Items" section.
- **Language Constraint**: Write the generated user manual and test guide in clear, formal English unless the user explicitly requests another language.

# Technical Analysis Workflow

Analyze the plugin's source code and metadata before writing the manual:

1. **Process Analysis (`SvrProcess`)**:
   - Locate classes extending `SvrProcess` (usually in `.process` packages).
   - Read the `prepare()` method to identify UI parameters (mandatory/optional fields in the process window).
   - Read the `doIt()` method to understand the main business logic, validations, and expected outcomes.

2. **Model Validator Analysis (`ModelValidator`)**:
   - Locate classes implementing `ModelValidator` or listening to persistence events in `.event` packages.
   - Trace validations that throw `AdempiereException` or `SaveError`. These restrictions form the basis of the **Negative Tests** section in the user manual.

3. **Callout Analysis (`CalloutEngine`)**:
   - Locate classes extending `CalloutEngine` (usually in `.callout` packages).
   - Trace dynamic field dependencies (e.g., clearing or filtering dependent fields, like Address -> Department -> Section).

4. **Dictionary Metadata Analysis**:
   - Look for SQL migration scripts in `migration/` or dictionary packages (`2pack/`, `dict/`, or `PackOut.xml`).
   - Identify added or modified windows (`AD_Window`), tabs (`AD_Tab`), tables (`AD_Table`), and columns (`AD_Column`).

# Mandatory Manual Structure

The generated manual must be in Markdown and follow this structure:

## 1. Title
Functional title of the process or window (e.g., `# Test Manual: Asset Creation and Activation`).

## 2. Objective
A brief business-oriented description (1-2 paragraphs) of the problem this feature solves and the expected result.

## 3. Terminology Mapping
A table mapping database/code technical names to the functional labels visible in the UI:
| Technical name | Functional label |
|---|---|
| E.g., `A_Asset` | Asset |
| E.g., `CDS_A_AssetClassifier_ID` | Asset classifier |

## 4. Prerequisites and Packages
- List dictionary packages (`2pack.zip`) to import.
- State functional prerequisites (e.g., active accounting schema, test supplier).

## 5. Step-by-step Functional Test Guides
Divide the document into logical test scenarios (e.g., "Test 1: Asset master data"). For each scenario, provide:
1. **Numbered action steps**: UI interactions (e.g., "Open window X and create a record", "Select product Y").
2. **Expected result**: UI behavior and database updates (e.g., "The operating status changes to 'Pending assignment'").

## 6. Negative Tests
Numbered scenarios validating that business rules prevent invalid states (e.g., "Try to save an asset without a classifier; the system must prevent the action").

## 7. Evidence
An empty table for testers to document IDs and statuses (e.g., `A_Asset_ID`, `DocumentNo`, Accounts debited/credited), followed by required screenshots list.

## 8. Cleanup
Instructions on post-test steps (e.g., "Do not delete completed documents. To repeat the test, create a new asset").

# Output Contract

Produce:
1. A brief technical summary of the analyzed plugin files.
2. The complete Markdown manual in English adhering to the defined structure.
