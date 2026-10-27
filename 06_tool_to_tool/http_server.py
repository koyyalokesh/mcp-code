from fastmcp import FastMCP, Client
from fastmcp.client.transports import PythonStdioTransport
from pathlib import Path
import sys

mcp = FastMCP('HTTP-SERVER')

@mcp.tool
async def add_then_double(num1:float, num2:float)->float:
    """this is a tool used to add 2 numbers"""
    result = num1 + num2
    stdio_server = PythonStdioTransport(Path(__file__).parent/'stdio_server.py', python_cmd=sys.executable)
    async with Client(stdio_server) as stdio:
        result = await stdio.call_tool('double',{'num':result})
        return result.data
  

@mcp.tool
async def double(num:float)->float:
    """use this tool to double the number num."""
    return num*2      



if __name__ == "__main__":
    mcp.run(transport='http',host='127.0.0.1', port=3001)