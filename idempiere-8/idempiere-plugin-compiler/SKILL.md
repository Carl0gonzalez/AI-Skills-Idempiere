---
name: idempiere-plugin-compiler
description: Builds an iDempiere OSGi plugin with the repository's target-platform builder, resolving local plugin dependencies and reporting generated artifacts.
---

# Purpose

Build iDempiere 8.2 OSGi plugins reproducibly using the repository target platform and the official source image `idempiereofficial/idempiere:source-release-8.2` when the build runs in Docker or Jenkins.

# Activation Guidance

Use this skill when the user asks to build, compile, package, or diagnose compilation failures for an iDempiere plugin.

# Constraints

- Inspect the repository's build documentation, `Jenkinsfile`, target platform, and `META-INF/MANIFEST.MF` before choosing a command.
- Do not assume a builder path, shell, operating system, iDempiere version, or plugin name.
- For Docker or Jenkins builds, use only `idempiereofficial/idempiere:source-release-8.2`; do not replace it with a private or third-party image.
- Build dependencies in manifest dependency order. When cycles exist, use the repository's documented multi-plugin build command.
- Do not delete build outputs or alter dependency metadata unless the user explicitly requests it.
- Never expose credentials, tokens, or repository URLs containing secrets.

# Scope and evidence

For core builds use the actual core headless-build/unit-test guidance rather than applying a plugin builder to the core reactor. Verify the release JDK and wrapper/target metadata. Compilation does not prove test execution, DS activation, PackIn or database compatibility.

If tests are requested, enable them through the documented builder and inspect new report timestamps/counts. The reference core ./mvnw verify skips tests unless -DskipTests=false; do not assume plugin builders behave the same way. Preserve unrelated outputs and use clean builds in isolated review workspaces when switching revisions.

# Workflow

1. Identify the plugin bundle, its `MANIFEST.MF`, the target-platform directory, and documented build command.
2. Read `Require-Bundle` and applicable `Import-Package` entries to identify custom local dependencies.
3. Confirm the available builder command and, for containerized builds, verify that Jenkins uses `idempiereofficial/idempiere:source-release-8.2`.
4. Run the build from the documented target-platform directory, passing dependent plugin paths before the requested plugin when required.
5. Report the command, build result, relevant errors, and generated JAR files with timestamps.

# Output Contract

Return the exact command executed, the build result (including the relevant Maven/Tycho summary or failure), and the generated artifacts with their paths and modification times.
