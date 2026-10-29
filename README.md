# MCP Code Examples

Python examples for learning and experimenting with the Model Context Protocol (MCP) using [FastMCP](https://gofastmcp.com/).

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)

Install the project dependencies from the repository root:

```powershell
uv sync
```

## Examples

| Folder | Description |
| --- | --- |
| [01_mcp_call](./01_mcp_call) | Basic MCP server and client communication |
| [02_mcp_session](./02_mcp_session) | MCP sessions and session state |
| [03_mcp_no_session](./03_mcp_no_session) | MCP communication without a persistent session |
| [04_mcp_http](./04_mcp_http) | Running an MCP server over HTTP |
| [05_notification](./05_notification) | MCP notifications |
| [06_tool_to_tool](./06_tool_to_tool) | One MCP tool calling another MCP tool |
| [07_error_handling](./07_error_handling) | Handling expected and unexpected MCP tool errors |
| [08_github_mcp](./08_github_mcp) | Automating GitHub workflows through MCP |

Each example folder contains its own Python files and may include a detailed README with setup and run instructions.

## Running an example

Run commands from the repository root. For example, the tool-to-tool example requires the HTTP server to be started first:

```powershell
uv run python .\06_tool_to_tool\http_server.py
```

Then, in a second terminal:

```powershell
uv run python .\06_tool_to_tool\client.py
```

See the [06_tool_to_tool README](./06_tool_to_tool/README.md) for the complete explanation.

## Project layout

```text
mcp-code/
|-- 01_mcp_call/
|-- 02_mcp_session/
|-- 03_mcp_no_session/
|-- 04_mcp_http/
|-- 05_notification/
|-- 06_tool_to_tool/
|-- 07_error_handling/
|-- 08_github_mcp/
|-- src/mcp_code/
|-- pyproject.toml
|-- uv.lock
`-- README.md
```

## Security

Do not commit API keys or other secrets. Store local environment variables in `.env` files; these files are excluded by `.gitignore`.
