# MCP over Streamable HTTP

This example shows an MCP server exposed over Streamable HTTP and a LangChain client connecting to it.

## Files

- `server.py` exposes a `greet(name)` tool over HTTP on port `3000`.
- `client.py` discovers the HTTP tool, lets `gpt-4o-mini` call it, and prints the final response.

## Setup

Create a `.env` file in the repository root:

```env
OPENAI_API_KEY=your-api-key
```

## Run

Start the server in one terminal:

```powershell
uv run python .\04_mcp_http\server.py
```

Keep it running, then open a second terminal and run the client:

```powershell
uv run python .\04_mcp_http\client.py
```

The server endpoint is:

```text
http://127.0.0.1:3000/mcp
```

Stop the server with `Ctrl+C` when finished.
