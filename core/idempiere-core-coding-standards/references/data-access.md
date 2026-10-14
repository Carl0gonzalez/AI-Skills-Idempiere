# Data-access review questions

1. Can an existing model method preserve business behavior and reuse appropriate caching?
2. Does Query bind values and carry the owning transaction, client and required role constraints?
3. If DB helpers/raw UPDATE are used, is bypassing lifecycle hooks/events/change logging intentional?
4. Does an available batch PO API preserve the specific hooks the operation needs? Inspect the target API/tests before using it.
5. Are JDBC resources closed on success and failure using the target convention?
6. Does every statement express equivalent behavior on PostgreSQL and Oracle, including nulls, ordering and first-row selection?

Do not mutate cached read-only POs or commit an externally owned transaction. Framework/API selection depends on target source, not the age of this reference.
