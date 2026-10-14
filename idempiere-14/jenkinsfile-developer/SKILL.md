---
name: jenkinsfile-developer
description: Create or update Jenkins pipelines for iDempiere 14 plugins using the actual source revision, supported builder and existing job conventions. Use for CI builds and requested documentation archiving.
---

# iDempiere 14 Jenkins pipelines

Read the target Jenkinsfile, manifests, POM/wrapper, target platform and job configuration. Read [references/idempiere14-baseline.md](references/idempiere14-baseline.md) for the verified development baseline. Do not copy a release-13 image or invent a release-14 image/branch.

## Builder and scope

- Verify the actual official image/tag/digest or repository-approved builder, source revision, JDK and target platform. Prefer a pinned source revision for reproducibility; master is a moving development branch.
- If no compatible container builder is available, use the configured host/wrapper build or report the missing infrastructure. Never silently change dependencies or artifact versions to make an older builder pass.
- Preserve existing stages, credentials bindings, timeouts and workspace conventions. Do not add libraries, Java changes, job configuration or new publishing services outside the request.
- Do not print secrets, use hardcoded host mounts or derive dependencies from example plugin names. Discover actual manifest dependencies and artifact paths.

## Implementation

1. Define the minimal requested stages. Set currentBuild.description with safe existing fields when useful; rawBuild/job-description changes require evidence that Jenkins policy allows them.
2. Reuse the documented plugin builder or wrapper command and target-platform checkout. Run dependencies in the required order, explicitly enable requested tests and inspect fresh reports/counts.
3. Archive actual generated artifacts; report compilation separately from OSGi/runtime validation. Do not claim plugin installation from artifact creation.
4. Add README HTML archiving only when requested or established in the job. Reuse its design/parser/publishHTML convention and verify plugin availability. HTML-escape untrusted Markdown; avoid introducing a regex parser that treats raw HTML as trusted.
5. For embedded Python/Groovy, validate Groovy string/backslash handling and f-string braces. Do not include incomplete placeholders or speculative credentials. Use Jenkins lint or an existing test harness where available.
6. Review failure paths, post actions, resource timeouts and branch conditions. Publication/deployment stages require authorization for those actions, not merely pipeline editing.

## Output

Return the changed Jenkinsfile, selected source/JDK/builder evidence, dependency/artifact paths, validation performed and unavailable Jenkins/runtime checks. Changing this skill does not provision Jenkins or publish any artifact.
