# Demo Summary

This demo uses Gemini CLI to update and modernize the AcmePools application.



## Setup

First clone the java-8 repo from 2022:

`git clone https://github.com/javaee-samples/javaee8-applications.git`

Change into the Acmepools sample app

`cd javaee8-applications/AcmePools/`

Then start the Gemini CLI

### Initial Prompt

> "update this application to Java 21"

### Follow-up Prompts

The user then guided the process with these follow-up prompts:

> "Now that the build is working succesfully - can you review the code and suggest 3-4 useful modernizations or improvements that are now possible with the currently used version of java?"

> "lets begin with your first suggestion"

> "how would you describe the test coverage of this app, from poor to excellent - score of 1-10"

> "can we get a few basic tests started for this application, pick the most impactful areas to write tests for to start"

### Features and Capabilities Demonstrated

*   **Java and Jakarta EE Migration:** Updated the application from Java 8 and Java EE 8 to Java 21 and Jakarta EE 10. This involved updating the `pom.xml`, replacing `javax.*` with `jakarta.*` namespaces, and resolving dependency and compilation issues.
*   **Code Modernization:**
    *   Identified opportunities to use modern Java features like Records, `var`, Switch Expressions, and Text Blocks.
    *   Converted several Plain Old Java Objects (POJOs) into Records to reduce boilerplate code.
*   **Test Coverage Improvement:**
    *   Assessed the initial test coverage as "Poor" (1/10).
    *   Added JUnit 5 and Mockito dependencies to the project.
    *   Created a new test source directory (`src/test/java`).
    *   Wrote initial unit tests for key business logic (Facades) and a JSF controller.
    *   Debugged and resolved several test failures related to dependency versions, environment compatibility, and incorrect mocking.

### Review of Steps Taken by Gemini CLI

1.  **Analyzed `pom.xml`:** The CLI started by reading the `pom.xml` to understand the project's current dependencies and build configuration.
2.  **Updated `pom.xml`:** The CLI updated the `pom.xml` to use Java 21, Jakarta EE 10, and updated versions of dependencies like PrimeFaces and Lombok.
3.  **Replaced `javax` with `jakarta`:** The CLI performed a global search and replace to update all `javax.*` imports to their `jakarta.*` equivalents across the entire codebase.
4.  **Handled Deprecated Code:** The CLI identified and replaced the deprecated `sun.misc.BASE64Encoder` and `sun.misc.BASE64Decoder` with the modern `java.util.Base64`.
5.  **Iterative Build and Debug:** The CLI attempted to build the project, identified compilation errors, and iteratively fixed them. This included:
    *   Adding the `jakarta` classifier to the PrimeFaces dependency.
    *   Correcting the `maven-compiler-plugin` configuration.
    *   Fixing incorrect annotations and imports.
    *   Resolving issues with constructor calls after converting classes to records.
6.  **Code Modernization (Records):** Based on the user's request, the CLI converted several classes (`JobEvent`, `ColumnModel`, `Owner`) into Java Records.
7.  **Test Implementation:**
    *   Added test dependencies to the `pom.xml`.
    *   Created the test directory structure.
    *   Wrote new unit tests for `CustomerFacade`, `JobFacade`, and `CustomerController`.
    *   Debugged and fixed test failures by:
        *   Updating test dependency versions to be compatible with the user's Java 24 environment.
        *   Configuring the `maven-surefire-plugin` to handle Byte Buddy experimental features.
        *   Correcting Mockito stubbing issues.
8.  **Final Successful Build:** The CLI ran a final build, which compiled the application and successfully ran all the new tests.
9.  **Session Summary:** Finally, the CLI generated this summary of the session and appended it to the `README.md` file.