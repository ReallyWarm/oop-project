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
    



def all_wholesale(tool : Tool) -> dict :  
    dict = {}
    for ws in tool.wholesales : 
        dict[ws.code]={"discount_value":ws.discount_value,"amount":ws.amount}
    return dict
    
@app.get("/wholesale/all",tags = ['wholesale']) 
async def show_wholesale()->dict : 
# def show_wholesale()->dict :
    return all_wholesale(testing)

@app.put("/wholesale/all",tags = ['wholesale']) 
async def update_wholesale(data : dict) ->dict :
# def update_wholesale(data : dict) ->dict :
    code = data["tool_modify"]["code"]
    for key_sys in all_wholesale(testing).keys(): 
        if key_sys == data["tool_modify"]["code"] : 
                system.modify_wholesale(data["tool_modify"]["code"],data["tool_modify"]["amount"],data["tool_modify"]["discount_value"])
                return {"data":f"wholesale at code {code} has been update"} 
                   
    return {"data":f"wholesale at code {code} is not found"} 

@app.post("/wholesale/all",tags = ['wholesale'])  
async def add_wholesale(data: dict) -> dict:  
# def add_wholesale(data: dict) -> dict:  
    for key_sys in all_wholesale(testing).keys(): 
        if key_sys == data["tool_modify"]["code"] : 
                return {"data" : f"wholesale have already in dict"}
    for wholesale in system.wholesales : 
        if data["tool_modify"]["code"] == wholesale.code :    
            testing.add_wholesale(system.search_wholesale(wholesale.code))
            return {"data" : f"add new wholesale with code {wholesale.code} successfully"}
    code =  data["tool_modify"]["code"]
    system.add_wholesale(data["tool_modify"]["code"],data["tool_modify"]["amount"],data["tool_modify"]["discount_value"])
    added_wholesale = system.search_wholesale(data["tool_modify"]["code"])
    testing.add_wholesale(added_wholesale)
    return {"data" : f"add new wholesale with code  {code}  successfully"}

@app.delete("/wholesale/all",tags = ['wholesale']) 
async def delete_wholesale(data : dict) ->dict: 
# def delete_wholesale(data : dict) ->dict: 
    code = data["code"]
    for code in all_wholesale(testing) : 
        if code == data["code"]: 
            system.delete_wholesale(data["code"])
            return {"data":f"wholesale with code {code} have been deleted"} 
    return {"data":f"wholesale with code {code} is not found"}
