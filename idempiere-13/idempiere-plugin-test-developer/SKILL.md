---
name: idempiere-plugin-test-developer
description: Generates unit tests, mocks, and isolation strategies for iDempiere plugin components using an existing test project or fragment and its declared test framework.
---

# Purpose

This skill guides the creation of unit tests, stubs, mocks, and isolation strategies for iDempiere plugin components. It targets test classes inside an existing test project or unit-test fragment.

It should be activated when the user asks to:
- Generate unit tests for processes, callouts, validators, or utilities
- Design test fixtures, stubs, or mocks for iDempiere domain objects
- Propose refactoring to make tightly coupled iDempiere classes testable
- Write unit tests using JUnit 5 and Mockito

# Operating Principles

1. **Build on Top**: Inspect the existing test project, its build descriptor, and available test libraries before writing tests. Focus on Java test classes unless dependency changes are explicitly requested.
2. **Prioritize Isolation**: Avoid fragile tests that depend on a live database connection or full server boot. Mock static contexts (`Env`, `DB`, `Trx`, `PO`) or refactor the code to allow pure unit testing of business logic.
3. **Testability Analysis**: Before writing tests for a highly coupled class, evaluate if it requires a refactor. If so, propose a minimal refactor (e.g., extracting logic, injecting dependencies, parameterizing methods) before writing the test cases.
4. **Behavioral Testing**: Name test methods clearly based on the behavior being tested (e.g. `shouldCalculateDiscountWhenTotalExceedsThreshold`).
5. **Arrange-Act-Assert (AAA)**: Separate test phases clearly. Ensure test coverage covers happy paths, validation failures, boundary/limit conditions, nulls, and error exceptions.

# Activation Guidance

Trigger this skill for prompts like:
- "genera tests para este SvrProcess"
- "crea pruebas para este Callout"
- "ayúdame a testear este ModelValidator"
- "propón refactor para que esta clase de plugin sea testeable"
- "escribe pruebas unitarias de JUnit 5 para este helper del plugin"

# Constraints

- **Scope Limit**: Do NOT create project structure folders, maven configuration poms, or OSGi MANIFEST.MF metadata files. Focus strictly on creating Java test classes and test utilities inside the test project's `src/` folder.
- **Dependency Boundary**: Never add third-party testing libraries to the project's dependency config unless explicitly asked. Rely on JUnit 5, Mockito, and standard Java reflection.

---

# Testability & Isolation Strategy

When auditing a class for testing, classify the approach:

### 1. Pure Unit Test
* **Use when**: The class under test does not call static iDempiere classes (`Env`, `DB`, `Msg`, `MSysConfig`) or database models (`PO`, `Query`).
* **Approach**: Standard JUnit 5 test with Mockito mocks if needed.

### 2. Tightly Coupled Class (Propose Refactor)
* **Use when**: The business logic is mixed with static database calls or environment reads (e.g. `DB.getSQLValueEx(...)` or `Env.getCtx()`).
* **Approach**: Recommend a refactor. Extract the pure logic to a separate helper class or a package-private method that takes the resolved values as arguments.
  * **Bad**: `public int calculateVal() { int multiplier = DB.getSQLValue(null, "SELECT Val FROM..."); return multiplier * qty; }`
  * **Good (Refactored)**: `public int calculateVal() { return calculateVal(DB.getSQLValue(null, "SELECT...")); }` and `int calculateVal(int multiplier) { return multiplier * qty; }` (we can test the second method directly).

### 3. Framework Dependency (Mocking and Reflection)
* **Use when**: Refactoring is not allowed or is too risky.
* **Approach**: Use Mockito static mocking only if the existing dependencies support it; otherwise use narrowly scoped reflection helpers or propose a refactor.

### 4. Integration Test
* **Use when**: The class under test contains critical database queries or native SQL logic that cannot be easily mocked or extracted, and actual database validation is required.
* **Approach**: Implement integration tests that inherit from iDempiere's integration test bases (e.g., configuring target platform, starting DB transaction, and performing assertions, ensuring rollbacks are performed at cleanups).


---

# Workflow

1. **Analyze Component**: Identify the type of component (Process, Callout, Validator, Utility).
2. **Assess Testability**: Check for static dependencies. If highly coupled, present a refactoring proposal to the user first.
3. **Draft the Test Class**:
   - Locate the target test class path (e.g., `com.example.recaptcha.test` fragment).
   - Write the JUnit 5 test following the AAA pattern.
4. **Output the Code**:
   - Provide file paths and full Java code.
   - Explain what is being tested and how static dependencies are isolated.

# Output Contract

When generating tests, produce:
1. **Target test file path** within the unit test fragment.
2. **Refactor proposal** (if code needs isolation).
3. **Full Java test code** with imports, package name, test class, and assertion cases.

---

# Testing Templates

### 1. Testing a SvrProcess
```java
package com.example.plugin.process.test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.HashMap;
import java.util.Map;
import org.compiere.process.ProcessInfo;
import org.compiere.process.ProcessInfoParameter;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.example.plugin.process.MyCustomProcess;

class MyCustomProcessTest {

	private MyCustomProcess process;

	@BeforeEach
	void setUp() {
		process = new MyCustomProcess();
	}

	@Test
	void shouldFailWhenParameterIsInvalid() {
		// Arrange
		ProcessInfoParameter p1 = new ProcessInfoParameter("ParameterName", 0, null, null, null);
		ProcessInfo pi = new ProcessInfo("MyProcess", 100);
		pi.setParameter(new ProcessInfoParameter[]{p1});

		// Act & Assert
		assertThrows(Exception.class, () -> {
			// This exercises prepare() and doIt()
			process.startProcess(null, pi, null);
		});
	}
}
```

### 2. Testing a Callout (Stubbing UI Contexts)
```java
package com.example.plugin.callout.test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.Properties;
import org.compiere.model.GridField;
import org.compiere.model.GridTab;
import org.junit.jupiter.api.Test;
import com.example.plugin.callout.MyCallout;

class MyCalloutTest {

	@Test
	void shouldUpdateAnotherColumnValue() {
		// Arrange
		MyCallout callout = new MyCallout();
		Properties ctx = new Properties();
		GridTab mTab = mock(GridTab.class);
		GridField mField = mock(GridField.class);

		// Act
		callout.validateField(ctx, 1, mTab, mField, "TriggerValue");

		// Assert
		verify(mTab).setValue("AnotherColumn", "NewValue");
	}
}
```

### 3. Reflection Helper for Static Contexts
```java
package com.example.plugin.test.util;

import java.lang.reflect.Field;

public class ReflectionTestUtil {
	public static void setStaticFieldValue(Class<?> clazz, String fieldName, Object newValue) throws ReflectiveOperationException {
		Field field = clazz.getDeclaredField(fieldName);
		field.setAccessible(true);
		field.set(null, newValue);
	}
}
```
