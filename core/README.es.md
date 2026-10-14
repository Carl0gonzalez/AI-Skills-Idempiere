# Guías de contribución al core

**Español** | [English](README.md)

Los **siete workflows core** son adaptaciones locales del commit upstream 75ad26081a1745ab64831567861ad8f9f6f78d36. Leer primero AGENTS.md, skills y documentación oficial del checkout real. No imponen las políticas Jira/IDs/migración del core a esta biblioteca ni a plugins privados.

| Skill | Propósito |
|---|---|
| [idempiere-contribution-workflow](idempiere-contribution-workflow/SKILL.md) | Preparar ramas vinculadas a Jira, commits focalizados, documentación y PR. |
| [idempiere-core-coding-standards](idempiere-core-coding-standards/SKILL.md) | Preservar transacciones, acceso por rol, compatibilidad API y comportamiento en ambos motores. |
| [idempiere-database-changes](idempiere-database-changes/SKILL.md) | Especificar cambios de UI y revisar migraciones generadas por el desarrollador con Centralized IDs. |
| [idempiere-unit-tests](idempiere-unit-tests/SKILL.md) | Escribir/ejecutar regresiones del core con fixtures GardenWorld verificados. |
| [idempiere-headless-build-run](idempiere-headless-build-run/SKILL.md) | Compilar core y realizar SyncDB/servidor autorizados con evidencia precisa. |
| [idempiere-pr-review](idempiere-pr-review/SKILL.md) | Revisar por etapas y probar integración en un worktree aislado. |
| [idempiere-jira-tickets](idempiere-jira-tickets/SKILL.md) | Redactar bugs/features reproducibles y reportes privados de seguridad. |

## Límites de ejecución

El desarrollador genera migraciones core, IDs/UUIDs del AD y modelos regenerados según reglas upstream. El agente los especifica y revisa. Commits, push, publicación de PR/tickets, SyncDB y ejecución del servidor son acciones separadas, sujetas a la autorización del usuario.

## Helper local de PR

El helper utiliza un worktree aislado y detached, comprueba el remoto oficial efectivo y preserva el checkout original. Rechaza limpieza con trabajo tracked/untracked/ignored o cambios de HEAD y no tiene borrado forzado. No revierte migraciones ni detiene servidores.

Requisitos: Git 2.31+ (worktrees/--path-format), Bash 3.2+ e identidad local para el merge de revisión no publicado. Windows usa Git Bash. Las pruebas usan fixtures locales temporales; no se afirma haber probado un PR real de GitHub.

```bash
python3 tests/test_review_pr.py
```

Leer [política](CORE_POLICY.md) y la skill de revisión antes de preparar un worktree.

## Revisiones y referencias

Consultar [versionado](../docs/VERSIONING.es.md), [fuentes](../docs/SOURCES.md), [revisión de adopción](../docs/ADOPTION_REVIEW.es.md) y [wiki](../docs/wiki/Inicio.md). Estas instrucciones no instalan skills ni publican páginas en una wiki remota.
