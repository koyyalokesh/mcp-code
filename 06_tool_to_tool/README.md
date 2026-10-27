# Tool-to-Tool MCP Example

This example demonstrates how one MCP tool can call another MCP tool through a different MCP server.

## Project structure

```text
06_tool_to_tool/
|-- client.py         # Calls both MCP servers
|-- http_server.py    # MCP server available over Streamable HTTP
|-- stdio_server.py   # MCP server available over stdio
`-- README.md
```

## How it works

There are two MCP servers:

1. `http_server.py` runs at `http://127.0.0.1:3001/mcp`.
2. `stdio_server.py` is started as a child process when needed.

Both servers expose these tools:

| Tool | Purpose |
| --- | --- |
| `double(num)` | Multiplies a number by two. |
| `add_then_double(num1, num2)` | Adds two numbers and sends the result to `double`. |

The tool-to-tool flow is:

```text
add_then_double(2, 4)
        |
        |-- 2 + 4 = 6
        |
        `-- double(6) = 12
```

The HTTP and stdio servers demonstrate both directions:

- The HTTP server starts the stdio server and calls its `double` tool.
- The stdio server connects to the HTTP server and calls its `double` tool.

## Requirements

From the project root, install the dependencies with:

```powershell
uv sync
```

The project requires Python 3.13 or newer.

## Run the example

Start the HTTP server in one terminal:

```powershell
uv run python .\06_tool_to_tool\http_server.py
```

Keep that terminal running. Then open a second terminal and run the client:

```powershell
uv run python .\06_tool_to_tool\client.py
```

Expected output:

```text
01 : 12
02 : 12
```

The client makes two calls:

- `01` calls `add_then_double` through the HTTP server.
- `02` calls `add_then_double` through the stdio server.

Both calls add `2 + 4` and then double the result, so both return `12`.

## Important notes

- Start `http_server.py` before running `client.py`.
- Do not start `stdio_server.py` manually; `PythonStdioTransport` starts it automatically.
- Stop the HTTP server with `Ctrl+C` when you are finished.
