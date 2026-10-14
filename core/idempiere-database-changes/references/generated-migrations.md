# Reviewing human-generated core migrations

Review and report; never rewrite migration statements or invent identifiers.

- PostgreSQL/Oracle files exist in the current version folders, with equivalent records and appropriate DDL for each engine.
- Names follow yyyyMMddHHmm_IDEMPIERE-<ticket>.sql and the target's chronological registration convention. Header ticket and register_migration_script filename match; Oracle settings follow the generator convention.
- All statements belong to the ticket. Identify failed logged statements, unrelated edits, repeated trial-and-error and unintended deletes.
- Centralized IDs are evidenced or confirmed by the developer. Core dictionary scope/EntityType match target rules (normally client/org 0, EntityType D).
- Physical types, length, defaults, constraints, FK/parent references and translations agree with UI specification and generated models. Do not demand speculative indexes without query/use evidence.
- Generated models changed only as expected. Sample data follows core generation rules.
- Review pending migrations and exact test DB before application. Confirm resulting schema/AD and AD_MigrationScript state afterwards. Static parity does not prove both engines executed successfully.
