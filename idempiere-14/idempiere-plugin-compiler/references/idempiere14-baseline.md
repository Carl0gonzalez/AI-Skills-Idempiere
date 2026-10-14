# Verified iDempiere 14 development baseline

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
