# Delegate selection

| Need | Candidate to verify in the target release | Key check |
|---|---|---|
| PO lifecycle | ModelEventDelegate + PO annotations | Owning trxName, before/after timing, recursion |
| Document lifecycle | ModelEventDelegate + document annotations | Action/event sequence including void/reversal/reactivation |
| Login/preferences | AfterLoginEventDelegate | Session context and supported callbacks |
| Posting facts validation | FactsValidateDelegate | Accounting schema, veto/error contract |

Use only the annotations required by the rule. Confirm the constructor and method signatures from actual core and tests. Search source and resolved dependencies; do not block merely because the model source is not open in an editor.
