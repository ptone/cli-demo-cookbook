# Ruby MCP Server

This document describes the process of building a simple Ruby-based [Model Context Protocol (MCP)](https://modelcontextprotocol.io/overview) server using an AI assistant. The goal is to create a server that provides basic system information through a set of tools, while also being easy to test and extend.

This is not about the final code, but about the journey to get there. The prompts below are the key steps to guide an AI assistant to build this solution.

## Getting Started

To run the final solution, you will need to have `just` and a working Ruby environment with `rbenv` installed.

1.  Navigate to the `possible-solution` directory:
    ```bash
    cd ruby-mcp-server/possible-solution
    ```
2.  Install the dependencies:
    ```bash
    bundle install
    ```
3.  Start the server:
    ```bash
    just serve
    ```
4.  In a separate terminal, run the tests:
    ```bash
    just test-em-all
    ```

## Building the Solution with an LLM

The following prompts were used to guide the AI assistant in building this solution. They are presented here as a reference for others who want to embark on a similar journey.

### 1. Initial Server Setup

```markdown
Hi, I want to create a little sinatra web server in ruby listening on port 4242. If possible, I'd like this to be an MCP server servinc some silly info like datetime and current location, and hostname, and uname.
```

This prompt sets the initial goal: a Sinatra-based server that provides some basic system information.

### 2. Refining the Output

```markdown
small nit: I'd like the hostname to be SHORT and this should work on both linux and mac. The location should be "city, country" - the comma will allow user to parse it back :)
```

```markdown
uname should be uname -a, Im just interested in Darwin/Mac.
```

These prompts refine the output of the server, making it more user-friendly and easier to parse.

### 3. Introducing the MCP Concept

```markdown
ok, now the tricky part. This should be an MCP server, for LLMs to interact with it. Are you familiar with MCP protocol? There are a few ruby gems to do it.
```

This prompt introduces the core concept of the MCP server and asks the AI assistant to research and select a suitable gem.

### 4. Adding a Comprehensive Test Suite

```markdown
Now add a test-em-all target which tests each single test. Also make sure curl is cleaned up of those Total/Current/Speed garbage thanks.
```

This prompt introduces the idea of a comprehensive test suite and asks the AI assistant to clean up the output of the test commands.

### 5. Implementing Robust Error Handling

```markdown
Marvellous! One final nit - I want the code to be handling ERRORS nicely. I want some exception handling, so if an error occurs, the tool safely returns a json with { error: "Error from exception" } and some other stuff, like return code or whatever makes sense to you. The important thing is the "error" part in the JSON. To test it, we can create a error_test tool in the code which always returns a raise "This is a permanent error to test error handling".
```

This prompt introduces the concept of robust error handling and asks the AI assistant to implement a global error handler.

### 6. Adding Verbose Error Reporting

```markdown
add an option to the get_error with verbose defaulting to false. If verbose, also show backtrace. if verbose is NOT defined, also dont show backtrace. Not this verbose can only be used from the error tool, but good enough.
```

This prompt adds a feature to the error handling, allowing the user to get more detailed error information when needed.
