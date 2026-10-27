# MCP Without an Explicit Session

This example shows a client loading MCP tools without explicitly opening and managing a session context.

## Files

- `server.py` exposes an `add_to_cart(item)` tool.
- `client.py` uses `MultiServerMCPClient.get_tools()` and invokes the tool twice.

## Run

Run from the repository root:

```powershell
uv run python .\03_mcp_no_session\client.py
```

The client starts `server.py` automatically over stdio. This example is useful for comparing direct tool loading with the explicit session handling shown in [02_mcp_session](../02_mcp_session).
