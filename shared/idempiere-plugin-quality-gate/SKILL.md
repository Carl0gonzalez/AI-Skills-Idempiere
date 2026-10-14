---
name: idempiere-plugin-quality-gate
description: Genera, ejecuta y documenta pruebas y controles de calidad para cualquier plugin OSGi de iDempiere, derivando el comportamiento esperado desde Java, metadatos de Application Dictionary, SQL/2Pack y una base de datos de pruebas. Usar al validar cambios de un plugin, crear pruebas unitarias o de integración, comprobar escenarios funcionales con datos reales, medir cobertura JaCoCo, analizar con SonarQube, publicar cobertura en Coveralls o exponer resultados mediante Prometheus/Grafana.
---

# Quality gate para plugins iDempiere

Construir evidencia reproducible de compilación, calidad estática, cobertura y comportamiento funcional. Adaptarse a la estructura y herramientas existentes; no imponer un Maven convencional sobre un build PDE/Tycho.

## Principios obligatorios

- Tratar código, Application Dictionary y BD de pruebas como fuentes complementarias. Resolver y documentar contradicciones.
- Ejecutar primero pruebas puras, luego integración con BD y finalmente UI. No reemplazar una capa por otra.
- Usar JaCoCo para producir cobertura; usar SonarQube y Coveralls para importarla/publicarla.
- Usar Grafana para visualizar métricas o anotar ejecuciones, no como ejecutor de pruebas.
- No revelar tokens, contraseñas ni URLs con credenciales. Informar sólo si una variable requerida está presente.
- Confirmar que la BD es de pruebas antes de escribir. Preferir transacciones revertibles, fixtures propios y rollback comprobado.
- No modificar build, CI, infraestructura o dashboards si el usuario pidió sólo diagnóstico.
- No declarar éxito de una prueba no ejecutada. Marcar `NO EJECUTADA` o `BLOQUEADA` y explicar la causa.

## Contexto y alcance

- En core, leer AGENTS.md y las skills locales de pruebas y cambios de BD. No escribir migraciones core ni inventar IDs; revisar lo generado por el desarrollador.
- Separar generación de tests (`idempiere-plugin-test-developer`) de ejecución/evidencia en esta skill. No imponer JUnit/Mockito ausentes en la versión objetivo.
- JaCoCo, SonarQube, Coveralls y Grafana son opcionales según el encargo y la configuración. No exigirlos para aprobar un cambio ajeno a esas integraciones.
- Verificar que el comando realmente ejecuta tests: en el core de referencia `./mvnw verify` los omite por defecto; usar `-DskipTests=false` y comprobar informes nuevos y conteos.
- No modificar fixtures compartidos de GardenWorld; usar registros propios y rollback, o mocks compatibles con las dependencias existentes.

## Flujo

### 1. Descubrir el entorno

1. Resolver la ruta absoluta del plugin y la raíz del repositorio.
2. Leer `META-INF/MANIFEST.MF`, `pom.xml`, `build.properties`, `Jenkinsfile`, componentes DS y documentación relevante.
3. Buscar el fragmento de pruebas, builder/target platform y configuración JaCoCo, SonarQube, Coveralls, Prometheus o Grafana.
4. Ejecutar el preflight sin efectos laterales:

```bash
python3 <skill-dir>/scripts/quality_evidence.py <plugin-dir> \
  --repo-root <repo-root> --environment <environment-id>
```

5. Informar capacidades y ausencias. No instalar servicios o dependencias automáticamente.

### 2. Derivar el contrato funcional

Inventariar procesos, callouts, validadores, factories, listeners, modelos, SQL y 2Pack. Registrar por flujo: disparador, entradas, precondiciones, tablas/columnas, fórmula, prioridad de fuentes, estado final, errores, permisos, transacción y efectos secundarios.

Leer `references/test-strategy.md`. Usar `SELECT` limitados para localizar casos representativos en la BD de pruebas y separar hechos de inferencias. Componer con `idempiere-local-postgres` cuando esté disponible; si no, usar inspección de solo lectura con el destino verificado.

### 3. Diseñar y generar pruebas

Construir una matriz `regla -> datos -> prueba -> evidencia`. Incluir camino feliz, límites, cero, nulos, precisión monetaria, errores, precedencia entre fuente específica y default, históricos, aislamiento cliente/organización, idempotencia de SQL/2Pack y la regresión que motivó el cambio.

Usar el framework declarado por el fragmento; preferir pruebas de lógica pura. Si el código mezcla reglas con `DB`, `Env`, `Query`, `PO` o UI, ejecutar el refactor mínimo autorizado que separe la regla sin alterar el contrato. Crear pruebas en el fragmento existente y componer con `idempiere-plugin-test-developer`.

Usar integración con BD sólo cuando el comportamiento no pueda verificarse por aislamiento. Crear datos propios o seleccionar identificadores estables; nunca depender silenciosamente de un registro accidental.

### 4. Ejecutar por capas

1. Ejecutar pruebas unitarias del fragmento.
2. Compilar con el builder documentado y dependencias OSGi en orden; componer con `idempiere-plugin-compiler`.
3. Ejecutar integración contra la BD confirmada como prueba y comprobar rollback/estado posterior.
4. Ejecutar UI sólo con instancia local accesible y credenciales autorizadas.
5. Conservar comando, código de salida, duración, conteos y artefactos.

No usar `mvn test` genérico cuando el repositorio requiere Tycho, parent POM o script builder.

### 5. Cobertura y calidad

Generar `jacoco.xml` antes del análisis. Si falta instrumentación, presentar y aplicar el cambio mínimo sólo dentro del alcance autorizado.

Ejecutar SonarQube sólo si existen scanner/goal, bytecode, URL y token. Usar una clave distinta por ambiente y plugin: `<environment-id>:<bundle-symbolic-name>`. Pasar `sonar.coverage.jacoco.xmlReportPaths` con la ruta real y registrar el Quality Gate final, no sólo la aceptación del análisis.

Publicar en Coveralls sólo desde rama/CI autorizada y con token. Reutilizar el mismo JaCoCo. Leer `references/integrations.md` antes de configurar o invocar servicios remotos.

### 6. Métricas y Grafana

Extraer métricas locales después de las pruebas:

```bash
python3 <skill-dir>/scripts/quality_evidence.py <plugin-dir> \
  --repo-root <repo-root> --environment <environment-id> --format prometheus
```

Publicarlas en el backend ya conectado a Grafana usando siempre las etiquetas `environment` y `plugin`, o crear una anotación si la integración existe. No enviar datos externamente sin autorización ni crear dashboards antes de detectar convenciones corporativas.

### 7. Evaluar y documentar

Copiar y completar `assets/QUALITY_REPORT_TEMPLATE.md`. Clasificar:

- `APROBADO`: todas las puertas obligatorias configuradas pasaron.
- `APROBADO CON OBSERVACIONES`: pruebas exigidas pasaron y sólo faltan integraciones opcionales identificadas.
- `RECHAZADO`: falló compilación, prueba obligatoria, Quality Gate o regla funcional.
- `INCONCLUSO`: faltó acceso, configuración o evidencia para decidir.

No inventar umbrales. Usar los definidos; si no existen, registrar línea base y proponer umbrales separados para código nuevo y total.

## Entrega

Entregar alcance y entorno; contrato y trazabilidad; archivos de prueba; comandos y resultados; capas de prueba separadas; cobertura, Sonar y Coveralls; publicación Grafana o razón de omisión; cambios/rollback de BD; riesgos, pendientes y veredicto.

## Recursos

- `scripts/quality_evidence.py`: inventariar y resumir Surefire/JaCoCo sin red ni BD.
- `references/test-strategy.md`: derivar pruebas funcionales desde código, AD y BD.
- `references/integrations.md`: integrar herramientas con seguridad.
- `assets/QUALITY_REPORT_TEMPLATE.md`: plantilla del informe.
- `assets/quality-gate.env.example`: nombres de configuración sin secretos.
