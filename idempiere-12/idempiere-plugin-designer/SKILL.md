---
name: idempiere-plugin-designer
description: Translate iDempiere requirements or data designs into minimal Java/OSGi implementation plans using the target release and bundle conventions. Use for technical plugin design, not initial data modeling or automatic implementation.
---

# Technical design

Read the affected bundle's instructions, `MANIFEST.MF`, `build.properties`, build/target configuration and relevant registration examples. Verify release, Java and APIs from the checkout, not another project's environment. Reuse an existing functional design; request only missing decisions that materially affect implementation.

- Prefer AD configuration, existing APIs and existing components before new classes or layers. Consult `idempiere-architecture-patterns` when available for substantial architectural choices, loading only the relevant reference.
- Keep generated `I_*`/`X_*` separate from `M*` domain behavior. Verify PO constructors and actual model factory or mapped registration. Do not edit generated models.
- Choose model/event enforcement for invariants shared by UI, REST, imports and processes. Callouts provide interactive assistance. Use `SvrProcess` for explicit operations; verify parameter parsing/injection in the actual factory.
- Reuse the bundle's proven XML/DS/annotation mechanism. Verify interfaces, topic constants and scanning packages in the target version. Do not invent `IEventFactory`, mandate annotations or add all factories by default.
- Preserve owning transactions, tenant/org/role access and normal document processing. Identify error/rollback behavior; assess locks, retries and idempotency when relevant. Preserve public/protected APIs and inspect affected callers.
- Core changes follow the actual contribution/database policy; private plugins retain their Entity Type, supported engines and export conventions. Design work alone does not authorize implementation, PackIn, SyncDB or deployment.

Return only required components: class/responsibility, entry point, actual registration, transaction owner, metadata dependencies and focused verification plan. Include paths supporting API choices and explicitly mark assumptions. Add pseudocode where control flow is non-obvious; avoid empty package trees and full code dumps. If the requested change fits an existing class, say so without designing a new framework.
