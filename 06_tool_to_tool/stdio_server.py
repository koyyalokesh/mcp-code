from fastmcp import FastMCP, Client


mcp = FastMCP('HTTP-SERVER')

HTTP_SERVER = 'http://127.0.0.1:3001/mcp'

@mcp.tool
async def add_then_double(num1:float, num2:float)->float:
    """use this tool to add number then pass to double tool to double the value """
    add_value = num1 + num2
    async with Client(HTTP_SERVER) as http:
        result = await http.call_tool('double', {'num': add_value})
        return result.data

@mcp.tool
async def double(num:float)->float:
    """this is a tool used to add 2 numbers"""
    return num*2
    


if __name__ == "__main__":
    mcp.run(transport='stdio',show_banner=False)
