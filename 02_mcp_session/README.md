# MCP Sessions and State

This example demonstrates an MCP session that stores shopping-cart state and a product quantity while the client is connected.

## Files

- `server.py` defines the cart tools and uses FastMCP `Context` state.
- `client.py` creates a session, loads the tools, and calls them through `MultiServerMCPClient`.

## Tools

- `add_to_cart(item)` adds an item to the current session cart and decreases the product quantity.
- `show_cart()` returns the current cart.
- `show_product_quantity()` returns the remaining quantity.
- `get_session_id()` returns the current MCP session ID.

The initial product quantity is `100`.

## Run

Run from the repository root:

```powershell
uv run python .\02_mcp_session\client.py
```

The client starts `server.py` automatically. The same MCP session is used for the cart operations in this example.
