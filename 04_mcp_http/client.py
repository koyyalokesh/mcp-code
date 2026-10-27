

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        'greeting':{
            'transport':'streamable_http',
            'url':'http://127.0.0.1:3000/mcp'
        }
    })
    
    tools = await client.get_tools()
    
    
    llm = ChatOpenAI(model="gpt-4o-mini")
    llm_with_tools = llm.bind_tools(tools=tools)
    messages=[HumanMessage(content='hey greet lokesh')]
    response = await llm_with_tools.ainvoke(messages)
    messages.append(AIMessage(content=response.content, tool_calls=response.tool_calls))
    tools_by_name = {tool.name:tool for tool in tools}
    
    for tool_call in response.tool_calls:
        tool = tools_by_name[tool_call['name']]
        response = await tool.ainvoke(tool_call['args'])
        #print(response[0]['text'])
        messages.append(ToolMessage(content=response[0]['text'], tool_call_id=tool_call['id']))
    
    final_response = await llm_with_tools.ainvoke(messages)
    print(final_response.content)
    
if __name__=="__main__":
    asyncio.run(main())