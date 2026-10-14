# Component registration alternatives

Inspect existing target-version code/tests before choosing. The list is a selection guide, not a promise that all APIs exist in every release.

| Component | Candidate | Verify |
|---|---|---|
| Process | Existing IProcessFactory | Class resolution and real AD Classname/parameters |
| Annotated process | AnnotationBasedProcessFactory + @Process/@Parameter | getPackages signature, supported parameter types, DS generation |
| Mapped process | IMappedProcessFactory.scan | Interface package/signature and service availability |
| Column callout | IColumnCalloutFactory / legacy CalloutEngine | Return/error semantics, AD/factory convention and recursion |
| Annotated callout | @Callout + AnnotationBasedColumnCalloutFactory | Table/column constants and scanned package |
| Event | AbstractEventHandler with DS XML/annotations | IEventTopics, table filters, handleEvent signature and veto behavior |
| Delegate | AnnotationBasedEventManager + delegates | Required annotations, constructors and scanned package |
| PO model | IModelFactory or IMappedModelFactory | Constructors and table mapping; generated model remains unchanged |

## Process patterns

```java
@Process
public class RecalculateProcess extends SvrProcess {
    @Parameter
    private int p_M_Product_ID;

    @Override
    protected void prepare() {
        // Validate the actual AD parameter before doIt uses it.
    }

    @Override
    protected String doIt() throws Exception {
        // Use get_TrxName(); implement the actual requested operation.
        return "";
    }
}
```

This is a structural snippet, not a finished process. Resolve imports, GPL header, translated results and actual logic from the target. If annotations are unavailable, parse ProcessInfoParameter in prepare using the existing factory/registration.

For annotation factories, add the package to the existing getPackages override; do not create another factory for each class. For mapped services, use the existing proven DS service injection and activation method, then scan the requested process/model package (which may differ from the activator package). Do not assume that bundle start implies mandatory DS services are already available.

## Callouts and events

An annotated IColumnCallout identifies a real table/column through @Callout and uses the target start(ctx, windowNo, tab, field, value, oldValue) signature. Preserve legacy CalloutEngine if that is the bundle's existing mechanism. Handle null/reentrant changes and check setValue/error semantics in core.

For an AbstractEventHandler, register only required table/topics, implement the target handleEvent and package its DS descriptor. For delegates, consult the event-annotation skill when available or inspect the actual manager/base/delegate source. Keep every operation inside its owning context/transaction.

## Completion

Inspect the built JAR for expected DS descriptors and resources. Test factory resolution or event dispatch at runtime when an instance is available. Report these separately from compilation. Do not copy a service ranking from an example without understanding which registration it would override.
