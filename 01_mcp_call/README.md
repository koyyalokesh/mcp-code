# Basic MCP Tool Calling

This example shows how a LangChain client discovers tools from a local FastMCP server and lets an OpenAI model choose and call a tool.

## Files

- `server.py` defines the MCP tools.
- `client.py` starts the server over stdio, loads its tools, and connects them to `gpt-4o-mini`.

## Tools

- `add(num1, num2)` adds two integers.
- `unique_way_print(name)` returns the name with a simple prefix.
- `default_number_of_printing(name)` repeats a name five times.
- `greet()` returns `5`.

## Setup

Create a `.env` file in the repository root and add your OpenAI key:

```env
OPENAI_API_KEY=your-api-key
```

The `.env` file is ignored by Git and must not be committed.

## Run

Run from the repository root:

```powershell
uv run python .\01_mcp_call\client.py
```

The client starts `server.py` automatically, so the server does not need to be started separately.
