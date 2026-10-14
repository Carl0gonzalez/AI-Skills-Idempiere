# Registration shape

Verify the installed REST plugin defines `com.trekglobal.idempiere.rest.api.ResourceExtension` before using this shape. Reuse an existing service where possible:

```java
@Component(service = ResourceExtension.class)
public class Resources implements ResourceExtension {
    @Override
    public Set<Class<?>> getResourceClasses() {
        return Collections.singleton(OrderResource.class);
    }
}
```

Imports, ranking, immediate activation, JAX-RS namespace and endpoint prefix come from the target bundle. Ensure DS output is generated and included in the packaged JAR. Route registration, authorization and business behavior require separate runtime evidence.
