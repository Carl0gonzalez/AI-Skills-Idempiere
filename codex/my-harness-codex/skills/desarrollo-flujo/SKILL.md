---
name: desarrollo-flujo
description: Organiza desarrollo de funcionalidades y cambios entre módulos o repositorios, desde requisitos hasta verificación. Usar al pedir un flujo completo de desarrollo, plan de implementación o coordinación de una entrega; para tareas puntuales, aplicar sólo las etapas pertinentes.
license: MIT
---

# Desarrollo proporcional al cambio

Identifica el resultado pedido, repositorios, versión, lenguaje, convenciones y comandos reales. Lee las instrucciones locales aplicables y busca una implementación vecina. Los requisitos del usuario y las políticas del proyecto mandan sobre este flujo.

Elige las etapas que aporten una decisión o una verificación necesaria:

| Necesidad | Rol o procedimiento |
|---|---|
| Ticket ambiguo, alcance o aceptación | `desarrollo-producto`; lectura con `desarrollo-ticket-leer` |
| Requisitos que necesitan un entregable trazable | `desarrollo-especificador` |
| Contratos, datos, transacciones o varios servicios | `desarrollo-arquitecto` |
| Segunda mirada a un diseño o diff de riesgo | `desarrollo-revisor` |
| Pruebas y diagnóstico por evidencia | `desarrollo-qa`; UI con `desarrollo-qa-frontend` |
| Infraestructura o pipeline | `desarrollo-devops` |
| Búsqueda acotada de código | `explorer` disponible |
| Implementación delimitada | Agente principal o `worker` disponible |
| Estado de entrega o sprint | `desarrollo-pr-pendientes`, `desarrollo-sprint-informe` |

Usa agentes especializados sólo si están disponibles y la delegación está autorizada por el usuario, las instrucciones del proyecto o las instrucciones aplicables de una skill. Esta skill no exige delegar: si no hay autorización, ejecuta las etapas pertinentes en el agente principal. No simules resultados de otro agente.

Para delegar, da objetivo, fuentes, archivos de responsabilidad, acciones permitidas, salida y dependencias. Los agentes comparten archivos: deben acomodar cambios ajenos y devolver evidencia breve. No delegues de nuevo desde los roles especializados. Etapas dependientes van en orden; paraleliza sólo trabajos independientes autorizados.

Resuelve decisiones reversibles de implementación con criterio y anota supuestos relevantes. Pregunta sólo cuando la respuesta cambie el comportamiento o alcance. No exijas especificación, ADR, entrevista ni matriz completa para un arreglo sencillo. Para decisiones de mayor alcance consulta [criterios de diseño y revisión](references/diseno-revision.md).

En iDempiere, usa primero los especialistas y skills disponibles para la versión real. Conserva las condiciones de `gestionar-tareas` sobre registros persistentes.

Implementa el cambio pedido, verifica según riesgo y presenta resultado, evidencia y límites. Separa inspección, ejecución, merge y despliegue. No publiques ni adjuntes por el solo hecho de terminar: usa las skills de escritura cuando el encargo incluya esa acción. Respeta autorizaciones ya dadas; no las solicites de nuevo sin un cambio material.

No copies reglas globales ni actualices repos automáticamente. Revisa documentación sólo cuando cambien instrucciones, contratos o decisiones que describe. Usa [entrega y continuidad](references/entrega.md) cuando necesites un resumen reutilizable.
