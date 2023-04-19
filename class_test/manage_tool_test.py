import sys
sys.path.append('./class_object/')
from category import Category, TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System

system = System()
category = system.category
hand_tools_type = TypeOfTool(name='Hand tools')
drills_type = SubtypeOfTool(name='Drills')
nothing = SubtypeOfTool(name='None')

# Create test Tool objects in Catalog
category.add_type(hand_tools_type)
category.type_add_subtype(hand_tools_type, drills_type)
category.type_add_subtype(hand_tools_type, nothing)
test_drill = Tool('01x', 'testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
faifa_drill = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
sawaan = Tool('03x', 'sawaan', 'go to hell', 'HEAVEN', 15, None, 2000.00, 'Drills')
category.subtype_add_tool(drills_type, test_drill)
category.subtype_add_tool(drills_type, faifa_drill)
category.subtype_add_tool(drills_type, sawaan)

#add tool *****done******
print(category.search_by_category("d"))
selected_category = input("type cetegory: ")
a = category.search_by_category(selected_category)
system.create_tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, a[selected_category])
print(category)
print(hand_tools_type)
print(drills_type)

#modify tool *****done*****
print(category.search_by_name("t"))
modifing_tool = input("type tool name: ")
b = category.search_by_name(modifing_tool)
obj_tool = b[modifing_tool]
print(category._all_subtypes)
print(obj_tool)
system.modify_tool(obj_tool, name='new name', description='new description', brand='new brand', price= 200, code='x0.23', type_of_tool='None')
print(obj_tool)


# delete tool ******done******
print(drills_type)
print(category.search_by_name("drill"))
deleting_tool = input("tool name: ")
d = category.search_by_name(deleting_tool)
system.delete_tool(d[deleting_tool])
print("---------------------------------------------------------------------------")
print(drills_type)

