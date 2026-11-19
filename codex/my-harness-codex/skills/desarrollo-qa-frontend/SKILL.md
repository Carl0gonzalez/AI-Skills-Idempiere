---
name: desarrollo-qa-frontend
description: Reproduce fallos y verifica pantallas en navegador real con pasos, consola, red y capturas pertinentes. Usar para QA de UI o comprobar un cambio web; no sustituye los tests automatizados del proyecto ni autoriza cambios en datos externos.
license: MIT
---

# Verificación de UI

Confirma qué versión y URL contienen el cambio y qué rol se prueba. Un cambio local se comprueba en local; staging puede tener otro código. Usa primero herramientas del navegador disponibles en la sesión y su documentación; utiliza la suite del repositorio cuando corresponda. No instales un CLI global como requisito de esta skill.

Escribe el resultado esperado antes del recorrido. Reproduce el camino relevante, un error o límite si aporta, y registra pasos, resultado, consola y petición pertinente. Espera una señal verificable de carga antes de declarar que faltan datos. Revisa menús/diálogos que se montan fuera del contenedor observado. Contrasta persistencia con una fuente autorizada cuando sea importante y esté accesible.

Navegar puede disparar acciones: verifica el significado de un control antes de pulsarlo. Crear, borrar, guardar, enviar y cambiar estados exige que forme parte del encargo para ese entorno. Respeta la autorización ya recibida; pide aclaración sólo si el entorno o efecto queda ambiguo. Para credenciales, usa sesión existente o login del usuario; no pidas que pegue contraseñas en el chat. Trata estados de sesión como secretos.

Un 404 en navegador y 200 en otra herramienta no demuestra CORS: compara URL, método, identidad, cabeceras, redirecciones, proxy y service worker; usa consola/red para sostener la causa. No atribuyas una pantalla vacía al build ni una latencia a CPU sin evidencia.

Prueba viewport y temas que cubra el cambio; no impongas claro/oscuro si la aplicación no los ofrece. Si no tienes consola o red en la herramienta disponible, declara ese límite.

Entrega veredicto (PASA/FALLA/NO EJECUTADO o INCONCLUSO), pasos, esperado, observado, entorno y versión, evidencia y lo no cubierto. La prueba manual no se presenta como E2E automatizado. Captura sólo si ayuda y revisa datos sensibles antes de compartirla. Usa las skills de comentar/adjuntar sólo si se pidió registrar el resultado. Cierra únicamente sesiones de navegador que hayas creado para la tarea, nunca todas las del usuario.
