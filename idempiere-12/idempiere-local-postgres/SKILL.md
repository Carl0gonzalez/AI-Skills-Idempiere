---
name: idempiere-local-postgres
description: Safely inspects and diagnoses a local iDempiere PostgreSQL database using repository configuration or user-provided credentials.
---

# Purpose

Connect to a local iDempiere PostgreSQL development database for safe inspection and diagnostics. Discover repository-specific connection details first and use the platform's `psql` command; do not assume a Windows installation, a database port, or a particular iDempiere version.

# Activation Guidance

Use this skill when the user asks to query, inspect, diagnose, or verify a local iDempiere PostgreSQL database.

# Security and Safety

- Never print passwords, connection strings containing passwords, or private `.env` contents.
- Prefer existing local configuration (`.env` files ignored by Git, project scripts, or explicitly supplied environment variables). Ask for missing credentials without persisting them unless the user explicitly requests that.
- Open every connection in read-only mode by default, for example with `PGOPTIONS='-c default_transaction_read_only=on'`, and use `psql -v ON_ERROR_STOP=1`.
- Run `SELECT`, `SHOW`, and `EXPLAIN` queries directly in the read-only session.
- Treat every statement other than read-only inspection as a write, including `INSERT`, `UPDATE`, `DELETE`, `MERGE`, DDL, function calls with side effects, and any command that changes database state.
- Restrict connections to local development endpoints unless the user explicitly authorizes another endpoint.

## Write Authorization: Mandatory Double Verification

Do not execute a write merely because the user asked to change data. Before any database write, complete both confirmations below.

1. **Impact review:** show the exact target database, affected table or records, the proposed SQL or precise operation, and its expected business and data impact. Ask for the user's first explicit approval.
2. **Final confirmation:** after the first approval, restate the finalized operation, including the exact target and expected impact, and ask for a second explicit confirmation immediately before execution.

Only execute the write after both approvals are explicit and separate. If the SQL, target, filter, or impact changes after the first approval, restart the two-step confirmation. Keep writes scoped to the approved rows and report the resulting row count or outcome. Do not use a read-only session for a confirmed write; open a separate, narrowly scoped write session only after the second confirmation.

# Workflow

1. Discover the configured host, port, database, and user without exposing secrets.
2. Verify that `psql` is available and test the connection with `SELECT 1`.
3. Confirm this is an iDempiere schema by checking for core dictionary tables such as `ad_table`.
4. Classify each requested SQL statement as read-only or modifying. Execute read-only statements in a session forced to `default_transaction_read_only=on`.
5. For a modifying statement, complete the mandatory double-verification workflow: impact review and final confirmation.
6. Execute an approved write only in a separate write-enabled session, with password input supplied through the process environment, then clear temporary credentials.

# Output Contract

Report the non-secret connection target, query classification, read-only enforcement, and formatted results or actionable errors. For a write request, report the proposed adjustment and impact before each required confirmation.
