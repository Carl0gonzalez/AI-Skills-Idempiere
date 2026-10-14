# Model registration

Keep generated I_*/X_* classes separate from M* domain behavior. Reuse the existing IModelFactory mapping or verified IMappedModelFactory annotation scan. Check the target interface, PO constructors, annotation, scan package and DS availability. A model package may differ from the activator package; scan the model package explicitly.

Do not add another activator/factory or force Incremental2PackActivator for simple scanning. If the scaffold already extends it for 2Pack lifecycle, preserve that behavior. Generated metadata and Java models must agree before use. In core, the developer generates the database and model artifacts.
