# Respaldo público de skills de Codex

Inventario verificado el 19 de noviembre de 2026. La rama de partida en GitHub y el checkout local tenían el mismo commit base, `805de2b3891b19f174454807fabceab0651bd0e6`.

| Origen instalado | Resultado de la comparación | Fuente para restaurar |
|---|---|---|
| 18 skills de iDempiere y soporte instaladas como carpetas personales | 17 coincidían archivo por archivo, omitiendo cachés de Python. Se incorporó la regla de traducciones del Diccionario de Aplicaciones de la copia instalada de arquitectura. | [shared](../shared/) y [core](../core/) |
| Tres skills de diseño y revisión enlazadas y dos roles iDempiere | Los enlaces y roles instalados coincidían con los destinos y TOML producidos por el instalador. Las copias de iDempiere 8, 10, 12, 13 y 14 coinciden con sus fuentes comunes. | [Especialistas iDempiere](../codex/README.md) |
| Siete skills de desarrollo enlazadas y seis roles generales | Los enlaces apuntaban al paquete local y los TOML instalados coincidían con sus originales. La edición pública conserva los auxiliares y pruebas y omite referencias a la integración documental privada. | [Flujos de desarrollo](../codex/my-harness-codex/README.md) |

El respaldo cubre **28 skills personales y 8 roles publicables**. El catálogo iDempiere conserva sus 96 entradas, incluidas las variantes por versión, y el paquete general agrega siete skills. Las skills del formato documental interno, sus agentes, plantillas, muestras y materiales privados quedan excluidos. Los componentes distribuidos por Codex y sus plugins se recuperan con sus respectivos instaladores. Este repositorio guarda fuentes reutilizables. Las credenciales, la configuración personal, los manifiestos de instalación y los informes locales pertenecen al entorno donde se generaron.

## Restauración

1. Clona este repositorio y conserva el checkout en una ruta estable si vas a instalar mediante enlaces.
2. Para las skills de `shared/` y `core/`, copia a la biblioteca personal cada carpeta que necesites, salvo las tres que instala el paso siguiente. Para una variante específica de iDempiere, usa la carpeta de la versión del proyecto y evita duplicar nombres con la instalación personal.
3. Para las tres skills de diseño/revisión y los dos especialistas, ejecuta `python3 codex/install.py` desde la raíz. Revisa la simulación y repite con `--apply` para instalar.
4. Para las siete skills de desarrollo y sus roles, entra a `codex/my-harness-codex/` y ejecuta `python3 scripts/install.py`. Revisa la simulación antes de usar `--apply`. Si existe una instalación previa desde otra ruta, conserva esa instalación o usa su instalador de origen para retirarla antes de reinstalar. Revisa cualquier personalización antes de sustituirla.
5. Abre un chat nuevo para comprobar el descubrimiento de skills y roles.

## Verificación

- Se revisaron los archivos del árbol candidato y los 214 blobs alcanzables desde la rama pública anterior. La búsqueda incluyó firmas de claves privadas, formatos habituales de tokens, JWT, credenciales en URLs, asignaciones sospechosas y referencias a material privado. La coincidencia de credenciales fue un comentario de ejemplo que enumera variables de entorno sin valores. Esta revisión por patrones tiene cobertura limitada.
- Pasaron 22 pruebas locales de los dos paquetes. La validación del paquete de desarrollo encontró siete skills y seis roles sin errores, y la comprobación de sincronización de las copias versionadas reportó cero diferencias.
- Las pruebas cubrieron los instaladores con destinos temporales. El respaldo no requirió reinstalar las skills ni ejecutar flujos externos de tickets o despliegue.

```bash
python3 codex/sync_design_skills.py --check
python3 -B -m unittest discover -s codex/tests -v
(
  cd codex/my-harness-codex
  python3 -B scripts/validate.py
  python3 -B -m unittest discover -s tests -v
)
```
