# Skills iDempiere 14

**Español** | [English](README.md)

Esta carpeta contiene **15 skills orientadas a proyectos iDempiere 14**. Identifica la plataforma objetivo, no la versión publicada de cada skill ni una certificación Java/OSGi/base de datos. Revisar APIs, scaffold y build reales antes de aplicar un workflow.

## Catálogo

| Skill | Propósito |
|---|---|
| [idempiere-local-postgres](idempiere-local-postgres/SKILL.md) | Diagnóstico PostgreSQL de solo lectura y controles explícitos de escritura. |
| [idempiere-migration-review](idempiere-migration-review/SKILL.md) | Auditar coherencia entre modelos, esquema, AD y Java/OSGi. |
| [idempiere-model-designer](idempiere-model-designer/SKILL.md) | Especificar entidades, referencias, ciclo de vida y requisitos del diccionario. |
| [idempiere-pipo-integrity-review](idempiere-pipo-integrity-review/SKILL.md) | Revisar tipos físicos/diccionario y dependencias de PackOut. |
| [idempiere-plugin-compiler](idempiere-plugin-compiler/SKILL.md) | Descubrir el builder real de target platform e informar artefactos. |
| [idempiere-plugin-version-upgrader](idempiere-plugin-version-upgrader/SKILL.md) | Planificar y verificar upgrades de plugins en ramas de versión aisladas. |
| [idempiere-plugin-component-developer](idempiere-plugin-component-developer/SKILL.md) | Implementar procesos, callouts, eventos y factories con registro compatible. |
| [idempiere-plugin-designer](idempiere-plugin-designer/SKILL.md) | Traducir requisitos funcionales a diseños Java/OSGi mínimos. |
| [idempiere-plugin-manual-generator](idempiere-plugin-manual-generator/SKILL.md) | Derivar manuales funcionales en inglés y guías de pruebas desde código/metadatos reales. |
| [idempiere-plugin-readme](idempiere-plugin-readme/SKILL.md) | Redactar README de plugins en inglés con evidencia del repositorio. |
| [idempiere-plugin-wiki-page](idempiere-plugin-wiki-page/SKILL.md) | Preparar páginas MediaWiki de plugins iDempiere basadas en evidencia. |
| [idempiere-plugin-test-developer](idempiere-plugin-test-developer/SKILL.md) | Escribir pruebas de regresión con el framework existente y fixtures aislados. |
| [jenkinsfile-developer](jenkinsfile-developer/SKILL.md) | Mantener builds Jenkins y pipelines de documentación según la release. |
| [skill-architect](skill-architect/SKILL.md) | Diseñar skills focalizadas cuando el catálogo no cubre una tarea reutilizable. |
| [skill-reviewer](skill-reviewer/SKILL.md) | Revisar activación, alcance, duplicación, estructura y calidad de instrucciones. |

## Seleccionar skills complementarias

Seleccionar este conjunto de versión una sola vez. Añadir las [skills comunes](../shared/README.es.md) pertinentes para arquitectura, calidad, entornos, REST y ZK. Consultar [guías del core](../core/README.es.md) sólo para contribuciones al core; prevalecen AGENTS.md y skills del checkout real. No instalar varias copias con el mismo nombre de distintas versiones.

## Revisiones y mantenimiento

Consultar [versionado de skills](../docs/VERSIONING.es.md) y [el inventario exacto de contenido](../docs/skill-versions.json). Cada copia y sus recursos tienen revisión propia. Los cambios comunes deben revisarse en todas las copias afectadas, sin propagar APIs a ciegas. Validar el repositorio antes de evaluar instalación.

## Uso y validación

Pedir al agente que lea SKILL.md y sólo los recursos necesarios. Cada skill vive en su carpeta y tiene metadatos name/description. Instalar, hacer commit, publicar o escribir en BD son acciones autorizadas por separado.

Desde la raíz del repositorio:

```bash
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
```

Consultar [wiki en español](../docs/wiki/Inicio.md), [README principal](../README.es.md) y [revisión de adopción](../docs/ADOPTION_REVIEW.es.md). Esta actualización de documentación no instala skills.
