# HTTP Client Modernization Demo

This demo showcases the Gemini CLI's ability to modernize a legacy Python script. The project starts with a simple synchronous HTTP client using the `requests` library and evolves it into a modern, asynchronous client using `httpx`, `pydantic`, and `asyncio`.

## Scenario

The user requested to upgrade a `requests`-based `client.py` to a modern stack, test it against the provided `server.py`, and ensure it handles various HTTP features correctly.

### Key Initial Prompt

> "I would like to modernize the http client in this project to use the httpx library, work with structured data using pydantic models, and switch to using asyncio based async flows. The server is running, so please test the new client when finished"

### Key Follow-up Actions

After an initial refactoring, Gemini CLI identified a bug where HTTP redirects were not being handled as expected. It then autonomously debugged and corrected the code.

> "The modernized client is almost working correctly. I noticed an issue with the redirect handling... I will correct the code to ensure redirects are followed."

## Gemini CLI Steps

1.  **Code Comprehension:** Gemini started by reading `client.py`, `server.py`, and `requirements.txt` to understand the project's current state.
2.  **Dependency Management:** It updated `requirements.txt` to replace `requests` with `httpx` and `pydantic` and then used `pip` to install the new dependencies into the existing virtual environment.
3.  **Code Refactoring:** Gemini rewrote `client.py` from scratch, replacing the synchronous `requests` calls with an `asyncio` event loop and an `httpx.AsyncClient`.
4.  **Data Modeling:** It introduced `pydantic` models to provide type-hinting and validation for the JSON data exchanged with the server, making the client more robust.
5.  **Testing and Debugging:** Gemini executed the new client, analyzed the output, and identified that the client was not following HTTP redirects correctly.
6.  **Code Correction:** It fixed the bug by reading the client code again, correctly configuring the `httpx.AsyncClient` to follow redirects, and adjusting the output to properly display the final URL and redirect history.
7.  **Final Verification:** Gemini ran the corrected client one last time to confirm that all features, including redirects, were working as expected.

## Features and Capabilities Demonstrated

*   **Code Analysis and Comprehension:** Understanding an existing codebase across multiple files.
*   **Dependency Management:** Modifying project dependencies and using package managers (`pip`).
*   **Modernization and Refactoring:** Upgrading a legacy codebase to a modern, asynchronous stack.
*   **Testing and Verification:** Running code to test for correctness against a live server.
*   **Debugging and Autonomous Correction:** Identifying functional bugs from output, forming a hypothesis, and implementing a fix without user intervention.
*   **Tool Usage:** Seamlessly using `read_many_files`, `write_file`, and `run_shell_command` to interact with the project.
