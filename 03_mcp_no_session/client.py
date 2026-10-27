import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import sys
from pathlib import Path
from langchain_mcp_adapters.tools import load_mcp_tools

SERVER_PATH = Path(__file__).parent / "server.py"
async def main():
    client = MultiServerMCPClient({
        'cart_server':{
            'transport':'stdio',
            'command':sys.executable,
            "args":[str(SERVER_PATH)]
        }
    })
    
    tools = await client.get_tools()
    tools_by_name={tool.name: tool for tool in tools}
    
    result = await tools_by_name['add_to_cart'].ainvoke({"item":"apple"})
    print(result[0]['text'])
    result = await tools_by_name['add_to_cart'].ainvoke({"item":"banana"})
    print(result[0]['text'])
    
if __name__ =="__main__":
    asyncio.run(main())