from fastmcp import FastMCP

mcp = FastMCP('FRST_MCP_SERVER')

@mcp.tool
def add(num1:int, num2:int)->int:
    '''use this tool to add two numbers'''
    return num1+num2

@mcp.tool
def unique_way_print(name:str)->str:
    '''use this tool to print name in unique way'''
    return 'haha'+name

@mcp.tool
def default_number_of_printing(name:str) -> str:
    '''Use this tool to get the default times of printing'''
    return f"{name}"*5

@mcp.tool
def greet()->int:
    '''this is greet tool, based upon the name it will greet the user.'''
    return 5

if __name__ == '__main__':
    mcp.run(transport='stdio')
