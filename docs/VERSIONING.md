# Target versions

**English** | [Español](VERSIONING.es.md)

The iDempiere line and a skill revision are different: a target directory identifies the platform, while Git history records changes to instructions and resources.

| Directory | Skills | Target |
|---|---:|---|
| [idempiere-8](../idempiere-8/README.md) | 15 | iDempiere 8 |
| [idempiere-10](../idempiere-10/README.md) | 15 | iDempiere 10 |
| [idempiere-12](../idempiere-12/README.md) | 15 | iDempiere 12 |
| [idempiere-13](../idempiere-13/README.md) | 15 | iDempiere 13 |
| [idempiere-14](../idempiere-14/README.md) | 15 | iDempiere 14 development |

| [shared](../shared/README.md) | 11 | Common workflows |
| [core](../core/README.md) | 7 | Core contributions |

Select one versioned set matching the actual project. Do not load several copies with the same name. Shared workflows require target-API checks; core workflows follow the actual checkout's contribution rules.

The catalog contains **93 entries and 33 distinct names**. A directory name is a target, not a runtime-test result. For iDempiere 14, inspect the selected development source revision, JDK and builder. Follow the target project's toolchain requirements rather than copying a previous release's settings.
