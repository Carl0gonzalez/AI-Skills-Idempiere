# Minimal form checks

Keep the example conceptual until the target API is verified:

```java
ClassLoader original = Thread.currentThread().getContextClassLoader();
try {
    Thread.currentThread().setContextClassLoader(getClass().getClassLoader());
    view = Executions.createComponents(resourcePath, this, arguments);
} finally {
    Thread.currentThread().setContextClassLoader(original);
}
Selectors.wireComponents(view, this, false);
```

The controller wires its listeners after constructing the UI. Ensure IDs and nested scopes match, component fields belong to the correct class, and the constructor uses the final class name. A missing resource is an error, not an empty successful form. Verify close/dispose and callback signatures in the actual release.
