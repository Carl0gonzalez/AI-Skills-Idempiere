# Versiones objetivo

**Español** | [English](VERSIONING.md)

La línea iDempiere y la revisión de una skill son conceptos distintos: la carpeta identifica la plataforma y el historial Git registra cambios de instrucciones y recursos.

| Carpeta | Skills | Destino |
|---|---:|---|
| [idempiere-8](../idempiere-8/README.es.md) | 15 | iDempiere 8 |
| [idempiere-10](../idempiere-10/README.es.md) | 15 | iDempiere 10 |
| [idempiere-12](../idempiere-12/README.es.md) | 15 | iDempiere 12 |
| [idempiere-13](../idempiere-13/README.es.md) | 15 | iDempiere 13 |
| [idempiere-14](../idempiere-14/README.es.md) | 15 | iDempiere 14 en desarrollo |

| [shared](../shared/README.es.md) | 14 | Workflows comunes |
| [core](../core/README.es.md) | 7 | Contribuciones core |

Seleccionar un conjunto versionado que corresponda al proyecto real. No cargar varias copias con el mismo nombre. Los workflows comunes requieren revisar APIs; los del core siguen las reglas de contribución del checkout objetivo.

El catálogo contiene **96 entradas y 33 nombres distintos**. Una carpeta expresa un destino, no una prueba runtime. Para iDempiere 14, revisar commit de desarrollo, JDK y builder seleccionados. Seguir el toolchain del proyecto sin copiar configuraciones de una release anterior.

Diseño de modelos, diseño técnico y revisión comparten una fuente en `shared/`. Las copias versionadas se mantienen con `python3 codex/sync_design_skills.py`. No instalar copias de igual nombre junto a las globales. Ver la [guía](../codex/GUIA.es.md).
