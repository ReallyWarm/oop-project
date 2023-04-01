import sys
sys.path.append('./class_object/')
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
    category.add_type(hand_tools_type)
    category.add_type(garden_tools_type)
    category.add_type(kitchen_tools_type)
    category.type_add_subtype(hand_tools_type, drills_type)
    category.type_add_subtype(hand_tools_type, saws_type)
    category.type_add_subtype(hand_tools_type, hammers_type)
    category.type_add_subtype(garden_tools_type, watering_type)
    category.type_add_subtype(garden_tools_type, garden_forks_type)
    category.type_add_subtype(garden_tools_type, pots_type)

    # Create tools
    drill_1 = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    drill_2 = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    saw_1 = Tool('01x', 'Testing saw', 'da-da', 'idk', 10, None, 700.00, 'Saws')
    saw_2 = Tool('02x', 'see saw', 'da-da', 'idk', 12, None, 1000.00, 'Saws')
    hammer_1 = Tool('01x', 'Testing hammer', 'bang bang', 'idk', 10, None, 200.00, 'Hammers')
    hammer_2 = Tool('02x', 'toob hammer', 'bang bang', 'idk', 12, None, 100.00, 'Hammers')
    watering_1 = Tool('01x', 'Testing watering can', 'WET', 'idk', 10, None, 50.00, 'Waterings')
    watering_2 = Tool('02x', 'Shower watering', 'WET', 'idk', 12, None, 100.00, 'Waterings')
    category.subtype_add_tool(drills_type, drill_1)
    category.subtype_add_tool(drills_type, drill_2)
    category.subtype_add_tool(saws_type, saw_1)
    category.subtype_add_tool(saws_type, saw_2)
    category.subtype_add_tool(hammers_type, hammer_1)
    category.subtype_add_tool(hammers_type, hammer_2)
    category.subtype_add_tool(watering_type, watering_1)
    category.subtype_add_tool(watering_type, watering_2)

    print(category)
    print(category.types_of_tool)

    t = time.perf_counter()
    print(category.search_by_category('d'))
    print(f'time used : {(time.perf_counter() - t)*(10*6):.5f} us')

    print(category.get_subtypes_list(hand_tools_type))

    t = time.perf_counter()
    print(category.search_by_name('t'))
    print(f'time used : {(time.perf_counter() - t)*(10*6):.5f} us')