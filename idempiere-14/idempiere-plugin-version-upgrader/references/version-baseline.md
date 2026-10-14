# Version baseline and source precedence

Use current official evidence for every upgrade. The version matrix below is a dated orientation, not a substitute for inspecting the target branch.

## Source precedence

1. The exact official target branch or tag in `https://github.com/idempiere/idempiere`.
2. The version section in the official [Migration Notes](https://wiki.idempiere.org/en/Migration_Notes).
3. Current official [development prerequisites](https://wiki.idempiere.org/en/Install_Development_Prerequisites), [headless build guide](https://wiki.idempiere.org/en/Building_iDempiere_without_Eclipse), and [plugin Maven build guide](https://docs.idempiere.org/docs/basic-development/plugin-development/plugin-maven-build).
4. Repository-specific build documentation and target-platform configuration, after checking that it actually targets the requested release.

When sources conflict, prefer the exact target branch for build properties and the migration notes for behavioral changes. Report the conflict and do not silently use a current requirement for an older release.

## What to derive from the target branch

Inspect `org.idempiere.parent/pom.xml`, target-platform definitions, database providers, Maven wrapper, and relevant manifests. Record:

- `<revision>`, `<jdk.version>`, compiler source/target/release, and execution environment;
- Tycho and Maven wrapper versions;
- P2/Eclipse target repositories and installable units;
- PostgreSQL JDBC driver and JDBC URL properties;
- release-specific package/bundle moves.

Useful raw parent POM pattern:

`https://raw.githubusercontent.com/idempiere/idempiere/release-N/org.idempiere.parent/pom.xml`

## Verified orientation snapshot

Verified from official sources on 2026-09-15:

| iDempiere release | Official branch | JDK in parent POM | Tycho in parent POM |
|---|---|---:|---:|
| 10 | `release-10` | 11 | 2.7.5 |
| 11 | `release-11` | 17 | 4.0.4 |
| 12 | `release-12` | 17 | 4.0.8 |
| 13 | `release-13` | 17 | 4.0.8 |

The current official prerequisites for release 13 and development specify OpenJDK 17 and PostgreSQL 14 or newer, using PostgreSQL 17 in the guide. Recheck this before future upgrades. For older releases, find requirements contemporary to that release or use the exact versioned environment already maintained for it; do not extrapolate the current PostgreSQL minimum backward.

## Version alignment checks

Compare all discovered values rather than assuming the README is correct:

- release branch or tag;
- root and module POM revisions/parents;
- bundle and fragment versions;
- `Bundle-RequiredExecutionEnvironment`;
- `Require-Bundle` and `Fragment-Host` ranges;
- feature and category versions;
- target names, repository URLs, and installable units;
- CI images, toolchains, `JAVA_HOME`, wrappers, and build arguments.

The plugin's own semantic version may be independent of the iDempiere platform version. Preserve the repository convention unless the user explicitly requests platform-aligned artifact versions.

## iDempiere 14 development target


Verified 2026-10-14 against official master commit `75ad26081a1745ab64831567861ad8f9f6f78d36`:

| Property | Value |
|---|---|
| Source line | master (development) |
| Maven revision | `14.0.0-SNAPSHOT` |
| JDK | 17 |
| Tycho | 4.0.8 |
| ZK | 10.3.0.1 |
| Maven distribution | 3.9.10 via the repository wrapper |

Sources: [parent POM](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/org.idempiere.parent/pom.xml) and [wrapper properties](https://github.com/idempiere/idempiere/blob/75ad26081a1745ab64831567861ad8f9f6f78d36/.mvn/wrapper/maven-wrapper.properties).

Recheck the actual target checkout before building. This snapshot does not establish a stable release, release-14 branch, Docker tag, PostgreSQL/Oracle execution or REST plugin compatibility. Do not reuse source-release-13 or invent source-release-14. Verify the official image/tag/digest or use the project's configured compatible host/wrapper builder.

Core instructions and generated-migration rules apply to core contributions. Private plugins retain their own scaffolds, Entity Types and export policy. Shared annotation/REST/ZK skills still require exact API and dependency verification.
