# MCP Notifications

This example demonstrates MCP log messages and progress notifications while a tool is running.

## Files

- `http_server.py` exposes `do_work()` over HTTP on port `3001`.
- `server.py` exposes the same tool over stdio.
- `client.py` connects to both servers and registers callbacks for logs and progress updates.

## Tool behavior

`do_work()` performs three simulated steps. Each step:

1. Waits for one second.
2. Sends a log message with `ctx.info()`.
3. Sends a progress update with `ctx.report_progress()`.

After the notifications, the tool returns `Job done!`.

## Run

Start the HTTP server in one terminal:

```powershell
uv run python .\05_notification\http_server.py
```

Keep it running, then open a second terminal and run:

```powershell
uv run python .\05_notification\client.py
```

The client starts the stdio server automatically and connects to the HTTP server at:

```text
http://127.0.0.1:3001/mcp
```

You should see log messages, progress updates from `1 / 3` through `3 / 3`, and a final `Job done!` result.
