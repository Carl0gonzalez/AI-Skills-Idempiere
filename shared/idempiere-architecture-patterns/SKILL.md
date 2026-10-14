---
name: idempiere-architecture-patterns
description: Guides implementation, modification, review, and refactoring of iDempiere plugins and integrations by choosing the simplest architecture supported by the project's actual version, scaffold, Application Dictionary, OSGi conventions, lifecycle, and tests. Use for iDempiere Java architecture decisions and code changes; compose with specialized model, migration, testing, build, or upgrade skills when those workflows dominate.
---

# iDempiere Architecture Patterns

Solve each requirement with the least complexity that correctly follows the actual iDempiere architecture. Patterns are tools, not goals.

For new plugins: **scaffold first, customs second, existing project conventions third, new structure last**.

## Boundaries

- Inspect before designing. The target workspace and its exact version outrank generic examples or remembered APIs.
- Preserve existing factories, annotations, DS descriptors, test fragments, builders, packages, and custom overlays when they are valid.
- Do not create a Service, Interface, Factory, Adapter, DTO, Mapper, Repository, Strategy, additional handler, or module unless it solves an observed need: real reuse, non-trivial testability, an external boundary, multiple implementations, a genuine extension point, problematic coupling, or established project convention.
- Do not edit generated `I_*`/`X_*` sources; find their generator or Application Dictionary source.
- Do not modify core or a shared scaffold for a plugin-specific need. Treat scaffold improvement as a separate, explicitly justified change.
- Preserve authorization boundaries: implementation does not imply database writes, deployment, PackIn, commit, push, or publication.

## Select repository context

- **Core:** the target core AGENTS.md and its task skills govern contribution rules. Read them from the actual checkout; central core/ guidance is a fallback reference, not a substitute for newer repository rules. Do not author core migration scripts, AD IDs/UUIDs or generated models. PostgreSQL and Oracle are required.
- **Plugin:** preserve the plugin scaffold, Entity Type, supported databases and registration mechanism. Core Centralized-ID rules are not automatically a ban on authorized private-plugin migrations.
- **Environment:** use the actual release's Java/Maven/OSGi requirements; do not treat an installed global skill as proof of release compatibility.

## Choose the operating mode

### Implement mode

Use when asked to create, implement, add, integrate, migrate, or extend.

1. Establish the actual baseline and conventions.
2. Classify the requirement and choose the smallest suitable mechanism.
3. Implement the minimum coherent change, including necessary registration and tests.
4. Build with the repository's real Maven/Tycho/target-platform workflow.
5. Review the final architecture and state exactly what runtime behavior remains unverified.

### Review mode

Use when asked to review, audit, diagnose, analyze, or refactor.

- Inspect without rewriting by default.
- Report the concrete problem, impact, architectural cause, and smallest recommended correction.
- Separate defects from optional improvements.
- Do not turn a local correction into package reorganization or broad refactoring unless required.

## Evidence-driven discovery

Before a relevant decision, determine as applicable:

- iDempiere release, Java, Maven/Tycho, target platform, and PostgreSQL/JDBC baseline;
- affected bundles, fragments, features, `MANIFEST.MF`, `build.properties`, POMs, DS registrations, Jenkins/build scripts, and repository instructions;
- scaffold/template locations, `custom`/`customs`/overlay mechanisms, and one or two recent plugins created from them;
- existing factories, annotations, OSGi services, extension points, models, processes, handlers, callouts, tests, and core equivalents;
- Application Dictionary options, document lifecycle, transaction ownership, concurrency, idempotency, and distribution through PackOut/PackIn.

Search likely scaffold names including `scaffold`, `scafold`, `plugin-template`, `templates`, `tools`, `dev`, and `sources`. If scaffold and recent plugins differ, investigate before choosing.

Use this source order: current project code, similar local implementations, exact-version core and tests, official documentation, then general knowledge.

Read [decision-guide.md](references/decision-guide.md) when selecting components, layers, or patterns. Read [review-checklist.md](references/review-checklist.md) before finalizing a non-trivial implementation or architectural review. Read [scenarios.md](references/scenarios.md) when examples help calibrate complexity.

## Architecture selection

Classify internally:

- **Simple:** local rule, one entry point, no external boundary or significant concurrency. Prefer AD, direct core/model API, or a small change in the existing component.
- **Medium:** multiple rules or entry points, meaningful reuse, important transaction, or cross-cutting behavior. A focused Service or event component may be justified.
- **Complex:** external integration, retries, idempotency, concurrency, distributed consistency, or multiple plugins/systems. Ports/adapters, controlled retry, correlation, or Outbox may be justified only by those needs.

Try solutions in this order:

1. Application Dictionary or configuration.
2. Existing API, model, factory, annotation, or extension point.
3. Small change in the appropriate `M*` model or existing component.
4. Callout, EventHandler, or `SvrProcess` according to the entry point.
5. Service for genuinely shared or non-trivial logic.
6. Interface/Strategy for multiple real implementations.
7. Adapter/Port for a relevant external boundary.
8. Core modification only as a last resort.

## iDempiere invariants

- **AD:** prefer metadata for fields, validation, display/read-only/mandatory logic, references, workflows, parameters, preferences, access, and configurable values.
- **PO models:** `I_*` is the generated contract, `X_*` generated persistence, and `M*` domain behavior. Prefer PO, `MTable`, `Query`, and core APIs over direct SQL.
- **Entry points:** Callout is interactive UX; EventHandler enforces cross-entry behavior; `M*` owns natural invariants; `SvrProcess` orchestrates explicit operations; REST maps transport; Scheduler triggers work.
- **Documents:** use `processIt()`, `DocumentEngine`, and valid actions. Never simulate completion with `setDocStatus("CO")` plus save.
- **Transactions:** preserve the owning `trxName`; avoid hidden commits, arbitrary nested transactions, `null` transaction mixing, and partial persistence.
- **OSGi:** follow the bundle's proven DS/XML/annotation and factory convention. Do not add a parallel registry or duplicate a scaffold factory.
- **Queries:** bind parameters. Prefer `Query` where it expresses the intent; use direct SQL only when it has a concrete benefit.
- **Configuration:** keep functional configuration in AD, technical configuration in the appropriate system mechanism, and secrets in protected runtime configuration. Avoid database-specific numeric IDs.
- **Integrations:** keep protocol mapping at the boundary and business rules in reusable domain/application logic when reuse or complexity warrants it. Consider idempotency, retries, correlation, locking, duplicates, and Outbox proportionally.
- **Performance:** check obvious N+1 queries, unbounded scans, queries or external calls inside loops, bulk `saveEx()`, and excessive logging without premature optimization.
- **Errors/logging:** preserve causes, use compatible iDempiere exceptions and logging, never swallow exceptions or log secrets, and never use `System.out` in production code.

## Compatibility and collateral impact

Search callers of changed APIs and assess other documents, clients/orgs, currencies and accounting schemas. Prefer overloads/deprecation over removing public or protected signatures. Translate user-facing messages through AD_Message/Msg; follow the target license/header and serialVersionUID convention. Do not use a batch API merely because it exists in another release; verify lifecycle hooks and signatures locally.

## Testing and completion

Use the existing test fragment and declared framework. Prefer pure unit tests for isolated rules, domain tests next, and integration/framework tests when behavior genuinely depends on iDempiere or the database. Extract logic only when that reduces real coupling and does not create a ceremonial layer.

A build proves compilation and tested paths, not deployment, OSGi activation, PackIn, database behavior, or UAT. Report these boundaries separately.

Compose rather than duplicate specialized workflows:

- use the available iDempiere model/design skill for substantial schema design;
- use component-development guidance for detailed process/callout/validator implementation;
- use the existing test, compiler, quality-gate, migration-review, or version-upgrade skill when that is the main task.

## Output

Lead with the selected mechanism and why it is the simplest compatible option. Then provide or implement the scoped change, tests/build evidence, affected files, architectural review findings, and remaining runtime limitations. For reviews, prioritize actionable defects and minimum corrections over generic pattern commentary.
