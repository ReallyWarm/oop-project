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
    saw_1 = Tool('01x', 'Testing saw', 'da-da', 'idk', 10, None, 700.00, 'Saws')
    saw_2 = Tool('02x', 'see saw', 'da-da', 'idk', 12, None, 1000.00, 'Saws')
    hammer_1 = Tool('01x', 'Testing hammer', 'bang bang', 'idk', 10, None, 200.00, 'Hammers')
    hammer_2 = Tool('02x', 'toob hammer', 'bang bang', 'idk', 12, None, 100.00, 'Hammers')
    watering_1 = Tool('01x', 'Testing watering can', 'WET', 'idk', 10, None, 50.00, 'Waterings')
    watering_2 = Tool('02x', 'Shower watering', 'WET', 'idk', 12, None, 100.00, 'Waterings')
    drills_type.add_tool(drill_1)
    drills_type.add_tool(drill_2)
    saws_type.add_tool(saw_1)
    saws_type.add_tool(saw_2)
    hammers_type.add_tool(hammer_1)
    hammers_type.add_tool(hammer_2)
    watering_type.add_tool(watering_1)
    watering_type.add_tool(watering_2)

    print(category._all_types)

    t = time.perf_counter()
    print(category.search_by_category('d'))
    print(f'time used : {(time.perf_counter() - t)*(10*6):.5f} us')

    print(category._all_tools)

    t = time.perf_counter()
    print(category.search_by_name('t'))
    print(f'time used : {(time.perf_counter() - t)*(10*6):.5f} us')