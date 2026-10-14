# Contrato de documentación del entorno

## Tabla de contenido

- Fuente de verdad
- Estructura recomendada
- Matriz de trazabilidad
- Contenido por tema
- Control de calidad

## Fuente de verdad

Ordenar la evidencia así:

1. `.envrc` y wrappers generados;
2. archivos versionados del mismo entorno;
3. metadatos del clon de iDempiere;
4. documentación oficial de la release;
5. ejemplos claramente rotulados.

No inferir una función a partir del nombre de un comando. Leer su heredoc completo. No afirmar que un directorio se ignora sin revisar `.gitignore`.

## Estructura recomendada

Adaptar, sin forzar secciones vacías:

1. propósito y alcance;
2. características principales;
3. requisitos del sistema;
4. arquitectura de aislamiento y árbol de directorios;
5. instalación desde cero;
6. primera carga con direnv;
7. obtención de fuentes;
8. Java y Maven;
9. Eclipse, P2 y separación workspace/fuentes;
10. modelo Git oficial/fork;
11. referencia de comandos;
12. flujo cotidiano y contribuciones;
13. diagnóstico y troubleshooting;
14. seguridad, datos locales y `.gitignore`;
15. licencia, si existe.

## Matriz de trazabilidad

Antes de cerrar, mantener una matriz de trabajo, aunque no tenga que publicarse:

| Hecho documentado | Evidencia esperada |
|---|---|
| Rama base | variable de rama o metadatos del clon |
| Java | candidatos y validación de versión |
| Maven | `MAVEN_HOME` o invocación de `mvnw` |
| Repo Maven | settings y `maven.repo.local` |
| P2 | variable y argumento de configuración de Eclipse |
| Workspace | variable y `-data` |
| Comando | heredoc del wrapper y lista de `chmod` |
| Git mode | archivo persistido, ramas condicionales y remotos |
| Archivo ignorado | patrón efectivo de `.gitignore` |

Resolver cualquier fila sin evidencia: corregir la documentación, solicitar la fuente o declarar la limitación.

## Contenido por tema

### Aislamiento

Explicar qué problema evita cada ruta, no sólo enumerarla. Indicar si la recarga crea directorios, settings o wrappers. Aclarar qué cachés pueden crecer y cuáles se pueden regenerar.

### Git

Incluir un diagrama textual simple o una explicación equivalente cuando haya forks. Describir `origin` y `upstream` por destino y propósito, no sólo por nombre. Separar sincronización segura de creación de ramas y apertura de Pull Requests.

### Comandos

Para cada wrapper indicar sintaxis, precondiciones, efectos, salida esperada y fallos habituales. No inventar opciones. Si un comando cambia ramas, hace push o accede a red, decirlo de forma visible.

### Troubleshooting

Derivar problemas de comprobaciones reales: JDK, ejecutabilidad del Wrapper, repo ausente, árbol Git sucio, remotos contradictorios, SSH, Eclipse y permisos de direnv. Preferir diagnóstico antes que reinstalación.

## Control de calidad

- Verificar enlaces y anclas locales.
- Mantener ejemplos sin secretos.
- Evitar rutas absolutas del autor.
- Evitar cifras de tamaño o tiempos no verificadas.
- No ocultar limitaciones de soporte por sistema operativo.
- Revisar que bloques de código sean copiables y estén correctamente cerrados.
- Comparar el README contra la salida de `inventariar_envrc.py` después de cada cambio funcional.
