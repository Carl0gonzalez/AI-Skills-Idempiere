# Estrategia de pruebas iDempiere

## Fuentes de evidencia

1. Usar ticket/requerimiento como intención funcional.
2. Usar Java y SQL ejecutable como comportamiento implementado.
3. Usar Application Dictionary y 2Pack como configuración habilitante.
4. Usar la BD de pruebas como evidencia de estados reales, no como especificación por sí sola.
5. Registrar diferencias entre intención, implementación, metadatos y datos.

## Inventario

Buscar `DB`, `Query`, `PO`, `Env`, `Trx`, `prepare`, `doIt`, `call`, `modelChange`, `docValidate`, `setValue`, `saveEx`, SQL escrito, tablas AD y servicios OSGi. Registrar por regla: entrada, fuente primaria, fallback, resultado, error, efecto persistente y propietario de la transacción.

## Datos seguros

- Confirmar host, puerto y nombre de BD; rechazar endpoints de producción.
- Empezar por conteos y consultas limitadas compatibles con el motor objetivo; no copiar LIMIT de PostgreSQL a Oracle.
- Evitar datos personales en informes.
- Cubrir registro nuevo, histórico, nulo, cero, alternativo y conflicto entre fuentes.
- Capturar cliente, organización y configuración vigente cuando afecten el caso.
- Ejecutar mutaciones en transacción con `ROLLBACK` o fixture cuya limpieza se compruebe.

## Capas

### Unidad

Validar fórmulas, redondeo, precedencia, límites y errores sin servidor/BD. Extraer función pura si es el refactor mínimo seguro. Para importes usar `BigDecimal`, comparación, escala y redondeo explícitos.

### Integración

Validar consultas, filtros cliente/organización, transacciones, modelos y metadatos. Comparar antes, durante y después; comprobar rollback.

### Migración/2Pack

Validar precondiciones, tipos físicos versus AD, IDs/secuencias y dependencias. Revisar repetición/idempotencia y rollback sólo según el mecanismo real: SyncDB registra migraciones y no implica que todo DDL pueda repetirse o revertirse transaccionalmente. En core revisar lo generado por el desarrollador, sin escribir/corregir scripts.

### Funcional/UI

Validar rol, ventana/proceso, entrada, mensaje, persistencia y recarga. Una simulación SQL no sustituye esta capa.

## Matriz mínima

| Regla | Caso | Nivel | Esperado | Evidencia |
|---|---|---|---|---|
| Fuente específica | específico lleno y default distinto | unidad + integración | usa específico | assertion + SELECT |
| Fallback | específico nulo | unidad + integración | usa default | assertion + SELECT |
| Límite | cero, igualdad, extremos | unidad | regla exacta | JUnit |
| Regresión | equivalente al ticket | integración + funcional | no reaparece error | log/pasos |
| Aislamiento | otro cliente/organización | integración | no mezcla datos | assertion/SELECT |
| Idempotencia | repetición mediante el mecanismo soportado | migración/2Pack | estado coherente | registro/consulta |

Clasificar cada caso como `EJECUTADA Y APROBADA`, `EJECUTADA Y FALLIDA`, `NO EJECUTADA` o `BLOQUEADA`. No convertir compilación exitosa en prueba funcional ni cobertura alta en corrección de reglas.
