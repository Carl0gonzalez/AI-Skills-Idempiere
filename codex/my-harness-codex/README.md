# my-harness-codex

Adaptación de my-harness-ai para Codex. Contiene **6 agentes y 7 skills**, con los procedimientos de desarrollo separados de roles especializados y de integraciones opcionales. Conserva la licencia MIT del original.

## Uso

Las skills se seleccionan por su descripción o explícitamente. Por ejemplo:

```text
Usa $desarrollo-flujo para implementar este cambio con las etapas necesarias.
Usa $desarrollo-ticket-leer para recuperar los requisitos de este ticket.
Usa $desarrollo-pr-pendientes para revisar qué falta entre estas ramas y PR.
Usa $desarrollo-qa-frontend para reproducir este fallo en la aplicación local.
```

La skill de flujo no impone un equipo completo: un cambio pequeño se resuelve directamente. Para delegación explícita:

```text
Usa desarrollo-especificador para redactar la especificación y después
desarrollo-revisor para revisarla independientemente. No implementes todavía.
```

Los otros roles son `desarrollo-producto`, `desarrollo-arquitecto`, `desarrollo-qa` y `desarrollo-devops`. Heredan modelo y permisos; no se configura otro modelo ni se amplían herramientas. `explorer` y `worker` se reutilizan cuando están disponibles. La sesión o proyecto debe autorizar delegar; los roles no delegan nuevamente.

Las skills `desarrollo-ticket-comentar` y `desarrollo-ticket-adjuntar` se usan sólo para el encargo correspondiente. Preparar un spec o terminar QA no publica nada por sí solo. Las autorizaciones explícitas vigentes se respetan sin preguntas repetidas.

## Instalación selectiva

Requisitos de validación: Python 3.11+ y PyYAML; pruebas de los auxiliares: Git y Bash para el control shell opcional. El uso habitual de las skills de instrucciones no requiere instalar dependencias. No hay paquetes nuevos instalados por este proyecto.

Desde esta carpeta:

```bash
python3 scripts/validate.py
python3 -B -m unittest discover -s tests -v
python3 scripts/install.py
python3 scripts/install.py --apply
```

El instalador primero verifica **todos** los destinos. Añade 7 enlaces en `~/.agents/skills/` y copia 6 TOML a `~/.codex/agents/`. Rechaza colisiones, incluso archivos iguales no registrados como propios: no sobrescribe tus agentes/skills. Por eso la primera instalación no necesita respaldar archivos ajenos. Guarda un manifiesto de propiedad y hashes en `.local-state/` dentro de este paquete. Una segunda ejecución sin cambios es idempotente; cambios posteriores requieren revisión explícita, no una sustitución automática.

El código fuente de las skills permanece aquí: no muevas ni borres esta carpeta mientras estén enlazadas. Los TOML personales son copias verificables, por lo que editar el origen después no actualiza automáticamente el agente instalado.

La documentación oficial describe [skills locales y symlinks](https://learn.chatgpt.com/docs/build-skills) y [agentes TOML](https://learn.chatgpt.com/docs/agent-configuration/subagents). Si la lista de la sesión abierta no se actualiza, inicia un chat nuevo o reinicia Codex. Ejecuta `python3 scripts/verify_discovery.py` para comprobar el descubrimiento de las siete skills en el app-server local.

## Reversión

```bash
python3 scripts/install.py --uninstall
python3 scripts/install.py --uninstall --apply
```

Sólo retira los destinos del manifiesto que todavía coincidan con el enlace o hash instalado. Si un archivo fue modificado por el usuario, aborta sin borrarlo y pide revisar ese cambio. Conserva directorios padres, agentes preexistentes y el paquete fuente. No modifica `config.toml`, Git ni datos externos. Haz la reversión antes de mover el paquete para conservar la trazabilidad de las rutas.

## Auxiliares y límites

- `skills/desarrollo-pr-pendientes/scripts/compare_refs.py`: compara árboles finales y SHA en rutas literales, sin inferir despliegue ni ausencia de una funcionalidad.
- `skills/desarrollo-sprint-informe/scripts/task_commits.py`: busca IDs literales, admite worktrees y muestra contención por commit/ref. Un squash puede tener distinto historial; se necesita evidencia adicional de contenido y proveedor.
- `skills/desarrollo-ticket-leer/scripts/select_spec.py`: filtra ID exacto y versión numérica; copias de la mayor versión quedan ambiguas.
- `optional/check_staged.py`: comprueba Python/JSON/YAML/shell leyendo blobs del índice. Es manual; no instala hook. Código 0: hubo controles y pasaron; 1: fallo; 2: sin controles aplicables o controles incompletos. No reemplaza compilador, linter ni pruebas del proyecto.

Los ejemplos `python3 scripts/...` dentro de las skills se ejecutan resolviendo primero la carpeta real de esa skill; no suponen que el directorio actual sea el de la skill.

## Opcionales evaluados

CodeGraph no estaba instalado al incorporar este paquete. Su skill/MCP se pospone hasta verificar soporte de lenguajes, versión y utilidad en un repositorio piloto; no se instala ni indexa nada aquí. Búsqueda y lectura siguen disponibles.

El runner de integración y los analizadores heurísticos del ZIP no se incorporan como ejecutables activos: el proyecto debe conservar sus pruebas/CI y linters reales. Se aprovecharon sus criterios útiles en las instrucciones de diseño/QA. No se han configurado servicios de tickets ni probado APIs remotas: las skills prefieren conectores disponibles y exigen documentación del proveedor antes de un fallback de API. No se instala `harness-target` porque no hay una integración REST concreta que lo necesite.

Hooks globales, sincronización automática Git/KB, delegación de hooks de subrepos, reglas de emojis y bloqueos globales de documentación quedaron excluidos.
