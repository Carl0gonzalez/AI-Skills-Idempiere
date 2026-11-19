# Criterios condicionales de diseño y revisión

Elige los que apliquen: nulos/vacíos, límites, volumen, roles, aislamiento, concurrencia, reintentos, fallos externos, estados inválidos, datos existentes, reversa y observabilidad. No fuerces apartados sin relación con el cambio.

Una especificación distingue requisito, evidencia y supuesto. Da criterios de aceptación observables; verifica persistencia cuando corresponda. Conserva trazabilidad a la fuente y señala conflictos sin asumir que cualquier comentario posterior tiene autoridad para cambiar el alcance.

Una decisión técnica no obvia explica contexto, alternativa viable, decisión y coste. Respeta límites de transacción y de despliegue. Una llamada externa dentro de una transacción requiere evaluar duración, bloqueos y recuperación. Si se necesita asincronía, diseña duplicados, orden pertinente, reintentos, agotamiento y seguimiento; aprovecha infraestructura existente.

Evalúa índices según motor, predicados, joins, selectividad, volumen, coste de escritura e índices existentes. Una FK no exige automáticamente crear un índice adicional. Define identidad autorizada del servidor: un tenant enviado por el cliente sólo puede usarse tras comprobar su acceso.

Migraciones y varios despliegues requieren describir compatibilidad intermedia, datos existentes y recuperación. Expand/contract y feature flags son opciones cuando resuelven un riesgo real, no requisitos universales. Una restauración puede ser parte de la recuperación si se explican pérdida de datos y tiempo.

Una revisión puede devolver cero hallazgos. Cada defecto debe incluir ubicación, escenario alcanzable, impacto y ajuste concreto. Distingue hipótesis pendientes de defectos comprobados. No exijas descubrir fallos ni impongas cuotas de observaciones.

En worktrees, el stash es compartido por repositorio: no hagas pop de trabajo cuya procedencia no confirmaste. Evita acciones Git automáticas. Prefiere búsquedas y lecturas dirigidas; conserva suficiente contexto para comprobar las afirmaciones.
