# Versiones de skills y plataformas objetivo

**Español** | [English](VERSIONING.md)

Deben distinguirse tres identificadores:

| Identificador | Significado | Evidencia |
|---|---|---|
| Línea objetivo iDempiere | Familia del proyecto: 8, 10, 12 o 13 | Carpeta de versión y checkout objetivo real |
| Revisión de contenido de la skill | Instrucciones, scripts, referencias, assets y metadatos UI exactos | SHA-256 en [skill-versions.json](skill-versions.json) |
| Release publicada del catálogo | Versión/tag emitida deliberadamente por el mantenedor | Tag/release Git; esta actualización no asigna ninguna |

La rama local es `main`; durante la revisión del 2026-10-14 no se encontraron tags locales de release ni ramas semánticas de versión. Las cuatro carpetas son conjuntos objetivo, no cuatro releases del software. Una carpeta iDempiere 13 no justifica afirmar «Probado con release 13.0.0».

## Matriz del catálogo

| Ámbito | Entradas | Uso previsto | Evidencia de compatibilidad |
|---|---:|---|---|
| [idempiere-8](../idempiere-8/README.es.md) | 15 | Proyectos orientados a iDempiere 8 | Descubrir/verificar APIs y build de la release real |
| [idempiere-10](../idempiere-10/README.es.md) | 15 | Proyectos orientados a iDempiere 10 | Descubrir/verificar APIs y build de la release real |
| [idempiere-12](../idempiere-12/README.es.md) | 15 | Proyectos orientados a iDempiere 12 | Descubrir/verificar APIs y build de la release real |
| [idempiere-13](../idempiere-13/README.es.md) | 15 | Proyectos orientados a iDempiere 13 | Descubrir/verificar APIs y build de la release real |
| [shared](../shared/README.es.md) | 11 | Arquitectura, calidad, entornos, tareas y componentes especializados | No se declara soporte global; verificar cada API requerida |
| [core](../core/README.es.md) | 7 | Contribuciones al checkout real del core | Prevalecen sus reglas y release frente a la adaptación fijada |

Total: **78 entradas y 33 nombres distintos**. Las copias de un mismo nombre en distintas versiones son deliberadas. Instalar sólo una copia objetivo de cada nombre en una biblioteca de agente.

## Revisiones exactas por skill

El inventario legible por herramientas enumera nombre, ruta, ámbito, línea objetivo, cantidad de recursos y digest completo de cada entrada. El digest incluye nombres relativos y contenidos de todos los recursos, incluido `SKILL.md`. Mover un recurso o cambiar un asset modifica la revisión; editar solamente un README del repo no la modifica.

El digest del catálogo incluye también las rutas de las entradas e identifica la distribución completa. Es un identificador de contenido, no versionado semántico ni una promesa de compatibilidad. Dos carpetas objetivo con archivos idénticos pueden compartir digest de skill y seguir siendo entradas distintas.

Desde la raíz del repo, con Python 3:

```bash
python3 scripts/catalog_versions.py --check
```

Después de revisar un cambio intencional de skill/recursos:

```bash
python3 scripts/catalog_versions.py --write
python3 scripts/validate_catalog.py
python3 scripts/catalog_versions.py --check
```

`--check` es de solo lectura. `--write` actualiza únicamente `docs/skill-versions.json`; no instala, hace commit ni publica. El validador del catálogo requiere además PyYAML.

## Fuentes y futuras releases

Las guías core adaptadas toman como referencia el commit upstream `75ad26081a1745ab64831567861ad8f9f6f78d36`. Los patrones de componentes se revisaron contra el pack de Hengsin en `a7ec5db8f7459ad67fd0753e0f314ba69021a9cb`. Son bases de procedencia upstream, no versiones de release de esta biblioteca. Consultar [fuentes](SOURCES.md).

Antes de emitir una release: revisar workflows modificados, validar recursos/scripts, actualizar inventario y documentación, y acordar tag y notas de versión. No derivar un número publicado de la carpeta de iDempiere. Las afirmaciones de compatibilidad necesitan evidencia separada de build/runtime.

## Estado instalado frente a estado versionado

[El inventario instalado previo](INSTALLED_SKILLS_INVENTORY.md) registra hashes de entrypoints instalados. Este inventario identifica las skills actuales del repo y todos sus recursos. Tienen propósitos distintos. Mejorar el repo no actualiza automáticamente las skills instaladas; conflictos y selección de destino se revisan por separado.
