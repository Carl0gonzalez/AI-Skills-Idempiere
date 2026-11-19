# Especialistas iDempiere en Codex

## Decisión y contexto trasladado

El 11 de noviembre de 2026 se trasladó a este repositorio la propuesta de compartir diseño y evaluación entre proyectos iDempiere y acompañarla con una guía para trabajar con menos contexto y retrabajo. La solución inicial es híbrida: skills como fuente de reglas, dos especialistas opcionales y coordinación del agente principal. Un arnés externo queda para una necesidad demostrada de CI, ejecución desatendida o medición automatizada.

| Pieza | Uso |
|---|---|
| `idempiere-model-designer` | Entidades, relaciones, AD y ciclo documental. |
| `idempiere-plugin-designer` | Componentes Java, transacciones y registro OSGi. |
| `idempiere-migration-review` | Coherencia y defectos entre modelo, SQL, AD y Java. |
| `idempiere-designer` | Subagente que carga diseño funcional, técnico o ambos según el encargo. |
| `idempiere-reviewer` | Subagente de revisión independiente de los artefactos delimitados. |

Las tres skills canónicas están en `shared/`. Las carpetas 8, 10, 12, 13 y 14 conservan copias portables sincronizadas: no son cinco conjuntos de reglas distintos. La versión real, Java, motores, APIs y convenciones se verifican en el proyecto. Esto no certifica compatibilidad runtime con todas las versiones, incluida 8.2.

No se crean por ahora cuatro agentes: el diseño técnico normalmente depende del funcional. Calidad continúa en `idempiere-plugin-quality-gate`, cuando el trabajo requiere pruebas; no se ejecuta automáticamente una auditoría completa por cada cambio.

## Instalación personal

Desde la raíz de este repositorio, con Python 3.11 o posterior:

```bash
python3 codex/install.py
python3 codex/install.py --apply
```

El primer comando muestra el plan. El segundo crea:

- Tres enlaces en `~/.agents/skills/` hacia las skills de `shared/`.
- Dos archivos TOML en `~/.codex/agents/`, con rutas absolutas a esas reglas.

La instalación es personal para los proyectos de esta máquina. No modifica `config.toml`, modelos, permisos, instrucciones globales ni otros proyectos. No sincroniza otra máquina. Mantén este repositorio en su ubicación; moverlo rompe las rutas. Antes de moverlo, desinstala y vuelve a instalar desde el destino.

El instalador rechaza conflictos sin sobrescribir archivos; detecta también estas tres skills en la ubicación histórica `~/.codex/skills/`. No inspecciona todas las copias de todos los proyectos. Si un proyecto ya incluye una skill con el mismo nombre, selecciona una sola fuente o invoca la ruta canónica explícitamente. No asumas que Codex fusiona copias.

Las skills enlazadas reflejan cambios locales inmediatamente. Los TOML son copias: ante una actualización que produzca conflicto, compara la copia instalada con la plantilla, conserva personalizaciones y reemplázala sólo tras revisión. El instalador no fuerza actualizaciones.

Para retirar exclusivamente esta instalación:

```bash
python3 codex/install.py --uninstall
python3 codex/install.py --uninstall --apply
```

Si un agente fue personalizado o las plantillas cambiaron desde su instalación, la retirada se detiene para protegerlo. No borra directorios ni archivos ajenos. No publiques rutas personales en commits: las rutas se insertan al instalar.

## Comprobación en un chat nuevo

Abre un proyecto iDempiere y pide:

```text
Comprueba si están disponibles idempiere-designer e idempiere-reviewer.
Usa un subagente idempiere-designer para identificar, sin editar, la versión,
Java y registro OSGi de [ruta del plugin]. Devuelve las fuentes y las dudas.
```

Verifica en la actividad que se haya creado el especialista solicitado. Si no aparece, reinicia Codex y comprueba los archivos instalados. Validar TOML no demuestra que el cliente haya cargado un rol. Si la herramienta de esa sesión no permite seleccionar roles personalizados, dilo: se puede delegar a un agente general con las instrucciones y rutas del especialista, pero debe identificarse como una prueba manual, no como carga nativa del rol.

Los agentes heredan permisos de la sesión. La instrucción de revisión de sólo lectura no constituye un sandbox separado.

## Elegir el modo con menor trabajo innecesario

| Situación | Modo inicial | Motivo |
|---|---|---|
| Ajuste local, regla conocida, pocas rutas | Agente principal y skill pertinente | Evita transferir contexto y repetir exploración. |
| Nuevo modelo o módulo con decisiones sustanciales | Un diseñador | Aísla exploración y devuelve decisiones. |
| Cambio con riesgo transaccional, contable o migración | Implementación y después un revisor | Aporta una comprobación independiente sobre artefactos concretos. |
| Revisión SQL/AD y revisión Java independientes | Dos encargos delimitados si lo pides | Puede reducir tiempo; requiere evitar lecturas repetidas. |
| Compilación o prueba que ya tiene comando fiable | Ejecutar ese comando | Un agente adicional no mejora por sí solo el resultado. |

Son recomendaciones de uso, no una instrucción para crear subagentes automáticamente. Empieza con cero o uno; añade otro sólo si tiene un objetivo distinto. Para revisiones, entrega requisitos y artefactos, sin pedir que confirme las conclusiones del autor.

## Prompts que puedes reutilizar

### Cambio pequeño

```text
Trabaja con un solo agente. En [plugin/ruta], necesito [comportamiento].
Revisa la versión real y usa la skill pertinente. Limita la inspección a
[archivos/área] y sus dependencias necesarias. Implementa y ejecuta las pruebas
adecuadas. Devuelve cambios, evidencia y pendientes en forma breve.
```

### Diseñar un módulo

```text
Delega en idempiere-designer el diseño de [necesidad] en [repositorio/plugin].
Alcance: [funcional/AD, Java o ambos]. Restricciones: [reglas de negocio].
Usa como entrada [requisitos/rutas]. No implementes todavía.
Guarda el diseño en [ruta autorizada] y devuelve decisiones, riesgos y dudas.
El agente principal integra el resultado; no repita toda la exploración.
```

### Evaluación independiente

```text
Usa idempiere-reviewer para revisar [diff base..head o archivos concretos].
Comportamiento esperado: [requisitos]. Prioriza [transacciones/AD/OSGi].
No modifiques archivos ni bases. Devuelve hallazgos con ruta/línea, escenario,
impacto y corrección mínima; separa lo que no se pudo verificar.
```

### Pruebas necesarias

```text
Usa idempiere-plugin-quality-gate para validar [cambio] en [plugin].
Reutiliza [comando y evidencia previa] si siguen vigentes. Ejecuta las pruebas
que cubran el riesgo del cambio. Entorno autorizado: [entorno de pruebas].
No publiques reportes externos. Distingue compilación, pruebas y runtime.
```

### Retomar sin reenviar el chat

```text
Retoma desde [ficha o documento]. Objetivo actual: [uno].
Decisiones vigentes: [dos o tres]. Evidencia: [rutas/commit].
Pendiente inmediato: [paso]. Verifica sólo lo que pueda haber cambiado.
```

Si el repositorio ya usa `.agents/tareas/`, pide explícitamente actualizar su ficha mediante `gestionar-tareas`. Si no lo usa, basta con un documento breve autorizado; no hace falta instalar otro sistema de tareas.

## Reducir tokens sin perder controles útiles

1. Entrega objetivo, ruta, alcance y criterio de aceptación en el primer mensaje. Indica qué entorno está autorizado cuando sean necesarias pruebas con base de datos.
2. Pasa referencias a archivos y un resumen vigente; evita pegar chats completos y logs enormes. Para errores, aporta comando, mensaje y tramo relevante del log.
3. Carga sólo la skill del trabajo actual y sus referencias pertinentes. Tener una skill instalada no exige ejecutar todos sus procedimientos.
4. Delimita los encargos de subagentes: objetivo, entradas, archivos que pueden modificar, entrega y condición de parada. Si la interfaz permite contexto independiente, usa un encargo autosuficiente en lugar de heredar todo el chat. No omitas restricciones necesarias.
5. Mantén un responsable de cada archivo. Diseña primero, implementa después y revisa el resultado estable; evita dos agentes editando el mismo componente.
6. Reutiliza resultados y comandos válidos. Repite una comprobación cuando cambió el artefacto, surgió un fallo o queda una incertidumbre relevante.
7. Pide conclusiones breves y evidencia enlazada. Un límite de palabras reduce la salida, pero no garantiza un límite del razonamiento ni de los tokens totales.
8. Ajusta modelo y esfuerzo según dificultad cuando tengas mediciones. Estas plantillas no fijan ninguno: respetan la selección/configuración existente. Un modelo menor requiere comprobar que mantiene la calidad necesaria.

La documentación oficial advierte que los subagentes consumen más tokens que una ejecución comparable con un solo agente. Úsalos por independencia, calidad o tiempo; no como promesa de ahorro. Las skills cargan detalle bajo demanda. [Subagentes](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills](https://learn.chatgpt.com/docs/build-skills).

## Medir la mejora

Compara tareas similares con criterios de aceptación iguales. Evita repetir sobre producción una tarea sólo para medirla. En una muestra pequeña de tareas reales registra:

| Tarea/commit | Modo y modelo | Tokens totales* | Tiempo | Defectos relevantes | Retrabajo | Aceptación |
|---|---|---:|---:|---:|---:|---|
| completar al usar | principal / diseñador / revisor | N/D | N/D | N/D | N/D | pendiente |

*Suma principal y subagentes; distingue entrada, entrada en caché y salida si la interfaz lo informa. Si no hay datos, registra N/D. No conviertas palabras o tamaño de archivos en consumo real ni inventes porcentajes. Una reducción del tiempo puede acompañarse de un aumento de tokens. Mantén el modo con mejor resultado para esa clase de tarea.

## Mantenimiento y validación

Edita las tres skills únicamente en `shared/`; sincroniza las copias para distribución individual:

```bash
python3 codex/sync_design_skills.py
python3 codex/sync_design_skills.py --check
python3 -m unittest discover -s codex/tests -v
```

El sincronizador copia archivos presentes en la fuente; no elimina recursos obsoletos. Al retirar un recurso, revisa sus referencias y las copias versionadas expresamente. El instalador se prueba con hogares temporales: simulación, repetición, conflictos, enlaces rotos y retirada protegida. Estos controles no sustituyen la prueba de descubrimiento de agentes en un chat nuevo ni una evaluación real de diseño iDempiere.

### Estado del piloto al 11 de noviembre de 2026

- Instalación personal ejecutada y verificada en la máquina de trabajo: tres enlaces de skills y dos agentes TOML; segunda ejecución sin duplicaciones.
- Cuatro pruebas del instalador aprobadas; tres skills aprobadas por `quick_validate.py`; quince copias de `SKILL.md` sincronizadas y referencias de modelo conservadas.
- TOML instalado válido, enlaces documentales locales comprobados y `git diff --check` sin errores.
- Pendientes: descubrimiento nativo de los roles en un chat nuevo, evaluación funcional con un proyecto y medición comparativa de tokens/tiempo. No se han probado builds, bases de datos ni compatibilidad runtime de iDempiere con este piloto.

No se añade un arnés externo ni llamadas API. Reconsiderarlo cuando sea necesario programar lotes reproducibles, integrar CI o recoger métricas automáticamente. Antes debe existir una tarea medible y estable que justifique ese mantenimiento.
