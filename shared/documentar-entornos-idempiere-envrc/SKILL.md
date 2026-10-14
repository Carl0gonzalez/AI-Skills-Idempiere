---
name: documentar-entornos-idempiere-envrc
description: Crear, completar, revisar y sincronizar README y guías técnicas de entornos aislados de iDempiere cuya fuente de verdad es un archivo .envrc. Usar al documentar instalación, aislamiento, Java, Maven o Maven Wrapper, P2, Eclipse, workspace, fuentes, Git official/fork, wrappers auxiliares, diagnóstico, contribuciones y troubleshooting, o al comprobar que la documentación coincide con el .envrc actual.
---

# Documentar entornos iDempiere desde `.envrc`

Tratar el `.envrc` como fuente de verdad operativa. Explicar su interfaz y comportamiento sin convertir la documentación en una copia línea por línea del código.

## Flujo

1. Localizar y leer completos `.envrc`, README, `.gitignore` y archivos auxiliares del entorno objetivo. Revisar también el estado Git si existe un repositorio.
2. Generar un inventario reproducible sin ejecutar el entorno:

   ```bash
   python3 <skill-dir>/scripts/inventariar_envrc.py ruta/al/.envrc
   ```

   Usar `--json` cuando se necesite comparar varios entornos o automatizar comprobaciones.
3. Leer [references/contrato-documentacion.md](references/contrato-documentacion.md).
4. Contrastar cada afirmación operativa con una línea, variable, wrapper o comportamiento observable del `.envrc`. Marcar como requisito externo aquello que no pueda verificarse localmente.
5. Conservar la estructura y el tono útiles del README existente. Añadir sólo secciones justificadas por funciones reales.
6. Documentar rutas relativas a la raíz; usar rutas y forks personales únicamente como ejemplos inequívocos.
7. Comparar el inventario final con comandos, variables, archivos generados y `.gitignore` mencionados en la documentación.
8. Si la revisión descubre un defecto del entorno, no ocultarlo en prosa: informarlo y usar `$crear-entornos-idempiere-envrc` si el usuario autorizó corregir código.

## Reglas editoriales

- Escribir en el idioma solicitado y usar Markdown compatible con GitHub.
- No usar emoticonos ni emojis salvo petición expresa o necesidad de conservar una convención existente.
- Explicar primero el resultado para el desarrollador y después los detalles internos.
- Distinguir requisitos, instalación, primer uso, uso diario, contribución y diagnóstico.
- Mostrar comandos copiables con su directorio de ejecución cuando sea relevante.
- No prometer que `direnv allow` descarga, clona o instala componentes si el `.envrc` sólo prepara rutas y wrappers.
- Explicar qué permanece local y qué archivos sí se versionan.
- Explicar la separación entre workspace de Eclipse y clon Git cuando exista.
- Distinguir `origin` y `upstream` por rol. En modo fork, usar etiquetas como `Origin (fork)` y `Upstream (official)`; en modo oficial, `Origin (official)` y `Upstream: n/a`.
- Documentar efectos laterales, requisitos de red y credenciales, salidas no cero y protecciones contra pérdida de datos.
- Mantener ejemplos de versiones, ramas y herramientas alineados con el entorno concreto; no generalizar valores de otra release.

## Comprobación final

- Todos los wrappers inventariados aparecen en la referencia de comandos.
- Todas las rutas generadas relevantes aparecen en la estructura o en la explicación de aislamiento.
- La estrategia Maven coincide con el código: Wrapper o Maven local.
- La versión de Java y la rama se apoyan en el `.envrc` o en una fuente identificada.
- Los modos Git descritos coinciden con la validación implementada.
- Los archivos locales están cubiertos por `.gitignore` o se señala la ausencia.
- Instalación y troubleshooting no incluyen pasos destructivos ni secretos.
- No quedan nombres de usuario, hogares o forks personales presentados como valores predeterminados.
- Los comandos y nombres de variables conservan exactamente mayúsculas, guiones y argumentos.
