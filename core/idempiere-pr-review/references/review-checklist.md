# Core review checklist

- Scope: ticket, one purpose, exact files, separate refactoring, documentation needs.
- Data: both generated migration sets, ID origin, physical/AD consistency, no handwritten repair.
- SQL: parameter binding, PostgreSQL/Oracle behavior, PO lifecycle versus raw updates, closed resources.
- Transactions: owning trxName, no hidden commits/rollbacks/null mixing.
- Security: role/client/org access, validated input, safe UI output, no secrets.
- Compatibility: overloads/deprecation, declared intentional breaks, default behavior, external plugin callers, target serialVersionUID convention.
- Quality: English, license, translations, surrounding style, no new warnings/unrelated changes.
- Evidence: focused regression, real executed counts, base failures, manual/collateral scenarios, unavailable engines/runtime reported.

Rank correctness/security/compatibility before style. A declared break still requires a maintainer decision.
