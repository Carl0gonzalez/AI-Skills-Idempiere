# Skills de contribución al core

**Español** | [English](README.md)

Siete workflows para contribuciones al core de iDempiere. Leer primero AGENTS.md, skills locales y documentación oficial del checkout objetivo. Las políticas core no se aplican automáticamente a plugins privados.

| Skill | Propósito |
|---|---|
| [idempiere-contribution-workflow](idempiere-contribution-workflow/SKILL.md) | Preparar ramas vinculadas a Jira, commits focalizados, documentación y PR. |
| [idempiere-core-coding-standards](idempiere-core-coding-standards/SKILL.md) | Preservar transacciones, acceso por rol, compatibilidad API y comportamiento en ambos motores. |
| [idempiere-database-changes](idempiere-database-changes/SKILL.md) | Especificar cambios de UI y revisar migraciones generadas por el desarrollador con Centralized IDs. |
| [idempiere-unit-tests](idempiere-unit-tests/SKILL.md) | Escribir/ejecutar regresiones del core con fixtures GardenWorld verificados. |
| [idempiere-headless-build-run](idempiere-headless-build-run/SKILL.md) | Compilar core y realizar SyncDB/servidor autorizados con evidencia precisa. |
| [idempiere-pr-review](idempiere-pr-review/SKILL.md) | Revisar por etapas y probar integración en un worktree aislado. |
| [idempiere-jira-tickets](idempiere-jira-tickets/SKILL.md) | Redactar bugs/features reproducibles y reportes privados de seguridad. |

## Helper de revisión de PR

La skill de PR incluye un helper de worktrees aislados. Preserva el checkout original y rechaza limpieza cuando hay trabajo adicional en el worktree. Requisitos: Git 2.31+, Bash 3.2+ e identidad Git local configurada; Windows usa Git Bash. Leer la skill antes de ejecutar el helper. Consultar [política core](CORE_POLICY.md).


Consultar [catálogo del repo](../README.es.md) y [selección de versiones](../docs/VERSIONING.es.md).
