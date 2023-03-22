import sys
sys.path.append('./web_app/class_object/')
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
    category.add_type_of_tool(hand_tools_type)
    hand_tools_type.add_subtype(drills_type)
    hand_tools_type.add_subtype(nothing)
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    faifa_drill = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    sawaan = Tool('03x', 'Sawaan', 'go to hell', 'HEAVEN', 15, None, 2000.00, 'Drills')
    drills_type.add_tool(test_drill)
    drills_type.add_tool(faifa_drill)
    drills_type.add_tool(sawaan)
    print(test_drill)

    # Search tool
    ht = category.types_of_tool[0]
    dr = ht.subtypes_of_tool[0]
    tdr = dr.tools_list[1]

    # Add to Cart
    system.add_to_cart(tdr, 10)
    print(system.system_cart.carts[0].tool.price)
    print(system.system_cart)