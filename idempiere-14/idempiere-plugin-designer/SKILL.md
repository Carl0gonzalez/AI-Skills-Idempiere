---
name: idempiere-plugin-designer
description: Translates functional designs and data models into technical Java specifications, package structures, PO classes, callouts, processes, and OSGi plugins for iDempiere 14.
---

# Purpose

Translate logical data models and Application Dictionary specifications for iDempiere 14 into technical implementation designs for Java development. This skill maps tables and columns to PO (Persistent Object) classes, suggests package layouts, defines Process execution structures, structures Callouts and Model Validators, and details OSGi service extension registrations without immediately generating complete code blocks.

# Activation Guidance

Trigger this skill when the user asks to:
- Translate an iDempiere data model or AD design into a Java technical implementation plan.
- Propose packages, classes, factories, or OSGi structure for an iDempiere 14 plugin.
- Design Java Callouts, Model Validators, Event Handlers, or custom processes (`SvrProcess`).
- Propose extension points, component XML configurations, or service factories for OSGi.

Do NOT trigger this skill to design the initial database model (use `idempiere-model-designer`) or to generate SQL DDL from scratch. This skill focuses strictly on Java architecture, design patterns, and OSGi components.

# Constraints and Development Standards

1. **PO Class Conventions**:
   - Model classes must extend the generated `X_` classes (e.g. `MMyTable` extending `X_XX_MyTable`).
   - Transactional documents should implement the `DocAction` interface if they use the document routing engine.
2. **Existing registration first**:
   - Reuse actual IModelFactory/IProcessFactory/IColumnCalloutFactory mappings or target-supported annotation/mapped services.
   - Create only the missing mechanism required by the design; do not add all factories by default.
   - Event registrations use the actual handler/delegate APIs. Do not invent IEventFactory.
3. **OSGi registration**:
   - Inspect the target plugin's `MANIFEST.MF`, `build.properties`, and existing registrations first.
   - Follow its established registration style: `OSGI-INF/*.xml` when the bundle declares service components, or DS annotations only when the bundle already builds and exposes them correctly.
4. **Event Handler Topics**:
   - Use standard `IEventTopics` constants for custom event handlers (e.g., `PO_AFTER_NEW`, `PO_BEFORE_CHANGE`, `DOC_BEFORE_PREPARE`).
5. **Callout Interfaces**:
   - Follow the existing CalloutEngine or IColumnCallout registration. Use annotations only when the target supports them; cross-entry invariants need model/event enforcement.
6. **Process Classes**:
   - Custom processes must extend `SvrProcess` and override `prepare()` (for parameter parsing) and `doIt()` (for core execution logic).

# Context and design boundaries

Read target instructions and the architecture skill when available. Core contributions follow its Jira/database policy; do not author migrations/AD IDs. Private plugins retain their own conventions. Preserve public/protected APIs with overloads/deprecation and search callers. Prefer AD or existing components before adding packages/layers; pass owning transactions and preserve tenant/role access.

# Workflow

Follow these steps in sequence when the skill triggers:

## Step 1: Analyze Logical and Dictionary Models
1. Review the proposed tables, columns, references, and workflows.
2. Separate entities into:
   - Documents (needs `DocAction` implementation).
   - Master Catalog records (needs model validation, default behaviors).
   - Auxiliary tables.

## Step 2: Propose Package Structure and Naming
1. Define a standard Java package structure (e.g., `com.company.module.model`, `com.company.module.process`, `com.company.module.validator`, `com.company.module.factory`).
2. Identify naming prefixes matching the module.

## Step 3: Define Model PO and Factory Classes
1. List the custom `M_` classes that need implementation.
2. Outline the `IModelFactory` mapping required to bind database table names to custom PO class instantiations.

## Step 4: Propose Callouts and Model Validators
1. Propose Callout classes for fields requiring dynamic calculations, detailing the class name and the logic.
2. Propose Model Validators and Event Handlers, detailing the target tables and the specific lifecycle topics (`PO_BEFORE_NEW`, `PO_AFTER_CHANGE`, etc.) they will subscribe to.

## Step 5: Define Processes and Parameters
1. Propose custom process classes extending `SvrProcess`.
2. Map real AD parameters to prepare() parsing or verified @Parameter injection under the existing factory.
3. Provide a pseudo-code or step-by-step description of the execution flow in `doIt()`.

## Step 6: Identify OSGi Declarative Services Configurations
1. Outline the exact registration artifacts required by the target plugin for Model, Process, Callout, and Event Factories.
2. Detail package imports/exports inside the `MANIFEST.MF`.

# Output Contract

Produce a technical java plugin design document containing:
1. **Plugin Overview**: Project structure and OSGi parameters.
2. **Java Class List**: Table mapping PO classes, SvrProcess classes, Callouts, and Validators.
3. **Package Structure**: Structured package tree with names and purposes.
4. **OSGi Service Registrations**: XML configurations (`OSGI-INF/`) for factories.
5. **Business Logic Pseudo-code**: Step-by-step logic description for callouts, event handlers, and processes.
6. **Technical Risks & Integration Best Practices**: Mitigation strategies for locking, transaction safety, and avoiding overrides of core iDempiere classes.

# Example Triggers

- "give me the plugin design for this iDempiere module"
- "suggest PO classes and packages"
- "define validators and OSGi processes"
- "translate this model into technical Java implementation for iDempiere 14"
