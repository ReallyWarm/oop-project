from fastapi import FastAPI
import requests
import json
import sys
sys.path.append('./class_object/')
app = FastAPI()
from category import TypeOfTool, SubtypeOfTool
from wishlish import Wishlist
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System  
from admin import Admin 
from discount import Wholesale
system = System()
category = system.category
hand_tools_type = TypeOfTool(name='Hand tools')
drills_type = SubtypeOfTool(name='Drills')
nothing = SubtypeOfTool(name='None')

category.add_type(hand_tools_type)
category.type_add_subtype(hand_tools_type, drills_type)
category.type_add_subtype(hand_tools_type, nothing)
test_drill = Tool('01x', 'Testingdrill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
category.subtype_add_tool(drills_type, test_drill)
    #print(test_drill)

admin = Admin("admin","1234","Kelvin","Lim","admin@gmail.com")  
    # add wholesale
system.add_wholesale("03x",5,20) 
system.add_wholesale("05x",10,12)
    # search tool
search = category.search_by_name('')
testing = search['Testingdrill']
    # add wholesale to tools
wholesale = system.search_wholesale("03x")
testing.add_wholesale(wholesale)
wholesale = system.search_wholesale("05x") 
testing.add_wholesale(wholesale)
    



def all_wholesale(tool) -> dict :  
    for ws in tool.wholesales : 
        dict ={}
        dict["code"] = ws.code 
        dict["amount"] = ws.amount
        dict["discount_value"] = ws.discount_value 
    return {tool.name:dict},tool.name
    
DICT,name = all_wholesale(testing)
print(DICT)

@app.get("/wholesale/all",tags = ['wholesale'])
async def show_wholesale()->dict :
    return DICT

@app.put("/wholesale/all",tags = ['wholesale']) 
async def update_wholesale(code : str,amount : int, discount_value : int) ->dict :
    for key in DICT.keys(): 
        if DICT[key]["code"] == code : 
            DICT[key]["amount"] = amount 
            DICT[key]["discount_value"] = discount_value
            return {"data":f"wholesale at code {code} has been update"} 
    return {"data":f"wholesale at code {code} is not found"} 

@app.post("/wholesale/all",tags = ['wholesale'])  
async def add_wholesale(name : str,code : str,amount : int,discount_value : int): 
    value = {} 
    value["code"] = code 
    value["amount"] = amount
    value["discount_value"] = discount_value
    for key in DICT.keys(): 
        if DICT[key]["code"] == code :
            return {"data" : f"wholesale have already in dict"}
    DICT[name] = value
    return {"data" : f"add new wholesale with code {code} successfully"}

@app.delete("/wholesale/all",tags = ['wholesale']) 
async def delete_wholesale(code : str) ->dict: 
    for key in DICT.keys(): 
        if DICT[key]["code"] == code : 
            DICT.pop(key)
            return {"data":f"wholesale with code {code} have been deleted"}
    return {"data":f"wholesale with code {code} is not found"}

