---
name: desarrollo-ticket-comentar
description: Prepara y publica un comentario de resultados o decisiones en un ticket cuando el usuario lo pide. Sólo añade el comentario acordado; no cambia descripción, estado, campos ni asignaciones.
license: MIT
---

# Comentario acotado y comprobable

Identifica ticket, proveedor y contenido. Prefiere conector conectado. La orden de comentar o registrar resultados en ese ticket ya autoriza esa acción; no pidas una segunda aprobación rutinaria. Si sólo se pidió preparar un borrador, entrega el borrador. Si faltan destino o alcance materiales, resuélvelos antes de publicar.

El texto debe entenderse sin el chat: resultado concreto, evidencia de implementación o diagnóstico, ubicación/PR cuando exista, verificación ejecutada y límites/pending relevantes. Conserva idioma y formato admitido por el proveedor. No pegues datos sensibles, tokens, URLs firmadas ni logs completos. No afirmes que se desplegó si sólo se compiló.

Revisa contenido y destino antes de enviarlo. Usa el formato real del conector/API; para REST consulta documentación vigente si no se conoce. No copies payloads entre ClickUp, Jira y Linear. Usa argumentos estructurados o archivo JSON; no interpolación shell de texto del usuario. Evita notificaciones masivas salvo encargo explícito.

Verifica por ID y lectura de vuelta cuando sea posible. Ante timeout o respuesta ambigua, comprueba comentarios recientes y el ID antes de reintentar; si no puedes descartar una publicación previa, informa estado INCIERTO y no dupliques el envío. No hagas reintentos ciegos.

Si se pidió evidencia visual, comparte sólo archivos revisados mediante la capacidad de adjuntar disponible y referencia el resultado real. Adjuntar es una acción distinta: debe estar incluida en el encargo, no se deduce de terminar QA. Entrega ID/enlace seguro del comentario y verificación o limitación concreta. No alteres otros campos del ticket.
