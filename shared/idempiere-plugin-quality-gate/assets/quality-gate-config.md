# Variables de configuración del quality gate

Los nombres siguientes se usan según el entorno y las integraciones habilitadas.

| Componente | Variables |
|---|---|
| Base de datos de pruebas | `IDEMPIERE_TEST_DB_HOST`, `IDEMPIERE_TEST_DB_PORT`, `IDEMPIERE_TEST_DB_NAME`, `IDEMPIERE_TEST_DB_USER` |
| SonarQube | `SONAR_HOST_URL`, `SONAR_PROJECT_KEY` |
| Prometheus | `PROMETHEUS_PUSHGATEWAY_URL` |
| Grafana | `GRAFANA_URL`, `GRAFANA_DASHBOARD_UID` |

Carga `PGPASSWORD` desde un gestor de secretos o en un entorno efímero. Gestiona `SONAR_TOKEN` y `COVERALLS_REPO_TOKEN` como secretos de CI. Usa una cuenta de servicio con privilegios mínimos para `GRAFANA_SERVICE_ACCOUNT_TOKEN`.
