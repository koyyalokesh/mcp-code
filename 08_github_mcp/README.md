# GitHub MCP Automation

This example connects LangChain to GitHub's hosted MCP server and performs a complete repository workflow through MCP tools.

## What the client does

The client in `client.py`:

1. Connects to `https://api.githubcopilot.com/mcp`.
2. Reads the authenticated GitHub user with `get_me`.
3. Creates a private repository named `mcp-demo`.
4. Creates a `live-mcp` branch from `main`.
5. Creates `live_mcp.txt` on that branch.
6. Opens and updates a pull request.
7. Creates a pull-request review and adds a review comment.

## Setup

Create a `.env` file in this folder:

```env
GITHUB_PERSONAL_ACCESS_TOKEN=your-github-token
```

The `.env` file is ignored by Git and must never be committed or shared.

The token needs permission to create repositories, write repository contents, and write pull requests. GitHub documents the repository-creation permissions [here](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28).

## Run

Run from this folder:

```powershell
uv run client.py
```

Or run from the repository root:

```powershell
uv run python .\08_github_mcp\client.py
```

## Expected behavior

The client prints the result of each MCP operation. A successful run creates the repository and pull request on GitHub.

If the repository already exists, the `create_repository` step will fail. In that case, either use a new repository name or remove that step and continue with an existing repository.

## Troubleshooting

### `403 Resource not accessible by personal access token`

The token is valid but does not have the permission required for the operation. Update the token permissions or create the repository manually.

### `httpx.ConnectError`

Check your internet connection and proxy settings. If your terminal contains an invalid proxy such as `http://127.0.0.1:9`, clear it temporarily:

```powershell
$env:HTTP_PROXY = ""
$env:HTTPS_PROXY = ""
$env:ALL_PROXY = ""
```
