# Antigravity Skills Repository

Welcome to the **Antigravity Skills Repository**! This repository serves as a centralized hub for sharing, managing, and developing reusable custom skills for the Antigravity AI coding assistant. 

---

## Repository Structure & Guidelines

To maintain a clean, high-quality, and easily maintainable codebase, all contributions must adhere to the following rules:

1. **Dedicated Folders**: Every skill must be placed in its own dedicated directory at the root of this repository.
2. **Metadata & Description**: Each skill must contain a `SKILL.md` file with a YAML frontmatter section detailing its `name` and `description` (e.g., specifying when it activates and its primary capability).
3. **Focused Scope**: Avoid broad or overlapping skills. Each skill should address a single, reusable capability.

---

## Available Skills

Below is a summary of the custom skills currently available in this repository:

| Skill Directory | Description | Primary Purpose |
| :--- | :--- | :--- |
| [`idempiere-local-postgres`](idempiere-local-postgres/SKILL.md) | Safely diagnoses iDempiere PostgreSQL databases. | Enforces read-only access by default and a double confirmation for writes. |
| [`idempiere-migration-review`](idempiere-migration-review/SKILL.md) | Audits iDempiere 12 module proposals. | Validates models, DDL, Application Dictionary and OSGi consistency. |
| [`idempiere-model-designer`](idempiere-model-designer/SKILL.md) | Designs iDempiere 12 module data models. | Defines entities, relationships and functional architecture. |
| [`idempiere-pipo-integrity-review`](idempiere-pipo-integrity-review/SKILL.md) | Performs PackOut/PIPO preflight validation. | Checks dictionary types and dependencies before export. |
| [`idempiere-plugin-compiler`](idempiere-plugin-compiler/SKILL.md) | Builds iDempiere OSGi plugins. | Uses the repository target-platform builder and reports artifacts. |
| [`idempiere-plugin-component-developer`](idempiere-plugin-component-developer/SKILL.md) | Develops internal plugin components. | Implements processes, callouts, validators and factories. |
| [`idempiere-plugin-designer`](idempiere-plugin-designer/SKILL.md) | Designs iDempiere 12 plugin implementations. | Translates functional designs into Java and OSGi specifications. |
| [`idempiere-plugin-manual-generator`](idempiere-plugin-manual-generator/SKILL.md) | Generates functional plugin manuals. | Produces English user manuals and test guides from code and metadata. |
| [`idempiere-plugin-readme`](idempiere-plugin-readme/SKILL.md) | Standardizes plugin repository documentation. | Creates English README files from actual OSGi project contents. |
| [`idempiere-plugin-test-developer`](idempiere-plugin-test-developer/SKILL.md) | Develops tests for plugin components. | Creates unit tests, mocks and isolation strategies. |
| [`jenkinsfile-developer`](jenkinsfile-developer/SKILL.md) | Maintains iDempiere 12 Jenkins pipelines. | Standardizes compilation and README publishing without host-specific paths. |
| [`skill-architect`](skill-architect/SKILL.md) | Designs focused reusable skills. | Scaffolds capabilities not already covered by the library. |
| [`skill-reviewer`](skill-reviewer/SKILL.md) | Reviews Antigravity skills before adoption. | Validates naming, scope, activation and structure. |

---

## How to Load Skills

To use these skills with your Antigravity assistant, ensure they are copied or linked into your workspace's skill library path (typically `.agents/skills/` under your project root) or the global user configuration path.

---

*Copyright &copy; 2026 [Casa del Software](https://www.casadelsoftware.com). Licensed under GPL 2.*
