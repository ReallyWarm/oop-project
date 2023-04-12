from fastapi import FastAPI 
import sys
sys.path.append('./class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from admin import Admin 
app = FastAPI()
system = System()
namning = Admin("Admin","1234","Pithakpong","Sawongnam","pithakpong0862@gmail.com")
coupons_dicts = {}

@app.get("/coupons/all",tags = ['coupon'])
async def get_coupons() -> dict: 
    return coupons_dicts
 
@app.put("/coupons/all",tags=['coupon'])
async def update_coupons(code : str,name : str,discount_value : int) -> dict: 
    for key in coupons_dicts.keys(): 
        if key == code : 
            coupons_dicts[key]["name"] = name 
            coupons_dicts[key]["discount_value"] = discount_value
            return {"data":f"coupon at code {code} has been update"}
    return {"data":f"coupon at code {code} is not found"}

@app.post("/coupons/all",tags=['coupon']) 
async def add_coupons(code : str,name : str,discount_value :int) -> dict:
    for key in coupons_dicts.keys(): 
        if key == code : 
            return {"data":f"coupon have already been added"} 
       
    coupons_dicts[code]= { 
        "name":name,
        "discount_value":discount_value
    }
    return {"data":f"add new coupon with code {code} successfully"}

@app.delete("/coupons/all",tags=['coupon'])
async def delete_coupons(code : str) ->dict : 
    for key in coupons_dicts.keys(): 
        if key == code : 
            coupons_dicts.pop(key)
            return {"data":f"coupon with code {code} have been deleted"}
    return {"data":f"delete coupon with code {code} is not found"}
