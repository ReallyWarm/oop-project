import sys
sys.path.append('./class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 

if __name__ == '__main__':
    # Set up the class object
    system = System()
    category = system.category
    hand_tools_type = TypeOfTool(name='Hand tools')
    drills_type = SubtypeOfTool(name='Drills')
    nothing = SubtypeOfTool(name='None')

    # Create test Tool objects in Catalog
    category.add_type(hand_tools_type)
    category.type_add_subtype(hand_tools_type, drills_type)
    category.type_add_subtype(hand_tools_type, nothing)
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    faifa_drill = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    sawaan = Tool('03x', 'Sawaan', 'go to hell', 'HEAVEN', 15, None, 2000.00, 'Drills')
    category.subtype_add_tool(drills_type, test_drill)
    category.subtype_add_tool(drills_type, faifa_drill)
    category.subtype_add_tool(drills_type, sawaan)
    print(test_drill)

    # Search tool
    search = category.search_by_name('')
    testing = search['Testing drill']
    faifa = search['faifa drill']

    # Add to Cart
    system.add_to_cart(testing, 10)
    system.add_to_cart(faifa, 20)
    print(system.system_cart.cart[0].tool.price)
    print(system.system_cart)
    print('----------------------------------------------------------------')
    # Add same tool, but with different amount
    system.add_to_cart(testing, 20)
    print(system.system_cart)



