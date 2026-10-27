from fastmcp import FastMCP
mcp = FastMCP("FRSTMCPSERVER")


@mcp.tool
def greet(name:str):
    """use this tool to greet with person name"""
    return f"hi {name} , welcome to dev team"

if __name__ == "__main__":
    mcp.run(transport='http', host='127.0.0.1', port=3000)