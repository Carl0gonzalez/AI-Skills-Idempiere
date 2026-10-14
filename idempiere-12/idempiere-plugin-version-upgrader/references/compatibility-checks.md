# Compatibility checks by target release

Read every section crossed by the source-to-target upgrade. Confirm each item against the current official Migration Notes and exact target branch because rolling maintenance can add changes within a release.

## Universal Java and OSGi checks

- Compile with the target JDK, not merely a newer JDK using an older source flag.
- Compare imports and method signatures with the target source or target-platform JARs.
- Check removed JDK modules, reflective access, internal `sun.*` APIs, XML/signature algorithms, date/time behavior, and library major-version changes.
- Resolve `Require-Bundle`, `Import-Package`, `Export-Package`, `Fragment-Host`, `Bundle-ClassPath`, and DS services against the target platform.
- Check embedded JAR bytecode levels and duplicate packages. A bundle can compile while failing OSGi resolution at runtime.
- Treat deprecation warnings as review items. Replace APIs when the target notes prescribe a replacement; do not rewrite harmless deprecations without a compatibility reason.

## PostgreSQL and JDBC checks

Search Java, SQL, XML/2Pack, Jasper expressions, and migration files for:

- database-specific casts/operators, quoted identifiers, reserved words, implicit type conversions, and Oracle-only or PostgreSQL-only functions;
- SQL built by string concatenation instead of bind parameters or `SQLFragment` where the target API provides it;
- untyped nullable parameters, especially constructs such as `(? IS NULL OR column = ?)`;
- UUID values treated as `varchar`, UUID/varchar unions and comparisons, custom UUID functions, and custom views depending on UUID columns;
- `DatabaseMetaData.get*` calls with arbitrary catalog values;
- assumptions about sequences, timestamps, booleans, numeric precision, `bytea`, large objects, transaction boundaries, or JDBC generated keys;
- migration scripts without registration/idempotence, dependency-ordered views/functions, or target-compatible DDL.

Prefer portable SQL when the plugin claims both PostgreSQL and Oracle support. PostgreSQL syntax such as `::varchar` may solve one target but break Oracle; use standard `CAST` where it preserves behavior.

Static findings identify risk. Execute affected statements or meaningful integration tests against the target PostgreSQL version before calling them compatible.

## Crossing into 8.2

- Theme resource paths became versioned.
- `ITheme.THEME_PATH_PREFIX` was removed; migrate affected themes to the supported `ThemeManager` API.

## Crossing into 9

- PostgreSQL native dialect became the default. Remove reliance on the compatibility dialect and `NATIVE_PostgreSQL_KEYWORK`; prefer SQL valid for the claimed databases.
- Direct HTTP usage was deprecated; inspect integrations that hardcode HTTP server endpoints.

## Crossing into 10

- System user ID zero was replaced by ID 10. Inspect hardcoded user IDs and custom-table references.
- `TimeUtil.getBusinessDaysBetween` changed end-date behavior; use the replacement overload when preserving prior behavior matters.
- Hazelcast configuration format changed in later release-10 maintenance. Plugin-owned Hazelcast configuration must follow the target template.

## Crossing into 11

- Java 17 is required for running and compiling. Update execution environments, toolchains, bytecode, libraries, and code incompatible with Java 17.
- Review constructor/API changes listed in the version 11 migration notes, including process-instance handling when the plugin constructs `MPInstance` directly.

## Crossing into 12

- PostgreSQL JDBC 42.7.5+ uses the catalog argument in `DatabaseMetaData.get*` as a real filter. Pass the database name or `null`, not an arbitrary catalog.
- Later release-12 adds `SQLFragment` and deprecates APIs that interpolate direct where clauses. Migrate affected code when upgrading to a maintenance level that contains this API.
- Inspect promotions dependencies because promotions moved out of core into a separate plugin.

## Crossing into 13

- PostgreSQL UUID columns moved from `varchar` to native `uuid`, and generated UUIDs moved to UUIDv7. Review bindings, casts, unions, views, functions, reports, and generated models.
- JDBC uses `stringtype=unspecified`; explicitly type ambiguous nullable parameters using portable SQL. Do not rely on the backend inferring a type for standalone `? IS NULL` expressions.
- PostgreSQL 13+ supplies `gen_random_uuid` natively; versions 11 and 12 may need `pgcrypto` for backported scripts. Test the actual supported target version.
- `MAttachment.setTitle` accepts restricted list values. Inspect plugins that used the title as arbitrary storage metadata.
- Old APIs deprecated for more than two major releases were removed. Compilation failures require migration to current APIs.
- Foreign-key object getters on generated `X_` classes are deprecated for performance; prefer cache-aware model access where appropriate.

## Crossing into 14 development

- SOAP web services moved from core to a standalone plugin. Update OSGi dependencies for code importing `org.idempiere.webservice.*`.
- Accounting implementation classes moved to `org.idempiere.acct`. Update bundle/package dependencies and imports for custom posting code.
- Recheck the full version 14 migration section because `master` changes continuously until release.

## Evidence levels

Use these result labels precisely:

- **Java/OSGi verified locally:** complete affected build passed with target JDK and target platform.
- **PostgreSQL verified locally:** affected SQL/JDBC paths passed against a recorded supported PostgreSQL server and JDBC driver.
- **Static PostgreSQL review only:** SQL/JDBC code was inspected but not executed.
- **Runtime not verified:** plugin was not installed and activated in a target iDempiere server.
