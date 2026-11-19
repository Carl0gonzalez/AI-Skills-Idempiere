---
name: desarrollo-pr-pendientes
description: Consolida PR/MR pendientes y compara contenido entre ramas con evidencia del proveedor y Git. Usar al preguntar qué falta por abrir, mergear o promover; sólo consulta, no crea PR ni hace merge o despliegue.
license: MIT
---

# Estado verificable de una entrega

Parte de repositorios, ramas, PR/MR y chats que el usuario indique. Usa herramientas de chats disponibles si pidió consolidar conversaciones; no rastrees todos los historiales personales ni transcripts de otro producto. Una URL citada no prueba que se haya creado el PR en esa conversación.

Consulta el conector Git disponible primero; como alternativa, CLI autenticado del proveedor. Verifica estado abierto/cerrado/mergeado, destino, SHA, conflictos y checks. No extraigas tokens a salidas. Si no hay acceso, informa estado remoto NO VERIFICADO. No hagas push, merge, checkout ni fetch automático: los refs locales pueden estar desactualizados; actualizar referencias es una acción aparte dentro del trabajo autorizado.

Para comprobar contenido usa el auxiliar con ruta resuelta desde esta skill:

```bash
python3 scripts/compare_refs.py --repo /ruta/repo --target origin/main --source origin/feature -- src/modulo
```

Compara los árboles finales de las rutas indicadas y devuelve los SHA observados. Mismo contenido no prueba quién lo introdujo; contenido distinto no prueba que falte el cambio completo: puede haber modificaciones posteriores. Usa el diff del PR, equivalencia de parches, código actual y pruebas específicas para decidir. Un diff de tres puntos usa el ancestro común y no demuestra ausencia después de squash/cherry-pick. Ni `git log` ni `git cherry` por sí solos cubren todas las formas de integración.

Entrega por abrir / abiertos / mergeados con promoción pendiente, sólo si hay evidencia para cada grupo. Un PR mergeado no demuestra despliegue. Para afirmar producción pide evidencia del artefacto/versión desplegado o de su pipeline. Ordena promociones según dependencias reales y explicita lo que no se pueda determinar.
