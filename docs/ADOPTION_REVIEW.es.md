# Doble revisión de adopciones y mejoras

Fecha: 2026-10-14. Esta revisión registra la preparación local previa a la autorización posterior de commit/push. Sus estados de publicación describen ese momento; instalación, publicación en una wiki remota, bases de datos y despliegues no forman parte de la revisión.

## Review result

**approve para las instrucciones del catálogo**, con compatibilidad Java/OSGi/DB/UI pendiente de comprobar en cada proyecto objetivo. Se realizaron dos pasadas de revisión por el mismo agente; no se atribuye una revisión independiente ni pruebas de generación a otro agente.

El catálogo contiene 33 nombres distintos y 78 entradas: 15 por cada versión 8/10/12/13, 11 comunes y siete para contribución al core. Las APIs de las skills comunes están condicionadas a verificación; no se asignó compatibilidad por semejanza de versiones.

## Primera revisión: idoneidad y alcance

| Origen/capacidad | Decisión | Razón |
|---|---|---|
| Arquitectura instalada | Centralizar completa y reforzar contexto/callers/API | Selecciona mecanismos y evita duplicación |
| Quality gate instalado | Centralizar recursos y ajustar framework/integraciones | Coordina evidencia; no sustituye autoría de tests |
| Dos skills de entornos | Centralizar sin imponer una release | Auditoría y documentación del .envrc real |
| gestionar-tareas instalada | Centralizar como complemento | Sólo actúa sobre registro existente y petición explícita |
| Annotation/mapped processes y callouts | Integrar en componentes | Evita skills con activación casi idéntica |
| Mapped model factory | Integrar en diseño de modelos | Debe respetar mapping/activator existentes |
| Handler OSGi clásico | Integrar en componentes | Su selección depende del registro del proyecto |
| Delegates por anotación | Skill especializada común | Catálogo de tipos de evento útil y distinto |
| REST ResourceExtension | Skill especializada común | Contrato y registro de un plugin REST real |
| WindowValidator | Skill especializada común | Intercepción UI; no sustituye invariantes de dominio |
| ZUL, grupos y editor de columna | Tres skills especializadas | Tareas distintas: formulario, agrupación y columna |
| Siete workflows del core | Adaptaciones bajo core/ | Políticas de contribución no aplicables globalmente a plugins |
| README instalado | Conservar ejemplos genéricos y mejorar evidencia | Evita restaurar valores por defecto de empresa |
| Wiki instalada | Sincronizar mejora de contributors en cuatro copias | Preserva la convención existente más reciente |

No se copió el pack entero ni se crearon versiones que afirmaran soporte no probado. Las seis skills propias que no están instaladas ya existían en las cuatro carpetas y se conservaron; se mejoraron las pertinentes. Tampoco se incorporaron skills de producto/plataforma ajenas a iDempiere dentro del catálogo.

## Segunda revisión: coherencia y escenarios

Esta pasada examinó las instrucciones finales con casos concretos; es una evaluación editorial de decisiones, no ejecución de tareas Java por un agente independiente.

| Caso revisado | Decisión indicada por las skills finales |
|---|---|
| Plugin v8 sin API de anotación/mapped | Comprobar dependencia real y mantener factory/registro compatible; no generar imports inventados |
| Clase de modelo presente sólo en target platform | Aceptar evidencia de dependencia resuelta; no exigir archivo abierto en IDE |
| Bundle con activator y factory existentes | Reutilizarlos; no añadir segundo registro ni imponer Incremental2PackActivator |
| Nuevo AD_Message en contribución core | Especificar UI/Centralized IDs y revisar lo generado; no escribir INSERT/DDL/UUID |
| Migración autorizada de plugin privado | Aplicar política del plugin; no imponer prohibición del core por defecto |
| Regla que también debe cumplir REST/importación | Modelo/evento/dominio; no enforcement únicamente mediante callout/WindowValidator |
| WindowValidator con confirmación asíncrona | Resolver callback una vez, incluyendo cancelación y errores |
| REST sin mapping implementado | No considerar un JSON vacío como endpoint terminado |
| SvrProcess que captura excepciones | Afirmar ProcessInfo/resultado real; no asumir assertThrows |
| verify con tests omitidos o informes antiguos | Informar compilación; habilitar tests y verificar conteos/informes nuevos |
| Fixture compartido GardenWorld | Crear datos propios/revertibles o mocks compatibles; no modificar semilla global |
| Cambio de firma pública/protegida | Overload/deprecation o ruptura explícita documentada y decidida por desarrollador |
| PR con trabajo previo en checkout | Worktree aislado; no checkout/stash/reset del trabajo del usuario |
| SyncDB con migraciones de otros tickets pendientes | Revisar todo el conjunto pendiente y destino antes de la escritura autorizada |
| Código terminado pero Oracle/OSGi/UI no ejecutados | Informar cada límite sin convertir build en evidencia runtime |

Se corrigieron durante esta pasada: dependencia relativa externa de las skills core, uso de mapfile incompatible con Bash 3.2, alcance ambiguo de quality gate, LIMIT específico de PostgreSQL en referencia común, imposición de índices por cada FK, y ruido de cambios de finales de línea.

## Findings

- Las entradas tienen frontmatter válido y recursos locales resolubles.
- Las 14 skills custom/domain instaladas inventariadas tienen destino en el catálogo; se preservaron las originales instaladas.
- Las cuatro versiones conservan el mismo inventario de 15 nombres. Las familias versionadas actualizadas usan las mismas reglas comunes, manteniendo menciones de su versión donde corresponde.
- La política core es referencia contextual bajo core/; no se instaló AGENTS.md del core como regla raíz de esta biblioteca ni se copiaron sus archivos de instrucciones para otros agentes.
- Se respetaron cambios previos de los README y las cuatro carpetas de upgrader sin seguimiento. El contenido de upgrader previo no fue sobrescrito.
- Las adopciones son instrucciones originales adaptadas con procedencia; no se copiaron/relicenciaron assets upstream sin licencia explícita.
- El script local de PR no publica, no ejecuta SyncDB ni inicia servidor; rechaza remotos no oficiales y limpieza con archivos tracked/untracked/ignored o cambios de HEAD.

## Suggested fixes

Las correcciones de esta revisión ya se aplicaron. Para el siguiente trabajo de instalación: elegir una versión, revisar conflictos de nombres y seleccionar shared/core por ámbito. No instalar copias de distintas versiones con el mismo nombre a la vez. Validar APIs/plantillas contra la release concreta antes de usarlas para generar código.

## Revised frontmatter

Las siete skills core y seis especializaciones nuevas tienen descripciones específicas para su mecanismo y alcance. database-changes restringe su activación a contribuciones core; ZUL tiene frontmatter explícito. Las familias de meta-skills ahora son independientes del proveedor. No quedan las descripciones YAML partidas del pack de referencia.

## Structure advice

- idempiere-{8,10,12,13}/: 15 skills propias por versión, con referencias internas para patrones de registro/modelos.
- shared/: arquitectura, quality gate, entornos, tareas y seis especializaciones, cada una con recursos autocontenidos cuando son necesarios.
- core/: siete workflows y resumen de política; cada skill enlaza la autoridad upstream y sus recursos internos.
- docs/: fuentes, inventario instalado y esta revisión.
- scripts/ y tests/: validador de catálogo y pruebas del helper de worktrees.

## Validación ejecutada

| Control | Resultado |
|---|---|
| quick_validate.py sobre las 78 entradas | 78 aprobadas, cero fallos |
| scripts/validate_catalog.py | Metadatos, enlaces locales e inventarios coherentes |
| bash -n review-pr.sh | Sin errores de sintaxis |
| tests/test_review_pr.py | Diez escenarios aprobados en Git temporal/local |
| Helpers copiados de quality gate | JSON y Prometheus comprobados con fixture de tres tests, un fallo y un omitido |
| Auditor/inventario .envrc copiados | Ejecutados sobre fixture temporal de sólo lectura |
| Sintaxis de todos los archivos Python | Verificada sin generar artefactos en el catálogo |
| git diff --check | Sin errores |

Los tests del helper usan una capa de transporte de fixture: el remoto configurado es oficial y el fetch se redirige localmente. No se probó un PR real en GitHub. Las comprobaciones de .envrc son de los helpers estáticos, no activación de entornos ni instalaciones Java/Maven/Eclipse. No se compiló Java, no se ejecutaron PostgreSQL/Oracle, PackIn, servidor ni UI.

## Final recommendation

Catálogo preparado para revisión de instalación, sin instalación realizada. Utilizar las nuevas guías core en ese contexto y combinar las especializaciones con arquitectura/build/pruebas según el proyecto. El resultado es una actualización local revisable, no un commit ni una publicación del repositorio.

## Documentación y versionado añadidos

Se añadieron README bilingües para las cuatro líneas objetivo, shared y core, una guía de versionado bilingüe y el inventario de revisiones SHA-256 de las 78 entradas y sus recursos. Se distingue línea iDempiere, revisión de contenido, base upstream y futura release publicada. No se asignaron releases ficticias.

La wiki local tiene [edición inglesa](wiki/Home.md), [edición española](wiki/Inicio.md) y fuentes MediaWiki enlazadas desde su [índice](wiki/README.es.md). Se adaptó la skill de wiki a una biblioteca de skills, sin categoría de plugins ni promesas de instalación OSGi. Estado: archivos locales, sin preview o publicación remota.

Validación adicional ejecutada: cuatro pruebas de revisiones de contenido, comprobación read-only del inventario, enlaces del catálogo y equilibrio de tablas/tags de ambas fuentes MediaWiki. Las cuatro pruebas verifican copias por versión, cambios/movimientos de recursos, separación de README y rechazo de inventario desactualizado sin escritura. No alteran skills instaladas ni prueban runtime iDempiere.

## Incorporación de iDempiere 14

Se añadió un quinto conjunto de 15 skills, con README bilingües y entradas wiki Markdown/MediaWiki. El catálogo actual tiene 93 entradas y conserva 33 nombres distintos; los conteos de 78 anteriores corresponden a la revisión histórica previa. Se verificó el commit oficial 75ad26081a1745ab64831567861ad8f9f6f78d36, con 14.0.0-SNAPSHOT, JDK 17, Tycho 4.0.8 y Maven Wrapper 3.9.10. Las guías de compiler/Jenkins no inventan release-14 ni imágenes source-release-14 y las referencias de upgrades mantienen datos históricos explícitos. Se heredan las mejoras Hengsin/core; shared y core no se duplican. No se instala ni compila Java como parte de esta incorporación documental.
