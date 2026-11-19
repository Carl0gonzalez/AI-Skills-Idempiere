---
name: desarrollo-ticket-adjuntar
description: Adjunta un archivo identificado a un ticket por encargo y verifica su registro sin duplicarlo. Usar al pedir subir un spec, informe o captura al gestor; no publica comentarios ni modifica otros campos.
license: MIT
---

# Adjuntar el archivo correcto

Resuelve ticket y archivo exactos desde el encargo, incluido qué versión se solicitó. Comprueba existencia, nombre, tamaño, contenido y datos sensibles pertinentes. La petición explícita de adjuntar ese archivo ya autoriza la subida; no repitas una confirmación. Si sólo se pidió crear el archivo, entrégalo sin subir.

Prefiere conector conectado con capacidad de adjuntar. Si no la tiene, explica la limitación y usa cliente/API documentada disponible dentro del encargo. Confirma el método y límite del proveedor real; no afirmes universalmente que los adjuntos no se pueden borrar ni que se reemplazan por nombre. No configures servicios ni inventes endpoints para completar la subida.

Mantén nombres de versiones si el archivo es una especificación. Usa parámetros estructurados o subida de archivo; no interpolación de comandos desde el ticket. Registra el ID devuelto y verifica título, tamaño si está disponible y relación con el ticket mediante lectura posterior. Un 200 no prueba que el contenido sea legible. No descargues archivos grandes sin necesidad ni muestres URLs firmadas.

Ante timeout, consulta los adjuntos y compara identidad/nombre/tamaño/fecha y checksum si existe antes de reintentar. Una coincidencia sólo de nombre puede ser ambigua: informa INCIERTO si no puedes identificar la subida, sin crear duplicados. No borres archivos externos como compensación automática.

Entrega archivo y versión adjuntos, ticket y evidencia del registro; separa subida confirmada de legibilidad comprobada. Si falta acceso, entrega la ruta local y qué capacidad falta. No escribas comentarios ni cambies estado, descripción o asignaciones sin un encargo que también los incluya.
