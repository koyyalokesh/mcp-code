from fastmcp import FastMCP
from fastmcp.exceptions import ToolError
from pathlib import Path
mcp = FastMCP('Frstserver', mask_error_details=True)

@mcp.tool
async def divide(num1:int, num2:int)->float:
    """use this tool to divide the number"""
    if num2 == 0:
        raise ToolError("Cannot divide by zero. Please use a different number for num2.")
    return num1/num2

@mcp.tool
def file_read():
    """A tool with a bug: it opens a file that does not exist."""
    return open(Path(__file__).parent/"test.txt").read()

if __name__=="__main__":
    mcp.run(transport='stdio', show_banner=False)