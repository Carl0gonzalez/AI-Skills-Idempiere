---
name: crear-entornos-idempiere-envrc
description: Crear, adaptar, revisar y mantener entornos locales aislados de desarrollo de iDempiere basados en direnv y archivos .envrc. Usar al incorporar una versión de iDempiere, migrar un entorno existente, corregir aislamiento de Java/Maven/P2/Eclipse/Git, revisar wrappers locales o validar seguridad, portabilidad e idempotencia de un .envrc en Linux.
---

# Crear entornos iDempiere con `.envrc`

Construir el entorno desde los archivos existentes y desde los requisitos reales de la versión. Preservar lo correcto; no asumir que el `.envrc` más nuevo sirve sin adaptación para releases anteriores.

## Flujo

1. Localizar la raíz de trabajo, todos los `.envrc`, README, `.gitignore`, archivos de configuración local y el estado Git de cada repositorio aplicable.
2. Leer completo el `.envrc` objetivo y comparar sólo los hermanos útiles. Inventariar versión, rama, JDK, estrategia Maven, rutas aisladas, wrappers y modelo de remotos.
3. Leer [references/contrato-envrc.md](references/contrato-envrc.md) antes de crear o modificar un entorno.
4. Ejecutar el análisis estático antes de editar. Si el archivo aún no existe, auditar la referencia elegida y ejecutar el auditor sobre el primer candidato inmediatamente después de generarlo:

   ```bash
   python3 <skill-dir>/scripts/auditar_envrc.py ruta/al/.envrc
   ```

5. Derivar una matriz breve de requisitos. Verificar en los archivos del proyecto o fuentes oficiales cualquier versión que no esté fijada por el usuario. No copiar valores de otra release por semejanza.
6. Aplicar el cambio mínimo y mantener juntas las invariantes de aislamiento, portabilidad, seguridad Git e idempotencia.
7. Actualizar `.gitignore` cuando el entorno genere estado local. Si existe documentación, invocar también `$documentar-entornos-idempiere-envrc` para sincronizarla.
8. Validar de nuevo con el auditor y `bash -n`. Probar la evaluación con `direnv` únicamente en una copia temporal cuando el `.envrc` cree archivos o regenere wrappers.

## Reglas de implementación

- Tratar `.envrc` como Bash evaluado por direnv, no como un script ejecutado en un proceso independiente.
- Reservar `set -euo pipefail` para wrappers generados. No imponerlo globalmente al `.envrc` sin auditar cada expansión y el efecto sobre `direnv`.
- Resolver la raíz desde la ubicación del `.envrc`; no incluir usuarios, hogares ni forks personales.
- Citar todas las rutas y argumentos derivados de variables. Soportar espacios en la ruta raíz.
- Mantener cachés, repositorios, workspaces, instalaciones y wrappers dentro de la raíz del entorno.
- Separar el workspace de Eclipse del clon Git salvo que el usuario indique expresamente otro diseño.
- Preferir el Maven Wrapper cuando la release lo incluya y fije. Usar Maven local sólo cuando el contrato de esa release lo requiera.
- Generar wrappers físicos en un directorio local añadido a `PATH`; direnv no exporta funciones de shell al proceso interactivo.
- Hacer que una recarga regenere sólo artefactos derivados y nunca destruya datos de usuario.
- Validar configuración persistida antes de confiar en ella. Citar valores al escribir archivos de configuración y evitar evaluar contenido no confiable salvo que el formato sea deliberadamente un archivo shell controlado.
- Fallar de forma explícita ante directorios de clon no vacíos, remotos incoherentes, cambios Git locales o divergencias que impidan fast-forward.
- No ejecutar automáticamente `reset --hard`, `clean -fd`, `push --force`, borrados recursivos ni cambios de remoto silenciosos.

## Validación proporcional

- Ejecutar `bash -n` siempre.
- Ejecutar `<skill-dir>/scripts/auditar_envrc.py` sobre el archivo cambiado y, si se extrajo un patrón compartido, sobre los hermanos afectados.
- Si `shellcheck` está disponible, revisar por separado el cuerpo superior y los wrappers extraídos; documentar falsos positivos de heredoc.
- Probar rutas con espacios mediante una copia temporal.
- Probar dos recargas consecutivas y comparar artefactos derivados.
- Simular Git con repositorios temporales locales; no depender de red ni credenciales para pruebas básicas.
- Comprobar escenarios ausentes, válidos e inválidos para configuración persistida, repo, Java, Maven y Eclipse.

No modificar clones reales, remotos, ramas o credenciales sólo para validar la skill.
