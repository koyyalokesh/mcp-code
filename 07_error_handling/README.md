# MCP Error Handling

This example demonstrates how a FastMCP server reports tool errors and how an MCP client receives and displays them.

## Files

- `server.py` defines the tools and configures error-detail masking.
- `client.py` calls the tools and prints either an `OK` or `ERROR` result.

## Tools

### `divide(num1, num2)`

Divides `num1` by `num2`. If `num2` is zero, the server raises a clear `ToolError`:

```text
Cannot divide by zero. Please use a different number for num2.
```

### `file_read()`

Attempts to read `test.txt`. The file is intentionally missing so the example demonstrates an unexpected tool failure.

## Error handling flow

```text
Client calls a tool
        |
        v
Server executes the tool
        |
        +-- Success -> result.isError is False -> OK
        |
        `-- Failure -> result.isError is True  -> ERROR
```

The server uses `mask_error_details=True`, and the client sets `FASTMCP_LOG_LEVEL=CRITICAL` for the child process so the terminal focuses on the error result received by the client.

## Run

Run from the repository root:

```powershell
uv run python .\07_error_handling\client.py
```

The client starts `server.py` automatically over stdio. You should see successful output for `divide(2, 2)` and error output for division by zero and the missing file.

No separate server terminal is required.
