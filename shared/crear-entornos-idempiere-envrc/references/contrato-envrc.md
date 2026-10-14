# Contrato técnico para entornos iDempiere

## Tabla de contenido

- Invariantes
- Ciclo de carga
- Maven y Java
- Git y colaboración
- Wrappers y diagnóstico
- Casos de prueba

## Invariantes

Un entorno aislado debe conservar dentro de su raíz, según corresponda:

- repositorio y configuración de Maven;
- caché de Maven Wrapper;
- caché P2 y configuración de Eclipse;
- instalación de Eclipse;
- workspace separado;
- fuentes y clon Git;
- scripts o wrappers generados;
- configuración Git local del desarrollador.

Usar variables semánticas, por ejemplo `SOURCES_DIR`, `IDEMPIERE_REPOSITORY`, `ECLIPSE_HOME`, `ECLIPSE_WORKSPACE`, `MVN_LOCAL_REPO`, `MAVEN_USER_SETTINGS`, `ECLIPSE_P2` y `BIN_DIR`. Los nombres exactos pueden variar por versión, pero una misma ruta no debe tener significados contradictorios.

Ignorar en Git los artefactos generados. Normalmente esto incluye `.m2/`, `.p2/`, `.local-bin/`, `eclipse/`, `workspace-*/`, `sources/` y archivos locales con URLs o preferencias del desarrollador.

## Ciclo de carga

Direnv evalúa `.envrc` con Bash y captura el entorno resultante. Por eso:

- una función declarada en `.envrc` no se convierte de forma fiable en comando del shell del usuario;
- un wrapper físico sí puede añadirse a `PATH`;
- `return` es preferible a `exit` al abortar la carga;
- cada recarga puede volver a ejecutar `mkdir`, escrituras y generación de wrappers;
- las escrituras deben ser atómicas cuando un archivo incompleto pueda romper el entorno;
- las variables heredadas como `MAVEN_OPTS` no deben acumular la misma opción en cada recarga.

Usar heredocs con delimitador citado cuando el wrapper deba expandir variables al ejecutarse. Usar delimitador sin citar sólo cuando los valores deban fijarse al generar el wrapper. Auditar `"$@"`, `$?`, arrays y variables opcionales para evitar expansión prematura.

## Maven y Java

Determinar por release la rama Git, el JDK, Tycho, la revisión del proyecto, la presencia y versión del Maven Wrapper y la necesidad de Maven local. No copiar valores de otra release por semejanza.

Si existe Wrapper oficial, invocarlo desde el clon y aislar tanto `MAVEN_USER_HOME` como `maven.repo.local`. Si se usa Maven local, aislar `MAVEN_HOME`, settings y repositorio. No escribir configuración derivada dentro del clon si eso ensucia innecesariamente `git status`.

Validar la versión real de Java, no sólo el nombre del directorio. Permitir candidatos configurables y emitir una corrección accionable si no se encuentra el JDK.

## Git y colaboración

En modo oficial, `origin` apunta al repositorio oficial y `upstream` no es necesario. En modo fork, `origin` apunta al fork del desarrollador y `upstream` al repositorio oficial.

Persistir el modo y las URLs fuera del archivo versionado. Antes de clonar o sincronizar, validar modo, URLs y remotos reales. No reinterpretar un modo desconocido como oficial. Para sincronizar, exigir árbol limpio y usar fetch más merge/pull `--ff-only`. No reparar divergencias automáticamente.

Al crear una rama de trabajo, actualizar primero la referencia base remota y crear la rama desde esa referencia verificada. Rechazar nombres vacíos o ya existentes con un mensaje claro.

## Wrappers y diagnóstico

Cada wrapper debe usar `#!/bin/bash`, `set -euo pipefail`, rutas citadas y comprobaciones previas. El comando doctor debe ser de sólo lectura y devolver estado distinto de cero ante fallos que bloqueen el entorno.

El diagnóstico debe distinguir configuración deseada de estado real. Mostrar etiquetas inequívocas, por ejemplo `Origin (fork)` y `Upstream (official)`, y validar raíz, JDK, Maven, clon, rama, cambios locales, remotos, modo Git, Eclipse, workspace, P2 y comandos auxiliares. Las comprobaciones de red y SSH deben ser opcionales, rápidas y no bloquear el resto.

## Casos de prueba

Cubrir raíz con espacios; dos recargas consecutivas; Java ausente o incorrecto; repo ausente, presente o directorio no vacío; configuración Git ausente, inválida o válida; remotos contradictorios; rama base remota, obsoleta o divergente; árbol sucio; Maven ausente o no ejecutable; Eclipse ausente; red y SSH no disponibles; y ausencia de operaciones destructivas implícitas.
