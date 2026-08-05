---
name: idempiere-plugin-readme
description: Use this skill when creating or updating README files for iDempiere plugin repositories. Applies exclusively to iDempiere OSGi plugins, plugin fragments, MANIFEST.MF metadata, 2Pack content, process/event/callout documentation, component lists, prerequisites, and repository-level plugin documentation.
---

# iDempiere Plugin README

## Purpose

Create or update `README.md` files for iDempiere plugin repositories using a consistent English structure based on the actual project code and metadata. The README must describe what the plugin does, what it contains, what it requires, how to install or use it, and what functional behavior is provided by processes, events, callouts, models, and 2Pack content.

## Scope

Use this skill only for iDempiere plugin repositories.

The README must always be written in English, even if the current README or source messages are in Spanish.

Do not invent functionality. Infer behavior from source code, `META-INF/MANIFEST.MF`, 2Pack files, model classes, annotations, XML metadata, existing README content, and project structure. If a detail is not supported by the repository, omit it or state it conservatively.

## First Steps

Before writing or updating the README:

1. Identify the main plugin bundle directory and bundle symbolic name.
2. Read `META-INF/MANIFEST.MF` for each relevant project, especially the main plugin project.
3. Inspect the `src` folder structure and packages ending in `.process`, `.event`, `.callout`, `.model`, and other functional packages.
4. Inspect `META-INF` for 2Pack files or metadata that installs processes, windows, tables, references, messages, menus, model validators, or other application dictionary records.
5. Inspect existing `README.md` content and preserve correct facts while converting the structure and language to this standard.

## Required README Structure

Use this order:

```markdown
# <plugin.bundle.id>

- Copyright: <year> https://www.casadelsoftware.com
- Repository: <repository-url>
- License: GPL 2

## Description

<short plugin objective and behavior summary>

## Contributors

- <year> <Name> <email@example.com>.

## Components

- iDempiere Plugin [<plugin.bundle.id>](<plugin.bundle.id>)
- iDempiere Unit Test Fragment [<plugin.bundle.id>.test](<plugin.bundle.id>.test)

## Prerequisites

- Java <version>, commands `java` and `javac`.
- iDempiere <version>
- <additional non-base dependency>

## Features/Documentation

### Source Structure

<brief `src` folder/package structure before functional details>

<functional documentation based on code>

## Instructions

<installation or usage instructions>

## Extra Links

<only include this section when real links exist>
```

## Sections To Omit

Always omit these unless the user explicitly asks otherwise:

- `## Commands`
- Build command examples such as `./build`, `./build debug`, or `build.bat`.
- `iDempiere Target Platform` entries in `Components`.
- `Set IDEMPIERE_REPOSITORY env variable` in `Prerequisites`.
- `Extra Links` when there are no real links to include.

## Metadata Rules

- The H1 title must be the main plugin bundle ID, for example `# com.cdsoftware.lirion.posintegration`.
- Prefer repository URLs from the existing README, remote metadata, or visible project references.
- Use `GPL 2` as the license unless repository evidence clearly says otherwise.
- Use Casa del Software copyright format when no more specific valid project copyright exists.
- Contributors must use this format: `- Year Name <name@email.com>.`
- If only a company contributor is known, use a concise company line only if supported by existing project content.
- Always ask the user for the list of contributors and their email addresses if they are not explicitly defined in the project files.

## Components Rules

Include only components that exist in the repository.

Allowed component types:

- `iDempiere Plugin [bundle.id](bundle.id)`
- `iDempiere Unit Test Fragment [bundle.id.test](bundle.id.test)`

Do not include target platform components, even if a `.targetplatform` project exists.

## Prerequisites Rules

Determine Java and iDempiere versions and other plugin dependencies from project evidence instead of guessing.

Primary sources:

- `META-INF/MANIFEST.MF`
- `Bundle-RequiredExecutionEnvironment`
- `Require-Capability`
- `Require-Bundle`
- `Import-Package`
- target platform metadata only when needed to infer versions
- existing README only when supported by project metadata

Base prerequisites always include:

- Java version and commands `java` and `javac`.
- iDempiere version.
- Dependency on other custom or non-base plugins. Inspect the `Require-Bundle` and `Import-Package` headers of `META-INF/MANIFEST.MF` to check if this plugin depends on another custom or non-base plugin. If it does, list it clearly under the Prerequisites.

Do not include `IDEMPIERE_REPOSITORY`.

Add additional dependencies only when they are not part of this base dependency ignore list:

- `org.adempiere.base`
- `org.adempiere.plugin.utils`
- `org.adempiere.ui.zk`
- `org.apache.commons.lang3`
- `commons-lang3`
- `freemarker`
- `lib/freemarker.jar`
- `zcommon`
- `zel`
- `zhtml`
- `zk`
- `zkbind`
- `zkplus`
- `zul`
- `zweb`

When listing additional dependencies, keep names concise and use bundle/package IDs when that is the clearest source of truth.

## Description Rules

Write a brief description that explains the plugin's objective and the main business or technical capability it provides.

Good descriptions:

- Explain whether the plugin is a backend support plugin, UI extension, integration layer, localization extension, or business process plugin.
- Mention the main iDempiere area affected, such as POS, inventory, invoices, orders, users, accounting, reporting, or window behavior.
- Avoid long implementation detail; detailed behavior belongs in `Features/Documentation`.

Avoid:

- Placeholder text such as `Put the plugin description here`.
- Spanish headings or Spanish prose.
- Marketing claims not supported by the code.

## Features/Documentation Rules

This is the main functional documentation section. Include all relevant behavior found in the plugin.

Start this section with a `### Source Structure` subsection before describing processes, events, callouts, models, or 2Pack content. Represent the relevant `src` package/folder layout as a Markdown fenced code block using a tree-style structure. Include actual functional folders/packages and Java files that exist in the repository, such as `process`, `event`, `callout`, `model`, `component`, `form`, `util`, `base`, or project-specific service packages. Do NOT omit files or folders from this tree structure (avoid using `...` or generic markers). All source files must be fully listed. Do not use a table for this subsection.

Example:

```markdown
### Source Structure

```text
com.example.plugin/src
└── com
    └── example
        └── plugin
            ├── callout
            │   ├── ExampleCallout.java
            │   └── AnotherCallout.java
            ├── component
            │   ├── CalloutFactory.java
            │   ├── EventFactory.java
            │   ├── ModelFactory.java
            │   └── ProcessFactory.java
            ├── event
            │   └── ExampleEvent.java
            ├── model
            │   ├── MExample.java
            │   └── I_Example.java
            └── process
                ├── ExampleProcess.java
                └── AnotherProcess.java
```
```

Always format the following sections using highly structured markdown tables to ensure clean organization and maximum level of detail:

1. **Processes**: Group all processes under `.process` (or registered elsewhere) in a single structured table detailing:
   * Class Name
   * Purpose
   * Main Parameters (and whether they are required)
   * Key Logic & Results
   Do not leave any process files undocumented.

2. **Events**: Group all events and event handlers (such as model validators or topics registered in `.event` or custom handlers) in a structured table detailing:
   * Target Model / Table
   * Event Timing / Topic (e.g. `PO_AFTER_NEW`, `PO_AFTER_CHANGE`)
   * Functional Rule & Objective

3. **Callouts**: Group all callout classes in a structured table detailing:
   * Callout Class
   * Target Field / Column
   * Business Validation & UI Impact

4. **Application Dictionary Metadata (2Pack)**: List all zip or xml metadata packages in `META-INF` (or other config paths) in a structured table detailing:
   * Package / File Name
   * Purpose & Dictionary Configurations

Document models found in `.model` packages when they help explain custom tables or business data. Do not dump generated model fields unless they clarify plugin behavior.

## Instructions Rules

Keep installation or usage instructions practical and repository-specific.

Include instructions such as:

- Import the plugin's 2Pack when required.
- Install or deploy the OSGi bundle in iDempiere.
- Restart or refresh iDempiere when needed.
- Configure process access, menu entries, windows, roles, or related records when evidenced by the plugin.

Do not include build commands in this section.

## Extra Links Rules

Only include `## Extra Links` when there are real, useful links from the repository or user-provided context.

Do not include placeholder text.

## Style

- Always write in English.
- Use concise technical prose.
- Prefer precise headings over decorative separators.
- Use Markdown tables for summaries.
- Keep class names, table names, parameters, and bundle IDs in backticks.
- Keep code snippets minimal and only when they improve usage instructions.

## Quality Checklist

Before finishing a README update, confirm:

- The README is in English.
- The structure follows the required section order.
- `Commands` is absent.
- Target platform components are absent.
- `IDEMPIERE_REPOSITORY` is absent.
- Java and iDempiere versions are inferred from project metadata when available.
- Additional prerequisites exclude the base dependency ignore list.
- `Features/Documentation` starts with a `Source Structure` subsection based on actual `src` folders/packages.
- `Features/Documentation` reflects actual code, annotations, model classes, and 2Pack content.
- Placeholder text has been removed.
- `Extra Links` is omitted when empty.
