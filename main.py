import sys
sys.path.append('./class_object/')
from fastapi import FastAPI
from system import System
from category import TypeOfTool, SubtypeOfTool
from tool import Tool

app = FastAPI()
system = System()

@app.post("/system/category/typeoftools/")
async def add_typeoftool(type_data:dict):
    new_typeoftool = TypeOfTool(type_data['name'])
    system.category.add_type(new_typeoftool)
    return {"ADD TypeOfTool": new_typeoftool}

@app.post("/system/category/subtypeoftools/")
async def add_subtypeoftool(subtype_data:dict):
    new_subtypeoftool = SubtypeOfTool(subtype_data['name'])
    system.category.type_name_add_subtype(subtype_data['type'], new_subtypeoftool)
    return {'ADD SubtypeOfTool':new_subtypeoftool}

@app.post("/system/category/tools/")
async def add_tool(tool_data:dict):
    new_tool = Tool(tool_data['code'], tool_data['name'], tool_data['description'], tool_data['brand'], 
                    tool_data['amount'], tool_data['image'], tool_data['price'], tool_data['type_of_tool'])
    system.category.subtype_name_add_tool(tool_data['type_of_tool'], new_tool)
    return {'ADD Tool':new_tool}

@app.get("/system/category/")
async def search_category(search:str=''):
    return system.category.search_by_category(search)

@app.get("/system/category/tools/")
async def search_category(search:str=''):
    return system.category.search_by_name(search)