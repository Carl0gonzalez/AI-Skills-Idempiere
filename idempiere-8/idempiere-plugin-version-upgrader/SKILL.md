---
name: idempiere-plugin-version-upgrader
description: Upgrade existing iDempiere OSGi plugin repositories between major iDempiere releases, align version-specific Java, Maven/Tycho, OSGi, target-platform, and PostgreSQL code, then compile and verify the upgraded plugins locally. Use only for version migrations of existing plugins; do not use for feature development, server upgrades, database migrations, README-only edits, or ordinary builds without a version change.
---

# iDempiere Plugin Version Upgrader

Upgrade an existing plugin with the smallest compatible change set and produce local evidence that every updated bundle compiles against the requested iDempiere release.

## Required references

- Read [references/version-baseline.md](references/version-baseline.md) before choosing Java, PostgreSQL, Maven/Tycho, target-platform, or plugin versions.
- Read only the source-to-target sections that apply in [references/compatibility-checks.md](references/compatibility-checks.md).

## Scope boundaries

- Preserve plugin behavior unless the target release makes a compatibility change necessary.
- Treat plugin upgrade, iDempiere server upgrade, production database migration, documentation refresh, and deployment as separate tasks.
- Do not add features, redesign the plugin, install it on a server, modify a production database, commit, push, or publish unless the user requested that action.
- Preserve unrelated working-tree changes and existing release branches. Do not infer that `master` is a released iDempiere version.

## Review and branch gates

1. Perform discovery read-only. Inspect the current repository and target release before proposing edits.
2. Present the source and target baselines, compatibility findings, exact files expected to change, intended branch name, build command, and PostgreSQL validation plan. Obtain explicit approval before editing.
3. Fetch the remote and verify that local `master` matches the intended remote base. Create the upgrade branch from that `master`; use the repository's established version-branch convention, normally the target semantic release such as `12.0.0`.
4. Apply and verify the upgrade only on that branch. Do not edit `master` directly.
5. Present the final diff, commits if authorized, build results, PostgreSQL evidence, and remaining limitations for review.
6. Push the branch and create a PR targeting `master` only after explicit approval of the reviewable result. PR creation is not implied by approval to edit or compile.

If the target branch already exists, inspect its base and history. Reuse it only when it represents the same upgrade and can be reconciled without losing work; otherwise report the conflict before editing.

## Establish the baseline

1. Inspect Git status, branches, tags, remotes, recent history, and repository instructions.
2. Determine the source release from release branches, `MANIFEST.MF`, POMs, feature metadata, target definitions, and build files. Report conflicts instead of silently choosing one value.
3. Determine the requested target release. For a released version use official `idempiere/idempiere` branch `release-N`; use `master` only when the user explicitly targets the development release.
4. Record the target branch commit and derive its `revision`, JDK level, Tycho version, execution environment, target-platform units, JDBC driver, and supported PostgreSQL range. Verify volatile facts from current official sources.
5. Confirm that the local JDK and Maven actually used by the build match the target by recording `java -version`, `javac -version`, and `mvn -version` or `./mvnw -version`.

## Inventory before editing

Inventory every bundle, fragment, feature, P2 site, test project, target-platform project, and custom local dependency. Inspect at least:

- all `META-INF/MANIFEST.MF`, `pom.xml`, `feature.xml`, `category.xml`, `.target`, `.tpd`, `build.properties`, `plugin.xml`, `OSGI-INF`, `Jenkinsfile`, Maven wrapper, and repository build scripts;
- Java imports and references to iDempiere APIs, removed JDK modules, internal JDK APIs, OSGi services, JDBC APIs, and bundled third-party JARs;
- SQL embedded in Java, SQL files, Jasper reports, XML/2Pack content, views, functions, triggers, and migration scripts;
- generated `X_`/`I_` models and their relationship to Application Dictionary changes.

Build a dependency order from `Require-Bundle`, `Import-Package`, feature membership, and reactor modules. Include tests and fragments belonging to an updated bundle.

## Apply the upgrade

Align only metadata that the repository actually uses:

- Maven revision/parent and module list;
- OSGi `Bundle-Version`, `Bundle-RequiredExecutionEnvironment`, `Require-Bundle`, `Import-Package`, `Export-Package`, `Fragment-Host`, and DS metadata;
- feature, P2 category/repository, product, target-platform, and CI/build configuration;
- source code affected by removed, moved, deprecated-with-replacement, or behaviorally changed APIs;
- SQL and JDBC code affected by the target PostgreSQL/JDBC behavior.

Do not perform a blind repository-wide version replacement. Preserve independent library and product versions. Follow the repository's established artifact-version convention when it differs from the iDempiere release number.

For generated model classes, update from the target Application Dictionary when available. Do not hand-edit generated models merely to hide a schema mismatch.

## Java and OSGi verification

Apply the installed `idempiere-plugin-compiler` skill for builder discovery, dependency ordering, command execution, and artifact reporting; the upgrade rules and review gates in this skill still control the surrounding workflow.

1. Use the repository's documented builder and target platform. Prefer its Maven wrapper when present.
2. Build custom dependencies first or use the documented multi-module reactor. Pass the target revision property when the generated POM requires it.
3. Run the complete local verification goal, normally `verify`, without skipping compilation or tests. Compile every updated plugin, fragment, feature, and test bundle.
4. On failure, classify the first relevant cause: JDK language/API, iDempiere API, OSGi resolution, target-platform dependency, generated model, third-party library, or test/runtime behavior.
5. Make the smallest source-compatible correction and repeat the full affected build. Do not weaken compiler or OSGi checks to obtain success.

A successful build proves only that the compiled paths resolve against the selected JDK and target platform. It does not prove deployment, activation, PackIn success, or PostgreSQL runtime behavior.

## PostgreSQL verification

Compilation cannot validate SQL semantics. Always perform the static SQL/JDBC review in the applicable compatibility reference.

When the plugin contains database-specific code, validate it against a local or disposable PostgreSQL instance within the target release's officially supported range, using the recommended version when the documentation names one. Prefer the repository's test database and existing integration tests. Otherwise use an isolated database initialized for the target iDempiere release.

- Record `SHOW server_version` and the JDBC driver version.
- Run meaningful database-backed tests for affected queries, parameter bindings, views, functions, and migrations.
- Keep exploratory checks read-only. Apply schema/data changes only to an isolated test database and wrap reversible probes in a transaction with rollback.
- Never run upgrade SQL or PackIn content against production as part of this skill.
- If no suitable target database is available, complete the static review and report PostgreSQL runtime compatibility as **not verified**. Never convert static inspection or compilation into a PostgreSQL pass.

## Completion gate

The upgrade is ready for final review only when:

- target-version metadata is internally consistent;
- all updated bundles and their tests compile locally with the target JDK and target platform;
- `git diff --check` passes;
- SQL/JDBC review is complete;
- database-backed validation passes when database-specific behavior changed or the task provides a suitable test database;
- remaining warnings, untested runtime paths, and unavailable infrastructure are stated precisely.

## Report

Report:

- repository, source release, target release, upgrade branch, base `master` commit, and target iDempiere commit;
- verified Java, Maven/Tycho, PostgreSQL, and JDBC versions;
- files and compatibility fixes made;
- exact build/test commands and Maven/Tycho result;
- generated JARs or P2 artifacts with paths;
- PostgreSQL checks executed and their result;
- unresolved incompatibilities and the exact validation boundary;
- whether the branch is local, pushed, or represented by a PR targeting `master`.
