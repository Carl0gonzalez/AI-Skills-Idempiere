---
name: desarrollo-sprint-informe
description: Cruza tareas de un sprint con commits, ramas y PR/MR y muestra pendientes con límites de evidencia. Usar al pedir estado del sprint o relación tickets/código; sólo lectura, sin actualizar el gestor.
license: MIT
---

# Tareas y código

Determina sprint, periodo, zona horaria, equipo y repositorios desde el encargo y las fuentes conectadas. Si hay varios sprints vigentes y la elección cambia el resultado, pregunta cuál. Incluye subtareas, tareas cerradas y paginación según el alcance real del gestor; no presupongas la estructura de ClickUp para otros proveedores.

Usa el conector para leer tareas y PR/MR. Para referencias locales ejecuta el auxiliar desde la carpeta resuelta de esta skill:

```bash
python3 scripts/task_commits.py --workspace /ruta/workspace --release-ref origin/main -- ABC-123 ABC-124
```

También acepta `--repo /ruta/repo` repetido, incluidos worktrees enlazados. Busca IDs literales delimitados en mensajes y ramas. Usa sólo referencias locales: muestra cuándo no puede verificar una rama. Por commit informa qué refs lo contienen, y por ref si contiene todos los commits encontrados; eso no demuestra que la tarea completa llegó, ni que esté desplegada. Squash/rebase pueden ocultar equivalencia histórica; contrasta contenido y proveedor antes de concluir. El auxiliar no hace fetch, checkout, commit ni red.

«Sin commits encontrados» significa que no se halló el ID en los repositorios examinados, no que nadie trabajó. No cuentes asuntos iguales como prueba de cambios equivalentes. No confundas develop/staging con producción; las ramas relevantes se indican explícitamente.

Entrega estado por tarea, evidencia Git/PR, fecha o SHA observado, discrepancias y no verificable. Destaca completadas sin evidencia de integración, trabajo con PR pendiente y bloqueos reales. Confirma antes que la relación ticket/código sea correcta. No cambies estados ni publiques el informe en el gestor salvo un encargo adicional que lo incluya.
