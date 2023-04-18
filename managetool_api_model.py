import sys
import json
sys.path.append('./class_object/')
from category import *
from tool import Tool
from fastapi import FastAPI
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

app = FastAPI()

@app.get("/select subtype to add_tool", tags=['manage_tool'])
async def search_subtype(searching:str):
    return {"Data": category.search_by_category(searching)}

@app.get("/show tool in selected subtype", tags=['manage_tool'])
async def show_tool(searching_byname:str):
    return {"Data": category.search_by_name(searching_byname)}

@app.post("/create and add tool to category", tags=['manage_tool'])
async def add_tool(tool_info: dict):
    selected_subtype = tool_info["tool_category"]
    selected_subtype_list = category.search_by_category(selected_subtype)
    if selected_subtype_list != None:
        print(selected_subtype_list[selected_subtype])
        system.create_tool(tool_info["product_code"],tool_info["tool_name"],tool_info["tool_description"],tool_info["tool_brand"],tool_info["tool_amount"],tool_info["tool_image"],tool_info["tool_price"],selected_subtype_list[selected_subtype])
        print(selected_subtype_list[selected_subtype])
        print(category.search_by_name(""))
        return {"Data": "adding tool success"}
    else:
        return {"Data": "selected subtype not found"}