---
name: skill-architect
description: Creates new focused Antigravity skills when a task requires reusable capabilities that are not already covered by existing skills in the current workspace or user skill library.
---

# Purpose

This skill designs and scaffolds new Antigravity-compatible skills only when a reusable capability is missing.

It should be activated when the user asks Antigravity to:

- create a new skill
- scaffold a reusable workflow
- convert a repeated prompt into a skill
- package a task pattern into a skill folder
- create helper skills for other tasks

This skill must avoid creating duplicate, vague, or one-off skills.

# Operating principles

- Prefer reusing an existing skill over creating a new one.
- Prefer small, single-purpose skills over broad multi-domain skills.
- Create a skill only if the capability is reusable across tasks, repositories, or sessions.
- If the need is specific to one single task and unlikely to repeat, do not create a skill.
- Always optimize for discoverability: the name and description must make activation obvious.
- Keep the generated skill understandable by a future human maintainer.

# Before creating a skill

Perform this checklist:

1. Infer the missing reusable capability.
2. Search the currently available skills by name and description.
3. Check for overlap, duplication, or composition opportunities.
4. Decide whether the task needs:
   - a new skill
   - an update to an existing skill
   - a one-time answer with no skill
5. If the request is ambiguous, ask for scope clarification before generating anything.

# Skill creation criteria

Create a new skill only if most of these are true:

- The user is likely to need the capability again.
- The workflow has stable steps.
- The workflow benefits from explicit constraints or examples.
- The workflow would be improved by local resources, examples, or scripts.
- The capability is narrow enough to describe in one sentence.

Do not create a skill if any of these are true:

- The task is a one-off artifact.
- The requested capability overlaps heavily with an existing skill.
- The scope is too broad, such as "do anything with databases".
- The behavior depends mostly on ad hoc judgment and not on a repeatable procedure.

# Naming rules

Generated skill names must be:

- lowercase
- hyphen-separated
- short and specific
- capability-oriented, not project-oriented

Good examples:

- idempiere-migration-review
- sql-patch-safety-check
- release-note-builder
- rest-endpoint-scaffold

Bad examples:

- helper
- my-skill
- enterprise-devops-super-agent
- project-finalizer

# Description rules

The `description` field must:

- state when the skill should activate
- describe the capability in one sentence
- mention the relevant trigger context
- avoid vague wording like "helps with tasks"

Good example:
`Reviews SQL migration scripts for destructive changes, naming issues, and rollback gaps before execution.`

Bad example:
`Useful for SQL work.`

# Folder structure rules

Unless there is a reason not to, generate this structure:

<skill-name>/

- SKILL.md

Add optional folders only when justified:

- examples/ when a few-shot example will materially improve outputs
- resources/ when templates, reference text, or schemas are needed
- scripts/ when deterministic validation or scaffolding is required

Never create empty folders.

# Required content for generated SKILL.md

Every generated skill must include:

1. Frontmatter:
   - name
   - description

2. Purpose section:
   - what the skill does
   - when it should be used

3. Activation guidance:
   - phrases or task types that should trigger it

4. Constraints:
   - what it must not do
   - safety boundaries
   - scope limits

5. Workflow:
   - ordered steps
   - decision points
   - expected outputs

6. Output contract:
   - what the agent should produce

7. Optional examples:
   - short trigger examples if helpful

# Generation workflow

When asked to create a new skill, follow this exact sequence:

1. Summarize the requested reusable capability in one sentence.
2. Decide whether a skill should be created.
3. If not, explain why and continue without creating one.
4. If yes, propose:
   - skill name
   - description
   - target path
   - file structure
5. Generate the full contents.
6. Ensure the skill is narrow, non-duplicative, and reusable.
7. Tell the user how to reload skills in Antigravity.

# Output contract for this skill

When this skill creates another skill, return:

- Skill name
- Why it should exist
- Why it is not a duplicate
- Folder path
- Files created
- Full file contents

# Special rule for meta-skills

If asked to generate a skill that itself creates or manages other skills:

- enforce narrower scope
- require duplication checks
- require explicit naming and description quality
- prevent recursive over-generation of helper skills
- prefer one "architect" skill and one "reviewer" skill rather than a chain of autonomous meta-skills

# Anti-patterns

Never generate skills that:

- claim to solve all development tasks
- auto-create many skills without user confirmation
- have names unrelated to their behavior
- rely on hidden assumptions about the repository
- omit activation criteria
- omit constraints
- create scripts when plain instructions are enough

# Example triggers

Activate this skill for prompts like:

- "create a reusable skill for reviewing iDempiere migration scripts"
- "turn this repeated deployment workflow into a skill"
- "make a skill that can scaffold REST endpoint templates"
- "create a meta-skill that can generate other focused skills"
