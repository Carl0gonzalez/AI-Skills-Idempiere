# Integraciones de calidad

Mantener una cadena única: `JUnit/PDE -> JaCoCo XML -> SonarQube + Coveralls -> Prometheus -> Grafana`.

## JaCoCo

- Detectar Java, Maven/Tycho y configuración existente.
- Generar XML además de HTML y registrar su ruta.
- En plugin + fragmento, cubrir clases del plugin sin contar tests como producción.
- No fijar versiones arbitrarias; usar una compatible con builder y Java.

## SonarQube

- Preferir SonarScanner for Maven si Tycho expone correctamente fuentes y bytecode; usar CLI si el repositorio así lo establece.
- Generar JaCoCo primero y configurar `sonar.coverage.jacoco.xmlReportPaths`.
- Proporcionar `sonar.java.binaries` cuando el scanner no lo derive.
- Mantener `SONAR_TOKEN` sólo en entorno/secret store.
- Distinguir análisis recibido de Quality Gate terminado.
- Tratar el primer análisis como línea base: un Quality Gate basado en código nuevo puede devolver cero condiciones evaluadas hasta definir/existir código nuevo.

Documentación oficial: https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/test-coverage/overview

## Coveralls

- Reutilizar `jacoco.xml`; evitar repetir pruebas sólo para publicar.
- Detectar la integración soportada por el CI antes de escoger uploader/plugin.
- No copiar versiones desde ejemplos antiguos; comprobar compatibilidad con Java.
- Mantener `COVERALLS_REPO_TOKEN` en secretos de CI.
- Separar reporte producido, carga aceptada y estado remoto.

Documentación: https://docs.coveralls.io/

## Prometheus y Grafana

1. Convertir la ejecución con `quality_evidence.py --format prometheus`.
2. Enviar al Pushgateway configurado o exponer al scraper existente.
3. Usar labels de baja cardinalidad: `environment`, `plugin`, tipo y resultado. No mezclar dos entornos bajo la misma identidad.
4. Consultar desde el datasource Prometheus provisionado en Grafana.

Usar anotaciones sólo para correlacionar ejecuciones/despliegues. Detectar versión de Grafana antes de llamar su API: los APIs nuevos `/apis` aparecen desde Grafana 12 y los legacy `/api` comienzan a deprecarse en Grafana 13. Usar service account con privilegio mínimo.

Documentación oficial:

- https://grafana.com/docs/grafana/latest/datasources/prometheus/
- https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/
- https://grafana.com/docs/grafana/latest/developer-resources/api-reference/http-api/authentication/

## Preflight remoto

Antes de publicar comprobar servicio/versión, proyecto/datasource, autorización, secreto presente pero no impreso, reporte válido, rama/commit y política de reintento sin duplicados.
