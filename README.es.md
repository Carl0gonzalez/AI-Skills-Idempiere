# Repositorio de skills iDempiere

**Español** | [English](README.md)

Skills reutilizables para desarrollo de plugins iDempiere, modelado, pruebas, documentación, entornos y contribuciones al core.

## Organización

| Carpeta | Entradas | Alcance |
|---|---:|---|
| [idempiere-8](idempiere-8/README.es.md) | 15 | iDempiere 8 |
| [idempiere-10](idempiere-10/README.es.md) | 15 | iDempiere 10 |
| [idempiere-12](idempiere-12/README.es.md) | 15 | iDempiere 12 |
| [idempiere-13](idempiere-13/README.es.md) | 15 | iDempiere 13 |
| [idempiere-14](idempiere-14/README.es.md) | 15 | iDempiere 14 en desarrollo |
| [shared](shared/README.es.md) | 11 | Workflows comunes |
| [core](core/README.es.md) | 7 | Contribuciones al core |

**93 entradas y 33 nombres distintos.** Cada conjunto versionado contiene los mismos 15 nombres de workflow.

## Skills de plugins

| Skill | Propósito |
|---|---|
| [idempiere-local-postgres](idempiere-14/idempiere-local-postgres/SKILL.md) | Diagnóstico PostgreSQL de solo lectura y controles explícitos de escritura. |
| [idempiere-migration-review](idempiere-14/idempiere-migration-review/SKILL.md) | Auditar coherencia entre modelos, esquema, AD y Java/OSGi. |
| [idempiere-model-designer](idempiere-14/idempiere-model-designer/SKILL.md) | Especificar entidades, referencias, ciclo de vida y requisitos del diccionario. |
| [idempiere-pipo-integrity-review](idempiere-14/idempiere-pipo-integrity-review/SKILL.md) | Revisar tipos físicos/diccionario y dependencias de PackOut. |
| [idempiere-plugin-compiler](idempiere-14/idempiere-plugin-compiler/SKILL.md) | Descubrir el builder real de target platform e informar artefactos. |
| [idempiere-plugin-version-upgrader](idempiere-14/idempiere-plugin-version-upgrader/SKILL.md) | Planificar y verificar upgrades de plugins en ramas de versión aisladas. |
| [idempiere-plugin-component-developer](idempiere-14/idempiere-plugin-component-developer/SKILL.md) | Implementar procesos, callouts, eventos y factories con registro compatible. |
| [idempiere-plugin-designer](idempiere-14/idempiere-plugin-designer/SKILL.md) | Traducir requisitos funcionales a diseños Java/OSGi mínimos. |
| [idempiere-plugin-manual-generator](idempiere-14/idempiere-plugin-manual-generator/SKILL.md) | Derivar manuales funcionales en inglés y guías de pruebas desde código/metadatos reales. |
| [idempiere-plugin-readme](idempiere-14/idempiere-plugin-readme/SKILL.md) | Redactar README de plugins en inglés con evidencia del repositorio. |
| [idempiere-plugin-wiki-page](idempiere-14/idempiere-plugin-wiki-page/SKILL.md) | Preparar páginas MediaWiki de plugins iDempiere basadas en evidencia. |
| [idempiere-plugin-test-developer](idempiere-14/idempiere-plugin-test-developer/SKILL.md) | Escribir pruebas de regresión con el framework existente y fixtures aislados. |
| [jenkinsfile-developer](idempiere-14/jenkinsfile-developer/SKILL.md) | Mantener builds Jenkins y pipelines de documentación según la release. |
| [skill-architect](idempiere-14/skill-architect/SKILL.md) | Diseñar skills focalizadas cuando el catálogo no cubre una tarea reutilizable. |
| [skill-reviewer](idempiere-14/skill-reviewer/SKILL.md) | Revisar activación, alcance, duplicación, estructura y calidad de instrucciones. |

Los enlaces anteriores apuntan al conjunto iDempiere 14. Seleccionar la carpeta que corresponde a la versión del proyecto.

## Skills comunes

| Skill | Propósito |
|---|---|
| [idempiere-architecture-patterns](shared/idempiere-architecture-patterns/SKILL.md) | Elegir el mecanismo compatible más simple y distinguir core, plugin y entorno. |
| [idempiere-plugin-quality-gate](shared/idempiere-plugin-quality-gate/SKILL.md) | Coordinar ejecución de pruebas, cobertura y evidencia de calidad. |
| [crear-entornos-idempiere-envrc](shared/crear-entornos-idempiere-envrc/SKILL.md) | Crear y revisar entornos direnv aislados con comprobaciones estáticas. |
| [documentar-entornos-idempiere-envrc](shared/documentar-entornos-idempiere-envrc/SKILL.md) | Documentar el contrato operativo del .envrc real. |
| [gestionar-tareas](shared/gestionar-tareas/SKILL.md) | Mantener un registro de tareas existente cuando se solicita explícitamente. |
| [idempiere-event-annotation](shared/idempiere-event-annotation/SKILL.md) | Implementar delegates anotados con APIs de la versión objetivo. |
| [idempiere-rest-resource](shared/idempiere-rest-resource/SKILL.md) | Definir contratos REST, controles de acceso y registro ResourceExtension. |
| [idempiere-window-validator](shared/idempiere-window-validator/SKILL.md) | Interceptar acciones de ventana resolviendo todos los callbacks. |
| [idempiere-zul-form](shared/idempiere-zul-form/SKILL.md) | Crear formularios ZUL, controllers, wiring y recursos empaquetados. |
| [idempiere-grouped-listbox](shared/idempiere-grouped-listbox/SKILL.md) | Implementar modelos agrupados, renderers y acceso limitado a datos. |
| [idempiere-wlistbox-custom-editor](shared/idempiere-wlistbox-custom-editor/SKILL.md) | Personalizar editores y presentación de columnas WListbox existentes. |

## Skills de contribución al core

| Skill | Propósito |
|---|---|
| [idempiere-contribution-workflow](core/idempiere-contribution-workflow/SKILL.md) | Preparar ramas vinculadas a Jira, commits focalizados, documentación y PR. |
| [idempiere-core-coding-standards](core/idempiere-core-coding-standards/SKILL.md) | Preservar transacciones, acceso por rol, compatibilidad API y comportamiento en ambos motores. |
| [idempiere-database-changes](core/idempiere-database-changes/SKILL.md) | Especificar cambios de UI y revisar migraciones generadas por el desarrollador con Centralized IDs. |
| [idempiere-unit-tests](core/idempiere-unit-tests/SKILL.md) | Escribir/ejecutar regresiones del core con fixtures GardenWorld verificados. |
| [idempiere-headless-build-run](core/idempiere-headless-build-run/SKILL.md) | Compilar core y realizar SyncDB/servidor autorizados con evidencia precisa. |
| [idempiere-pr-review](core/idempiere-pr-review/SKILL.md) | Revisar por etapas y probar integración en un worktree aislado. |
| [idempiere-jira-tickets](core/idempiere-jira-tickets/SKILL.md) | Redactar bugs/features reproducibles y reportes privados de seguridad. |

## Uso

1. Seleccionar la carpeta versionada que corresponde al proyecto iDempiere.
2. Añadir los workflows comunes pertinentes para arquitectura, calidad, REST, ZK o entornos.
3. Usar workflows core sólo para contribuciones al core. Prevalecen AGENTS.md e instrucciones locales del checkout objetivo.
4. Leer SKILL.md y sus recursos antes de realizar la tarea.

Para Codex, copiar cada carpeta de skill seleccionada a `.agents/skills/` del proyecto. Las skills comunes/core pueden ubicarse en la biblioteca global del usuario. Copiar la carpeta completa, incluidos scripts, referencias y assets. No cargar varias copias del mismo nombre de distintas versiones ni sobrescribir personalizaciones sin revisarlas.

## Versiones objetivo

Las carpetas identifican la línea iDempiere prevista. La fuente, JDK, APIs, target platform y builder reales determinan la compatibilidad. iDempiere 14 se orienta a fuentes de desarrollo; revisar el commit seleccionado antes de compilar.

Las revisiones de las skills se mantienen mediante el historial Git. Consultar [selección de versiones](docs/VERSIONING.es.md). El repositorio complementario [idempiere-dev-environments](https://github.com/Carl0gonzalez/idempiere-dev-environments) documenta entornos de desarrollo aislados.

## Documentación

- [Wiki en español](https://github.com/Carl0gonzalez/AI-Skills-Idempiere/wiki/Inicio).
- [Wiki en inglés](https://github.com/Carl0gonzalez/AI-Skills-Idempiere/wiki/Home).
- [Fuentes de la wiki](docs/wiki/README.es.md).
- [Procedencia](docs/SOURCES.md).

## Mantenimiento

Mantener nombres y criterios de activación específicos. Reutilizar workflows antes de crear otra skill. Conservar los recursos necesarios dentro de su carpeta. Revisar copias afectadas cuando cambia un comportamiento común y actualizar ambos idiomas del catálogo.

## Licencia

[MIT](LICENSE). Copyright © 2026 Carlo González.
