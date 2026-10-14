---
name: gestionar-tareas
description: Mantén el contexto mínimo y persistente de tareas de un repositorio que use `.agents/tareas/`. Usar al iniciar, continuar, revisar, actualizar o cerrar una tarea, o cuando el usuario pida retomar trabajo previo.
---

# Flujo

1. Resolver la carpeta de tareas como `.agents/tareas/` desde la raíz del repositorio actual. Si no existe, informar que no hay un registro de tareas configurado y no crear uno salvo petición explícita.
2. No leer ni abrir fichas de tarea por defecto.
3. Leer una ficha sólo cuando el usuario solicite explícitamente revisar, retomar o actualizar una tarea.
4. Crear o actualizar una ficha desde `_plantilla.md` únicamente ante una instrucción explícita de registrar o actualizar la tarea.
5. Mantener cada campo en una línea corta; registrar sólo el estado actual, no un diario.
6. Al recibir que una tarea concluyó, cambiar su estado a `CERRADA` y no volver a editarla salvo instrucción explícita.
