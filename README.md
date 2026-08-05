# iDempiere Skills Repository

> Biblioteca versionada de skills reutilizables para diseñar, desarrollar, validar y operar soluciones iDempiere.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![iDempiere 8](https://img.shields.io/badge/iDempiere-8-4B7BEC)](idempiere-8/)
[![iDempiere 10](https://img.shields.io/badge/iDempiere-10-20BF6B)](idempiere-10/)
[![iDempiere 12](https://img.shields.io/badge/iDempiere-12-8854D0)](idempiere-12/)
[![iDempiere 13](https://img.shields.io/badge/iDempiere-13-E67E22)](idempiere-13/)

Bienvenido al repositorio de skills para iDempiere. Este repositorio centraliza capacidades reutilizables para asistentes de desarrollo, permitiendo mantener instrucciones consistentes y separadas por versión mayor de iDempiere.

Su objetivo es facilitar el trabajo seguro sobre plugins OSGi, Application Dictionary, PIPO/2Pack, PostgreSQL, Jenkins y documentación funcional, evitando que instrucciones diseñadas para una versión se apliquen accidentalmente a otra.

---

## Contenido

- [Estructura del repositorio](#estructura-del-repositorio)
- [Reglas de organización](#reglas-de-organización)
- [Skills disponibles](#skills-disponibles)
- [Meta-skills: crear y revisar skills](#meta-skills-crear-y-revisar-skills)
- [Matriz de versiones](#matriz-de-versiones)
- [Instalación desde un clon local](#instalación-desde-un-clon-local)
- [Uso en entornos aislados con direnv](#uso-en-entornos-aislados-con-direnv)
- [Política de seguridad para PostgreSQL](#política-de-seguridad-para-postgresql)
- [Contribuciones y mantenimiento](#contribuciones-y-mantenimiento)
- [Licencia](#licencia)

---

## Estructura del repositorio

```text
.
├── idempiere-8/                 # Skills para repositorios iDempiere 8
├── idempiere-10/                # Skills para repositorios iDempiere 10
├── idempiere-12/                # Skills para repositorios iDempiere 12
├── idempiere-13/                # Skills para repositorios iDempiere 13
├── LICENSE                      # Licencia MIT
└── README.md                    # Catálogo y guía de uso
```

Cada carpeta de versión contiene una copia autónoma de las skills compatibles con esa línea de iDempiere. Esto permite respaldar, enlazar o instalar un conjunto completo sin mezclar instrucciones de distintas plataformas.

| Directorio | Alcance | Uso recomendado |
|---|---|---|
| [`idempiere-8`](idempiere-8/README.md) | iDempiere 8 | Proyectos, plugins y target platforms basados en v8. |
| [`idempiere-10`](idempiere-10/README.md) | iDempiere 10 | Proyectos, plugins y target platforms basados en v10. |
| [`idempiere-12`](idempiere-12/README.md) | iDempiere 12 | Proyectos, plugins y target platforms basados en v12. |
| [`idempiere-13`](idempiere-13/README.md) | iDempiere 13 | Proyectos, plugins y target platforms basados en v13. |

---

## Reglas de organización

Para mantener un catálogo claro, reutilizable y seguro, toda contribución debe respetar estas reglas:

| Regla | Criterio |
|---|---|
| **Carpetas dedicadas** | Cada skill debe vivir en su propia carpeta y contener `SKILL.md`. |
| **Metadatos claros** | El frontmatter debe incluir `name` y `description`, indicando capacidad y criterios de activación. |
| **Alcance focalizado** | Una skill debe resolver una capacidad reutilizable, no agrupar tareas inconexas. |
| **Separación por versión** | Toda skill específica de plataforma debe estar disponible bajo la versión de iDempiere que corresponda. |
| **Portabilidad** | No incluir rutas personales, nombres de usuario, credenciales, hosts, puertos ni supuestos de una máquina local. |
| **Validación** | Validar toda skill modificada antes de incorporarla al respaldo. |
| **No duplicación** | Preferir actualizar una skill existente antes de crear otra con el mismo propósito. |

### Estructura mínima de una skill

```text
nombre-de-la-skill/
└── SKILL.md
```

Una skill puede incluir `scripts/`, `references/` o `assets/` únicamente cuando esos recursos sean necesarios para un flujo repetible o determinista.

---

## Skills disponibles

Las siguientes skills están disponibles en cada directorio de versión, salvo que una futura variante requiera una especialización adicional.

| Skill | Descripción | Propósito principal |
|---|---|---|
| [`idempiere-local-postgres`](idempiere-12/idempiere-local-postgres/SKILL.md) | Diagnóstico seguro de PostgreSQL para iDempiere. | Inspecciona datos, esquema y configuración con sesiones de solo lectura por defecto. |
| [`idempiere-migration-review`](idempiere-12/idempiere-migration-review/SKILL.md) | Auditoría de propuestas de migración y módulos. | Revisa modelos, DDL, Application Dictionary y consistencia OSGi. |
| [`idempiere-model-designer`](idempiere-12/idempiere-model-designer/SKILL.md) | Diseño de modelos de datos y arquitectura funcional. | Define entidades, relaciones, documentos y reglas ERP. |
| [`idempiere-pipo-integrity-review`](idempiere-12/idempiere-pipo-integrity-review/SKILL.md) | Preflight de PackOut/PIPO. | Verifica dependencias y compatibilidad entre diccionario y base de datos. |
| [`idempiere-plugin-compiler`](idempiere-12/idempiere-plugin-compiler/SKILL.md) | Compilación de plugins OSGi. | Descubre el builder del repositorio y reporta artefactos generados. |
| [`idempiere-plugin-component-developer`](idempiere-12/idempiere-plugin-component-developer/SKILL.md) | Desarrollo de componentes internos. | Implementa procesos, callouts, validadores y factories. |
| [`idempiere-plugin-designer`](idempiere-12/idempiere-plugin-designer/SKILL.md) | Diseño técnico de plugins. | Convierte diseños funcionales en especificaciones Java y OSGi. |
| [`idempiere-plugin-manual-generator`](idempiere-12/idempiere-plugin-manual-generator/SKILL.md) | Generación de manuales funcionales. | Produce documentación de uso y guías de prueba desde código y metadatos. |
| [`idempiere-plugin-readme`](idempiere-12/idempiere-plugin-readme/SKILL.md) | Documentación de repositorios de plugins. | Crea y actualiza README en inglés basados en el contenido real del proyecto. |
| [`idempiere-plugin-test-developer`](idempiere-12/idempiere-plugin-test-developer/SKILL.md) | Desarrollo de pruebas para plugins. | Define pruebas unitarias, mocks y estrategias de aislamiento. |
| [`jenkinsfile-developer`](idempiere-12/jenkinsfile-developer/SKILL.md) | Mantenimiento de pipelines Jenkins. | Estandariza compilación y publicación de documentación por versión. |
| [`skill-architect`](idempiere-12/skill-architect/SKILL.md) | Diseño de nuevas skills. | Crea capacidades enfocadas cuando no existe una skill adecuada. |
| [`skill-reviewer`](idempiere-12/skill-reviewer/SKILL.md) | Revisión de skills antes de adoptarlas. | Evalúa nombre, activación, alcance, estructura y riesgo de duplicación. |

---

## Meta-skills: crear y revisar skills

`skill-architect` y `skill-reviewer` no dependen de iDempiere. Son meta-skills para mantener la calidad del propio catálogo: están disponibles en las tres versiones para que cada entorno pueda crear o evaluar capacidades nuevas sin mezclar dependencias de plataforma.

| Skill | Función | Cuándo usarla | Resultado esperado |
|---|---|---|---|
| [`skill-architect`](idempiere-12/skill-architect/SKILL.md) | Diseña y estructura una skill nueva y reutilizable. | Cuando hay un flujo repetible que no está cubierto por una skill existente. | Nombre, descripción, ubicación, estructura y contenido de una skill acotada. |
| [`skill-reviewer`](idempiere-12/skill-reviewer/SKILL.md) | Audita una skill antes de incorporarla o modificarla. | Antes de hacer commit, instalar una skill o cuando hay dudas sobre alcance o duplicación. | Veredicto, hallazgos, correcciones propuestas y recomendación final. |

### Cómo trabajan juntas

```text
Necesidad repetible
        │
        ▼
skill-architect ──► ¿Existe una skill equivalente?
        │                    │
        │ no                 └── sí: actualizar o reutilizar la existente
        ▼
Diseño y creación de una skill enfocada
        │
        ▼
skill-reviewer ───► Revisión de nombre, activación, alcance y estructura
        │
        ▼
Corrección necesaria o aprobación para adopción
```

`skill-architect` no debe generar una skill para una actividad puntual, ambigua o ya cubierta. Antes de crearla, busca solapamientos, propone un nombre en minúsculas con guiones, redacta una descripción que indique cuándo se activa y limita los archivos auxiliares a los realmente necesarios.

`skill-reviewer` no crea cambios por defecto: primero evalúa si la skill es específica, reutilizable y detectable por un agente. Su salida clasifica el resultado como aprobación, aprobación con ajustes menores, revisión necesaria o rechazo por duplicación/amplitud excesiva. Solo reescribe la skill cuando se le solicita expresamente.

### Ejemplo de uso: crear una skill

Usa este prompt cuando quieras convertir un procedimiento repetido en una skill:

```text
Quiero crear una skill reutilizable para revisar scripts SQL de migración antes de ejecutarlos.

Debe detectar operaciones destructivas, validar convenciones de nombres y exigir que se indique una estrategia de reversión. Revisa primero las skills disponibles para evitar duplicados. Si procede crearla, propón su nombre, descripción, estructura mínima y el contenido completo de SKILL.md. No agregues scripts ni carpetas auxiliares salvo que sean necesarios.
```

El resultado esperado es una propuesta como `sql-migration-safety-review`, con criterios claros de activación, límites de seguridad, flujo de revisión y contrato de salida.

### Ejemplo de uso: revisar una skill antes de adoptarla

Usa este prompt para validar una skill existente:

```text
Revisa la skill ubicada en <ruta-de-la-skill> antes de incorporarla al catálogo.

Evalúa el nombre, el frontmatter, los criterios de activación, el alcance, el riesgo de duplicación, las instrucciones y la estructura de archivos. Devuelve un veredicto, hallazgos concretos, correcciones sugeridas, frontmatter revisado si aplica y una recomendación final. No modifiques archivos todavía.
```

> Flujo recomendado: crea o actualiza la skill con `skill-architect`, revísala con `skill-reviewer`, aplica las correcciones aprobadas y valida el resultado antes de hacer commit.

---

## Matriz de versiones

| Área | iDempiere 8 | iDempiere 10 | iDempiere 12 | iDempiere 13 |
|---|:---:|:---:|:---:|:---:|
| Modelado, migración y PIPO | ✓ | ✓ | ✓ | ✓ |
| Diseño, desarrollo y pruebas de plugins | ✓ | ✓ | ✓ | ✓ |
| Documentación y manuales | ✓ | ✓ | ✓ | ✓ |
| PostgreSQL seguro | ✓ | ✓ | ✓ | ✓ |
| Jenkins version-aware | ✓ | ✓ | ✓ | ✓ |
| Builder y rama de target platform | Deben verificarse en el repositorio objetivo | Deben verificarse en el repositorio objetivo | Basados en la configuración del repositorio objetivo | Deben verificarse en el repositorio objetivo |

> Ninguna variante debe reutilizar automáticamente una imagen Docker o rama de target platform de otra versión mayor. La skill Jenkins exige descubrir y configurar el builder correspondiente al proyecto.

---

## Instalación desde un clon local

También es válido clonar este repositorio y pedir a cualquier asistente de IA que instale las skills desde la carpeta local. Así se conserva una copia versionada, se selecciona explícitamente la variante de iDempiere y el propio agente realiza la instalación según su mecanismo disponible.

1. Clonar este repositorio en una ubicación elegida por el usuario.
2. Identificar el directorio de la versión requerida: `idempiere-8/`, `idempiere-10/`, `idempiere-12/` o `idempiere-13/`.
3. Copiar el siguiente prompt y reemplazar los valores entre `<...>`.

```text
Necesito instalar un conjunto local de skills para mi agente de IA.

Origen de las skills: <ruta-local-del-clon>/idempiere-<8|10|12|13>/
Versión objetivo de iDempiere: <8|10|12|13>

Inspecciona esa carpeta, identifica todas las skills que contengan un archivo SKILL.md y propón instalarlas o enlazarlas en la biblioteca de skills que utiliza este entorno. Antes de modificar archivos, indícame:
1. Las skills detectadas y la ruta de destino que usarás.
2. Si existe alguna skill con el mismo nombre y cómo resolverás el conflicto.
3. Si copiarás o crearás enlaces simbólicos, con las implicaciones de cada alternativa.

No sobrescribas ni elimines ninguna skill existente sin mi confirmación explícita. Mantén la instalación limitada a la versión de iDempiere indicada y confirma al final qué skills quedaron disponibles.
```

El prompt no presupone un proveedor ni una ruta de instalación concreta; funciona como instrucción para Codex, ChatGPT, Claude, Gemini, Cursor, Windsurf u otro agente con acceso al sistema de archivos local.

| Ventaja | Resultado |
|---|---|
| Sin rutas fijas | El usuario decide dónde mantener el clon. |
| Selección controlada | Solo se instala la versión compatible con el proyecto. |
| Instalación segura | El agente debe informar conflictos y pedir autorización antes de sobrescribir. |
| Actualización simple | Basta actualizar el clon y repetir la instalación o los enlaces. |

> Verifica siempre que la versión elegida en el prompt coincida con la versión del repositorio iDempiere donde se trabajará.

---

## Uso en entornos aislados con direnv

Se recomienda usar `direnv` para cargar exclusivamente las skills de la versión correspondiente al repositorio abierto. Esto reduce el riesgo de compilar, diseñar o diagnosticar con supuestos de otra versión de iDempiere.

### Ejemplo de `.envrc`

Crear un `.envrc` dentro del repositorio de trabajo:

```sh
# Seleccionar únicamente la versión que usa este repositorio.
export IDEMPIERE_VERSION=12

# Mantener el estado de Codex aislado por proyecto.
export CODEX_HOME="$PWD/.codex"

# Definir esta variable fuera del repositorio o mediante la configuración de direnv.
export SKILLS_BACKUP_ROOT="${SKILLS_BACKUP_ROOT:?Configure SKILLS_BACKUP_ROOT antes de permitir este .envrc}"

mkdir -p "$CODEX_HOME/skills"

for skill_dir in "$SKILLS_BACKUP_ROOT/idempiere-$IDEMPIERE_VERSION"/*; do
  [ -d "$skill_dir" ] || continue
  ln -sfn "$skill_dir" "$CODEX_HOME/skills/$(basename "$skill_dir")"
done
```

Luego ejecutar:

```sh
direnv allow
```

### Beneficios del aislamiento

| Beneficio | Resultado |
|---|---|
| Selección explícita de versión | Cada proyecto carga skills acordes a su plataforma. |
| Menor contaminación de contexto | Evita instrucciones, builders o patrones de otra versión. |
| Configuración portable | La ubicación del respaldo se entrega mediante una variable de entorno. |
| Reproducibilidad | El equipo puede compartir un `.envrc.example` sin publicar rutas personales ni credenciales. |

---

## Política de seguridad para PostgreSQL

La skill `idempiere-local-postgres` aplica una política conservadora de acceso a datos:

| Control | Comportamiento |
|---|---|
| Modo predeterminado | Todas las conexiones se abren en solo lectura. |
| Consultas permitidas | `SELECT`, `SHOW` y `EXPLAIN`. |
| Operaciones consideradas escritura | `INSERT`, `UPDATE`, `DELETE`, `MERGE`, DDL y funciones con efectos secundarios. |
| Primera verificación | Se informa base, objetivo, SQL propuesto y posible impacto. |
| Segunda verificación | Se solicita confirmación final sobre la operación exacta antes de escribir. |
| Cambio de alcance | Cualquier modificación a SQL, filtros, destino o impacto reinicia las dos verificaciones. |

Esta política permite diagnosticar con seguridad y reduce el riesgo de cambios accidentales en bases de datos iDempiere.

---

## Contribuciones y mantenimiento

Antes de agregar o actualizar una skill:

1. Confirmar que no existe una skill equivalente que deba actualizarse.
2. Definir la versión o versiones de iDempiere a las que aplica.
3. Mantener las instrucciones breves, operativas y libres de información local.
4. Validar el frontmatter y la estructura de la skill.
5. Verificar que no se hayan agregado rutas personales, credenciales o configuraciones específicas de un equipo.
6. Actualizar este catálogo si se incorpora una nueva capacidad.

Para cambios complejos, revisar la skill con `skill-reviewer` antes de adoptarla.

---

## Licencia

Este repositorio se distribuye bajo la [Licencia MIT](LICENSE).

Copyright © 2026 Carlo González.
