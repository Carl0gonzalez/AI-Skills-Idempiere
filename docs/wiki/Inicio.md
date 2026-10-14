# Skills de IA para iDempiere

**Español** | [English](Home.md)

Esta biblioteca ofrece a los agentes IA instrucciones reutilizables para desarrollar con iDempiere. Centraliza workflows de plugins, arquitectura, entornos y reglas de contribución al core, manteniendo sus ámbitos separados. Es un catálogo de skills, no un plugin OSGi instalado en el ERP.

- **Responsable:** Carlo González, según la licencia del repositorio.
- **Licencia:** [MIT](../../LICENSE).
- **Fuentes:** [AI-Skills-Idempiere](https://github.com/Carl0gonzalez/AI-Skills-Idempiere).
- **Estado:** documentación e inventario de contenido locales; no se asigna release publicada ni certificación runtime.

## Organización del catálogo

| Carpeta | Skills | Uso |
|---|---:|---|
| idempiere-8, idempiere-10, idempiere-12, idempiere-13, idempiere-14 | 15 en cada una | Seleccionar la línea objetivo real del proyecto |
| shared | 11 | Arquitectura, calidad, entornos y componentes especializados |
| core | 7 | Contribuir al core según las reglas del checkout real |

Hay **93 entradas y 33 nombres distintos**. Una carpeta de versión expresa plataforma objetivo; no demuestra que cada API/ejemplo se compiló para esa release. Consultar [versionado](../VERSIONING.es.md) e [inventario exacto por skill](../skill-versions.json).

## iDempiere 14

El [nuevo conjunto objetivo](../../idempiere-14/README.es.md) contiene los mismos 15 workflows y las mejoras heredadas de Hengsin/core. Se orienta al desarrollo 14.0.0-SNAPSHOT verificado; antes de usarlo se descubre el builder y commit reales.

## Workflows versionados de plugins

Los enlaces usan la copia iDempiere 13 para consulta. Seleccionar la versión real antes de aplicar una skill.

| Skill | Propósito |
|---|---|
| [idempiere-local-postgres](../../idempiere-13/idempiere-local-postgres/SKILL.md) | Diagnóstico PostgreSQL de solo lectura y controles explícitos de escritura. |
| [idempiere-migration-review](../../idempiere-13/idempiere-migration-review/SKILL.md) | Auditar coherencia entre modelos, esquema, AD y Java/OSGi. |
| [idempiere-model-designer](../../idempiere-13/idempiere-model-designer/SKILL.md) | Especificar entidades, referencias, ciclo de vida y requisitos del diccionario. |
| [idempiere-pipo-integrity-review](../../idempiere-13/idempiere-pipo-integrity-review/SKILL.md) | Revisar tipos físicos/diccionario y dependencias de PackOut. |
| [idempiere-plugin-compiler](../../idempiere-13/idempiere-plugin-compiler/SKILL.md) | Descubrir el builder real de target platform e informar artefactos. |
| [idempiere-plugin-version-upgrader](../../idempiere-13/idempiere-plugin-version-upgrader/SKILL.md) | Planificar y verificar upgrades de plugins en ramas de versión aisladas. |
| [idempiere-plugin-component-developer](../../idempiere-13/idempiere-plugin-component-developer/SKILL.md) | Implementar procesos, callouts, eventos y factories con registro compatible. |
| [idempiere-plugin-designer](../../idempiere-13/idempiere-plugin-designer/SKILL.md) | Traducir requisitos funcionales a diseños Java/OSGi mínimos. |
| [idempiere-plugin-manual-generator](../../idempiere-13/idempiere-plugin-manual-generator/SKILL.md) | Derivar manuales funcionales en inglés y guías de pruebas desde código/metadatos reales. |
| [idempiere-plugin-readme](../../idempiere-13/idempiere-plugin-readme/SKILL.md) | Redactar README de plugins en inglés con evidencia del repositorio. |
| [idempiere-plugin-wiki-page](../../idempiere-13/idempiere-plugin-wiki-page/SKILL.md) | Preparar páginas MediaWiki de plugins iDempiere basadas en evidencia. |
| [idempiere-plugin-test-developer](../../idempiere-13/idempiere-plugin-test-developer/SKILL.md) | Escribir pruebas de regresión con el framework existente y fixtures aislados. |
| [jenkinsfile-developer](../../idempiere-13/jenkinsfile-developer/SKILL.md) | Mantener builds Jenkins y pipelines de documentación según la release. |
| [skill-architect](../../idempiere-13/skill-architect/SKILL.md) | Diseñar skills focalizadas cuando el catálogo no cubre una tarea reutilizable. |
| [skill-reviewer](../../idempiere-13/skill-reviewer/SKILL.md) | Revisar activación, alcance, duplicación, estructura y calidad de instrucciones. |

## Workflows comunes

| Skill | Propósito |
|---|---|
| [idempiere-architecture-patterns](../../shared/idempiere-architecture-patterns/SKILL.md) | Elegir el mecanismo compatible más simple y distinguir core, plugin y entorno. |
| [idempiere-plugin-quality-gate](../../shared/idempiere-plugin-quality-gate/SKILL.md) | Coordinar ejecución de pruebas, cobertura y evidencia de calidad. |
| [crear-entornos-idempiere-envrc](../../shared/crear-entornos-idempiere-envrc/SKILL.md) | Crear y revisar entornos direnv aislados con comprobaciones estáticas. |
| [documentar-entornos-idempiere-envrc](../../shared/documentar-entornos-idempiere-envrc/SKILL.md) | Documentar el contrato operativo del .envrc real. |
| [gestionar-tareas](../../shared/gestionar-tareas/SKILL.md) | Mantener un registro de tareas existente cuando se solicita explícitamente. |
| [idempiere-event-annotation](../../shared/idempiere-event-annotation/SKILL.md) | Implementar delegates anotados con APIs de la versión objetivo. |
| [idempiere-rest-resource](../../shared/idempiere-rest-resource/SKILL.md) | Definir contratos REST, controles de acceso y registro ResourceExtension. |
| [idempiere-window-validator](../../shared/idempiere-window-validator/SKILL.md) | Interceptar acciones de ventana resolviendo todos los callbacks. |
| [idempiere-zul-form](../../shared/idempiere-zul-form/SKILL.md) | Crear formularios ZUL, controllers, wiring y recursos empaquetados. |
| [idempiere-grouped-listbox](../../shared/idempiere-grouped-listbox/SKILL.md) | Implementar modelos agrupados, renderers y acceso limitado a datos. |
| [idempiere-wlistbox-custom-editor](../../shared/idempiere-wlistbox-custom-editor/SKILL.md) | Personalizar editores y presentación de columnas WListbox existentes. |

## Contribuciones al core

| Skill | Propósito |
|---|---|
| [idempiere-contribution-workflow](../../core/idempiere-contribution-workflow/SKILL.md) | Preparar ramas vinculadas a Jira, commits focalizados, documentación y PR. |
| [idempiere-core-coding-standards](../../core/idempiere-core-coding-standards/SKILL.md) | Preservar transacciones, acceso por rol, compatibilidad API y comportamiento en ambos motores. |
| [idempiere-database-changes](../../core/idempiere-database-changes/SKILL.md) | Especificar cambios de UI y revisar migraciones generadas por el desarrollador con Centralized IDs. |
| [idempiere-unit-tests](../../core/idempiere-unit-tests/SKILL.md) | Escribir/ejecutar regresiones del core con fixtures GardenWorld verificados. |
| [idempiere-headless-build-run](../../core/idempiere-headless-build-run/SKILL.md) | Compilar core y realizar SyncDB/servidor autorizados con evidencia precisa. |
| [idempiere-pr-review](../../core/idempiere-pr-review/SKILL.md) | Revisar por etapas y probar integración en un worktree aislado. |
| [idempiere-jira-tickets](../../core/idempiere-jira-tickets/SKILL.md) | Redactar bugs/features reproducibles y reportes privados de seguridad. |

## Selección y uso de skills

1. Determinar si el trabajo corresponde a un plugin, contribución core o entorno.
2. Confirmar release iDempiere, JDK, build y registro existentes.
3. Leer el workflow de versión adecuado y sumar arquitectura/especializaciones comunes cuando aporten información útil.
4. Para core, leer primero AGENTS.md y sus skills locales. Las adaptaciones centrales no reemplazan reglas más recientes del checkout.
5. Preservar modelos generados, transacción propietaria, acceso por rol/cliente/org y ciclo documental real.
6. Separar evidencia de fuente/build/pruebas/runtime. La instalación se evalúa después; no reemplazar silenciosamente una skill instalada.

Ejemplos:

- Un callout en un plugin existente usa arquitectura, componentes de la versión real y la factory existente.
- Un formulario ZUL usa su skill especializada tras verificar APIs y empaquetado de recursos.
- Un bug core utiliza contribución, coding standards, pruebas y revisión pertinentes al ticket.
- Un cambio de diccionario core se especifica para generación humana en UI con Centralized IDs; el agente revisa scripts y no escribe sustitutos.

## Requisitos y validación

Leer skills requiere un agente que acceda a Markdown y recursos locales. No exige Gemini CLI, Eclipse ni un connector específico. Los requisitos de implementación/build se derivan del proyecto. Validar el catálogo requiere Python 3 y PyYAML; el helper de PR requiere Git 2.31+, Bash 3.2+ e identidad Git local.

Desde la raíz del repo:

```bash
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
python3 tests/test_review_pr.py
```

La revisión de adopción registra 78 entradas validadas y diez escenarios locales Git aprobados. Esos controles no compilan Java, activan OSGi, importan 2Pack ni validan PostgreSQL/Oracle/UI. Consultar [la revisión](../ADOPTION_REVIEW.es.md) para conocer los límites precisos.

## Política de revisiones

Las revisiones de contenido son digests SHA-256 de instrucciones y recursos. Línea iDempiere, revisión, commit upstream y release publicada son conceptos distintos. No se infiere «Probado con release» desde las carpetas de versión o main. Una futura release requiere tag acordado y evidencia explícita.

## Fuentes y mantenimiento

[La procedencia](../SOURCES.md) documenta catálogo previo, skills propias instaladas, pack de componentes de Hengsin y siete workflows upstream del core. Los enlaces públicos identifican el repo fuente; las incorporaciones locales necesitan commit/push separados para aparecer remotamente.

El catálogo tiene licencia MIT. Aplicar las cabeceras/licencias del core/plugin objetivo al implementar código. Cada actualización debe revisar alcance/duplicación, comprobar copias afectadas, validar recursos y actualizar inventario.

## Documentación

- [README principal](../../README.es.md).
- [Selección de versión y revisiones](../VERSIONING.es.md).
- [Catálogo común](../../shared/README.es.md) y [catálogo core](../../core/README.es.md).
- [Inventario de skills propias instaladas](../INSTALLED_SKILLS_INVENTORY.md).
- [Formatos de wiki y estado de publicación](README.md).
