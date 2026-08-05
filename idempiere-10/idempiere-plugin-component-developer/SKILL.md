---
name: idempiere-plugin-component-developer
description: Develops iDempiere internal components (Processes, Callouts, Validators, Factories) in an existing plugin skeleton, following that plugin's proven OSGi registration conventions.
---

# Purpose

This skill guides the creation of internal business logic components for existing iDempiere OSGi plugin projects. It focuses on generating clean, performant, and secure Java classes (Processes, Callouts, Model Validators, Factories) that conform to modern iDempiere standards.

It should be activated when the user asks to:
- Write a new process extending `SvrProcess` or `CustomProcess`
- Create callout classes for fields and columns
- Implement `IModelValidator` classes for record validation
- Implement factories (`IProcessFactory`, `IModelFactory`, `IFormFactory`, etc.)
- Develop database access logic or transaction handling within a plugin

This skill must NOT attempt to generate plugin skeleton structure, configuration pom.xml files, or MANIFEST.MF metadata, unless explicitly requested.

# Operating Principles

1. **Build on Top**: Assume the OSGi project skeleton, MANIFEST.MF, and build configurations are already created. Focus exclusively on Java source files.
2. **Registration Compatibility**: Inspect `MANIFEST.MF`, `build.properties`, and existing component registrations before adding a factory. Preserve the target bundle's convention, which may be `OSGI-INF/*.xml` or DS annotations.
3. **Transaction Safety**: Always handle transactions (`Trx`) correctly. Keep database operations inside try-with-resources and commit/rollback properly.
4. **PostgreSQL / SQL Best Practices**: Avoid SQL injection. Never concatenate inputs in SQL strings. Use bind variables and prepared statements.
5. **Data Dictionary Ready**: Remind the user of the specific Application Dictionary configurations needed to activate the new code in iDempiere.

# Activation Guidance

Trigger this skill for prompts like:
- "create a callout for C_Order.DateOrdered to change the date promised"
- "implement a process class to close outdated inactive requests"
- "develop a model validator to enforce that prices are not below cost"
- "write a process factory for com.cdsoftware.recaptcha"

# Constraints

- **Scope Limit**: Do NOT generate parent directories, build pom files, or Eclipse metadata files. Focus on the `src/` folder contents of the target plugin.
- **OSGi Structure Constraint**: NEVER attempt to create the OSGi project skeleton from scratch or modify the `MANIFEST.MF` file, unless explicitly requested by the user. Always assume they already exist and build strictly on top of them.
- **Security Constraint**: Do NOT allow direct string concatenations in database queries. Always use `DB.getSQLValueEx` or `PreparedStatement`.
- **Registration Boundary**: Do not introduce a second registration mechanism into a bundle. Use the convention already packaged by the target plugin and ensure any required resource is included in `build.properties` and declared by `MANIFEST.MF` when the user authorizes metadata changes.

# Workflow

When writing a component, follow these ordered steps:

1. **Determine Component Type**: Define if it is a Process, Callout, Validator, or Factory.
2. **Inspect integration convention**: Identify the existing factory/callout base classes and OSGi registration mechanism before drafting code.
3. **Draft the Java class**:
   - Write correct imports.
   - Use annotations:
     - For Factories: Use `@Component(property = {"service.ranking:Integer=100"}, service = IProcessFactory.class)` (adjust for target factory).
     - For Model Validators: Use `@Component(property = {"service.ranking:Integer=100"}, service = IModelValidator.class)`.
3. **Apply Database Security Rules**:
   - For simple lookups: Use `DB.getSQLValueEx(trxName, sql, params)`.
   - For loops/queries: Use `PreparedStatement` inside a try-with-resources block:
     ```java
     String sql = "SELECT AD_User_ID FROM AD_User WHERE Name = ?";
     try (PreparedStatement pstmt = DB.prepareStatement(sql, trxName)) {
         pstmt.setString(1, name);
         try (ResultSet rs = pstmt.executeQuery()) {
             while (rs.next()) {
                 // logic
             }
         }
     } catch (SQLException e) {
         throw new AdempiereException(e);
     }
     ```
4. **Apply Transaction Rules**:
   - Do not commit transactions that do not belong to your process.
   - If a new transaction is required:
     ```java
     Trx trx = Trx.get("my_transaction_name", true);
     try {
         // operations
         trx.commit(true);
     } catch (Exception e) {
         trx.rollback();
         throw e;
     } finally {
         trx.close();
     }
     ```
6. **Prepare Application Dictionary Guide**:
   - Append a clear documentation header or comment explaining where and how to configure the component in the iDempiere UI (e.g. "Report & Process", "Table and Column -> Callout", "Model Validator" tab, etc.).

# Output Contract

When creating a component, produce:
1. **Target file path** relative to the project.
2. **Full Java code** with imports, package name, class definition, and annotations.
3. **AD Registration Instructions**: Structured markdown instructions explaining how to link this class to the iDempiere Data Dictionary.

# Example Component Templates

### 1. Process Class
```java
package com.cdsoftware.plugin.process;

import java.util.logging.Level;
import org.adempiere.exceptions.AdempiereException;
import org.compiere.process.ProcessInfoParameter;
import org.compiere.process.SvrProcess;

/**
 * AD Registration:
 * 1. Open "Report & Process" window.
 * 2. Create a new record with ClassName = com.cdsoftware.plugin.process.MyCustomProcess
 */
public class MyCustomProcess extends SvrProcess {

	private int parameterValue = 0;

	@Override
	protected void prepare() {
		for (ProcessInfoParameter para : getParameter()) {
			String name = para.getParameterName();
			if (name.equals("ParameterName")) {
				parameterValue = para.getParameterAsInt();
			} else {
				log.log(Level.SEVERE, "Unknown Parameter: " + name);
			}
		}
	}

	@Override
	protected String doIt() throws Exception {
		if (parameterValue <= 0) {
			throw new AdempiereException("Invalid parameter value");
		}
		// business logic
		return "Process completed successfully.";
	}
}
```

### 2. Callout Class
```java
package com.cdsoftware.plugin.callout;

import java.util.Properties;
import org.compiere.model.CalloutEngine;
import org.compiere.model.GridField;
import org.compiere.model.GridTab;

/**
 * AD Registration:
 * 1. Open "Table and Column" window, find target table and column.
 * 2. Set Callout = com.cdsoftware.plugin.callout.MyCallout.validateField
 */
public class MyCallout extends CalloutEngine {

	public String validateField(Properties ctx, int WindowNo, GridTab mTab, GridField mField, Object value) {
		if (value == null) {
			return "";
		}
		// logic
		mTab.setValue("AnotherColumn", "NewValue");
		return "";
	}
}
```
