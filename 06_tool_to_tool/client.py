from fastmcp import Client
import asyncio
from fastmcp.client.transports import PythonStdioTransport
from pathlib import Path
import sys

http_server = "http://127.0.0.1:3001/mcp" 
stdio_server = PythonStdioTransport(Path(__file__).parent/'stdio_server.py', python_cmd=sys.executable)


async def main():
    async with Client(http_server) as http, Client(stdio_server) as stdio:
        result = await http.call_tool('add_then_double',{'num1':2,'num2':4})
        print(f"01 : {result.data}")
        
        result2 = await stdio.call_tool('add_then_double',{'num1':2,'num2':4})
        print(f"02 : {result2.data}")
        

if __name__=="__main__":
    asyncio.run(main())