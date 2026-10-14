---
name: skill-reviewer
description: Reviews AI-agent skills for naming quality, activation clarity, scope control, duplication risk, folder structure, and instruction quality before adoption.
---

# Purpose

This skill reviews an agent-compatible skill before it is accepted into a workspace or user skill library.

It should be activated when the user asks to:

- review a new skill
- validate a generated SKILL.md
- check whether a skill is too broad or duplicated
- improve a skill description for better activation
- audit a skill folder before committing it

This skill does not create final production artifacts by itself unless the user explicitly asks for a corrected rewrite.

# Review principles

- A skill should do one job well.
- A skill description should make activation likely for the right tasks and unlikely for the wrong ones.
- A skill should be reusable, understandable, and narrow.
- A skill should not duplicate another skill unless the distinction is explicit and justified.
- Instructions should be operational, not vague.
- Scripts and extra folders must be justified by real need.

# Review checklist

Review the target skill against all of the following:

1. Naming

- Is the name lowercase and hyphen-separated?
- Is the name specific to the capability?
- Is the name short enough to remember?
- Does the name avoid project-specific jargon unless the domain requires it?

1. Description quality

- Does the description clearly say when the skill should trigger?
- Does it describe the capability in one sentence?
- Does it avoid vague wording like "helps with tasks"?
- Does it include relevant trigger terms?
- Does it avoid sounding too broad?

1. Scope control

- Is the skill focused on one reusable capability?
- Is it trying to do too many unrelated things?
- Could it be split into two smaller skills?
- Is it actually a one-off task disguised as a skill?

1. Duplication risk

- Does another known skill already cover the same workflow?
- Is the distinction between this skill and similar ones explicit?
- Should this be a revision of an existing skill instead?

1. Instruction quality

- Are there clear steps?
- Are constraints and safety boundaries present?
- Does the workflow specify inputs and outputs?
- Are decision points explicit?
- Are anti-patterns or failure cases covered where needed?

1. Folder structure

- Does the skill contain SKILL.md?
- Are examples, resources, or scripts included only when justified?
- Are there empty or unnecessary folders?
- Are supporting files named clearly?

1. Activation behavior

- Would a matching engine likely activate this skill from the description?
- Could the description produce false positives?
- Could important trigger phrases be missing?
- Is the skill too generic to be reliably selected?

# Required output format

When reviewing a skill, always return these sections:

## Review result

One of:

- approve
- approve with minor fixes
- revise before use
- reject as duplicate or too broad

## Findings

A concise bullet list of issues and strengths.

## Suggested fixes

Specific edits, not generic advice.

## Revised frontmatter

If changes are needed, provide improved:

- name
- description

## Structure advice

State whether the current folders are sufficient, excessive, or incomplete.

## Final recommendation

State whether the skill should be:

- kept as-is
- rewritten
- split
- merged with another skill
- not created at all

# Review workflow

Follow this exact process:

1. Read the skill name, description, and folder contents.
2. Infer the intended capability in one sentence.
3. Check for over-breadth or one-off behavior.
4. Check likely activation quality from the description.
5. Check duplication risk against nearby or known skills.
6. Review instruction quality and file structure.
7. Return a decision with concrete edits.
8. If the user requests it, provide a rewritten SKILL.md.

# Rewriting rules

If asked to rewrite a skill:

- preserve the original intent
- reduce ambiguity
- tighten scope
- improve trigger wording
- remove unnecessary folders or scripts
- keep the skill instruction-first unless deterministic tooling is essential

# Anti-patterns

Flag these aggressively:

- names like `helper`, `assistant`, `automation`, or `toolkit`
- descriptions that do not say when to activate
- "do everything" skills
- hidden assumptions about repository layout
- instructions with no output contract
- multiple unrelated workflows in one skill
- scripts added without necessity
- examples that contradict the instructions

# Example trigger prompts

Activate this skill for prompts like:

- "review this skill before I commit it"
- "is this SKILL.md too broad?"
- "improve the activation description of this skill"
- "check whether this new skill duplicates another one"
- "rewrite this skill so the agent triggers it more reliably"
