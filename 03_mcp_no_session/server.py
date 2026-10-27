from fastmcp import FastMCP,Context
import asyncio
mcp = FastMCP('frstmcpserver')

DEFAULT_PRODUCT_QUANTITY = 100

@mcp.tool
async def add_to_cart(item:str, context:Context):
    """Add an item to the shopping cart of the current session."""
    cart = await context.get_state("cart")
    product_quantity = await context.get_state("product_quantity")
    
    if product_quantity is None:
        product_quantity = DEFAULT_PRODUCT_QUANTITY
    
    await context.set_state('product_quantity', product_quantity-1)
    
    if cart is None:
        cart = []
    cart.append(item)
    await context.set_state('cart',cart)
    return f"Added {item}. Cart now has {len(cart)} item(s)."


if __name__ =="__main__":
    mcp.run(transport ='stdio')