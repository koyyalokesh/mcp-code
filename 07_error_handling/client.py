from langchain_mcp_adapters.client import MultiServerMCPClient

import asyncio
from pathlib import Path
import sys

SERVER_PATH = Path(__file__).parent/"server.py"


async def try_tool_call(session, tool_name, arguments):
    result = await session.call_tool(tool_name,arguments)
    tool_output = result.content[0].text
    if result.isError:
        print("  ERROR ->", tool_output)
    else:
        print("  OK    ->", tool_output)
        
        

async def main():
    client = MultiServerMCPClient(
        {
        'stdio_server':{
            'transport':'stdio',
            'command':sys.executable,
            'args':[str(SERVER_PATH)],
            #Hide the server's own error logs, so we only see what
            # the CLIENT receives.
            "env": {"FASTMCP_LOG_LEVEL": "CRITICAL"},
            
        }
    }
    )
    
    async with client.session('stdio_server') as session:
        await try_tool_call(session, 'divide', {'num1':2, 'num2':2})
        await try_tool_call(session, 'divide', {'num1':2, 'num2':0})
        await try_tool_call(session, 'file_read',{})
    


if __name__=="__main__":
    asyncio.run(main())