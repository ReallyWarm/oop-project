import sys
sys.path.append('./web_app/class_object/')
import time
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System

if __name__ == '__main__':
    # Set up the class object
    system = System()
    category = system.category
    # Create types of tool
    hand_tools_type = TypeOfTool(name='Hand tools')
    garden_tools_type = TypeOfTool(name='Garden tools')
    kitchen_tools_type = TypeOfTool(name='Kitchen tools')
    # Create subtypes of tool
    drills_type = SubtypeOfTool(name='Drills')
    saws_type = SubtypeOfTool(name='Saws')
    hammers_type = SubtypeOfTool(name='Hammers')
    watering_type = SubtypeOfTool(name='Watering')
    garden_forks_type = SubtypeOfTool(name='Garden forks')
    pots_type = SubtypeOfTool(name='Pots')

    # Create test Tool objects in Catalog
    category.add_type_of_tool(hand_tools_type)
    category.add_type_of_tool(garden_tools_type)
    category.add_type_of_tool(kitchen_tools_type)
    hand_tools_type.add_subtype(drills_type)
    hand_tools_type.add_subtype(saws_type)
    hand_tools_type.add_subtype(hammers_type)
    garden_tools_type.add_subtype(watering_type)
    garden_tools_type.add_subtype(garden_forks_type)
    garden_tools_type.add_subtype(pots_type)
    # Create tools
    drill_1 = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    drill_2 = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    drills_type.add_tool(drill_1)
    drills_type.add_tool(drill_2)

    t = time.perf_counter()
    print(category.search_by_category('d'))
    print(f'time used : {(time.perf_counter() - t)*(10*6):.5f} us')