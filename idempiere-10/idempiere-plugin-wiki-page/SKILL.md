---
name: idempiere-plugin-wiki-page
description: Create or normalize an iDempiere Available Plugins wiki page from a repository README, validating claims against the plugin code, OSGi metadata, 2Pack content, Git history, and the established iDempiere wiki style.
---

# iDempiere Plugin Wiki Page

## Purpose

Create or update an English MediaWiki page for an iDempiere plugin. Use the repository README as the editorial starting point, then verify factual claims against the repository before producing publication-ready wikitext.

Use this skill for pages listed in `Category:Available Plugins`. Use `idempiere-plugin-readme` when the requested deliverable is the repository README itself.

## Evidence Rules

- Preserve correct README content; do not rewrite or rediscover it without a reason.
- Verify the bundle ID, version, dependencies, registered services, functional components, and Java level from `META-INF/MANIFEST.MF`, project metadata, and source code.
- Inspect relevant `.process`, `.event`, `.callout`, `.model`, `.form`, `.component`, and service packages to confirm the documented behavior.
- Inspect every 2Pack, PackOut, migration, or dictionary artifact mentioned by the page. Distinguish an artifact present in the repository from one proven installed in a runtime.
- Use `git remote -v` for the source URL when available. Do not retain a stale README URL when the configured remote contradicts it.
- Use `git shortlog -sne --all`, `.mailmap`, commit trailers, and explicit source credits to identify contributors and candidate maintainers. Merge aliases only when the evidence supports that they are the same person. Do not promote a commit author to maintainer without explicit project or user evidence, and do not infer sponsorship from copyright alone.
- Treat a user-provided maintainer, sponsor, status, or tested version as authoritative for the requested page unless repository evidence directly conflicts with it; surface any conflict before publication.
- Do not claim `Tested with release X`, production readiness, successful installation, deployment, or runtime validation from a manifest version, target platform, build, or source inspection alone. Use `Targeting iDempiere X` when only compatibility metadata is available.
- Omit unsupported claims or label them conservatively. Keep unresolved material facts in a short `Questions or pending verification` list outside the wikitext draft.

## Workflow

1. Locate the repository root and check for workspace instructions before reading or modifying files.
2. Read the main README first and identify the proposed page title, maintainer, sponsor, status, license, source, documentation link, description, features, requirements, installation, configuration, and limitations.
3. Inspect only the code and metadata needed to verify those claims. Prefer focused searches over a full code walkthrough when the README is current.
4. Compare the intended page with existing pages in the same wiki family or category when they are accessible. Match their concise header, heading hierarchy, lists, `wikitable` tables, and link conventions without copying stale facts.
5. Read [references/wiki-page-template.wikitext](references/wiki-page-template.wikitext) and adapt it to the plugin. Omit conditional sections that do not apply; add one plugin-specific functional section when it makes the page easier to use.
6. Produce a complete `.wikitext` draft and a short edit summary. If updating an existing page, also provide a focused diff or clear change list.
7. Validate balanced MediaWiki tables and HTML-like tags, valid link syntax, the final category line, and the absence of unresolved placeholders.
8. Preview the page in the wiki before saving. Creating, editing, moving, or publishing a wiki page is an external change: do it only when the user explicitly asks for that action. A request to draft, review, or normalize content does not authorize publication.

## Naming and Category

- For Casa del Software repositories using the established family, use `Plugin: CDSoftware <Functional Name>`.
- Preserve an existing valid wiki title when normalizing an already published page unless the user asks to rename it.
- Use spaces and reader-facing words in the title; do not expose the Java bundle ID as the page title unless that is the established public name.
- End Casa del Software pages with `[[Category:Available Plugins|CDSoftware <Functional Name>]]` so they sort under `C`.
- For other maintainers, use `[[Category:Available Plugins|<sort key>]]` with the public plugin name as the sort key.

## Standard Page Structure

Keep this order for consistent pages:

1. Header bullets: `Maintainer`, `Sponsors` when applicable, `Status`, `License`, `Sources`, and `Documentation` when distinct from the source link.
2. `Description`.
3. `Features`.
4. A plugin-specific functional section when needed, such as supported events, processes, reports, integrations, or windows.
5. `Requirements`.
6. `Installation`.
7. `Configuration` or `Usage`, whichever matches the plugin.
8. Fallback behavior, limitations, compatibility notes, or troubleshooting only when supported and useful.
9. `Documentation and source code`.
10. `Category:Available Plugins` with the appropriate sort key.

Do not add empty sections. Keep implementation details out of the opening description. Use class names, configuration keys, paths, and event codes only where administrators need them.

## MediaWiki Style

- Write in clear English.
- Use `== Heading ==` and `=== Subheading ===`.
- Use `*` for unordered lists and `#` for ordered steps.
- Use `[https://example.org Label]` for external links; do not use Markdown link syntax.
- Use `'''Label:'''` for header labels and `<code>value</code>` for inline technical names.
- Use `<pre>...</pre>` for configuration lines or commands that users must copy.
- Use `{| class="wikitable" ... |}` for structured comparisons or mappings.
- Keep paragraphs short and administrative instructions precise.
- Do not include the page title as a heading inside the wikitext; MediaWiki renders it automatically.

## Output Contract

Return:

1. The proposed wiki title.
2. The evidence checked and any material discrepancy.
3. The complete wikitext draft or a focused diff for a small update.
4. A short edit summary suitable for the wiki form.
5. The publication state: draft only, previewed, or saved. Never report a page as saved without direct evidence.
