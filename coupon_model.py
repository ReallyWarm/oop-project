from fastapi import FastAPI 
import sys
sys.path.append('./class_object/')
from discount import Coupon
from system import System 
from admin import Admin 
app = FastAPI()
system = System()
namning = Admin("Admin","1234","Pithakpong","Sawongnam","pithakpong0862@gmail.com")
def make_coupon_dict(system : System): 
    dict = {}
    for item in system.server_coupon :
        dict[item.code] = {"name":item.name, "discount_value":item.discount_value}
    return dict
@app.get("/coupons/all",tags = ['coupon'])
async def get_coupons() -> dict:  
# def get_coupons() -> dict: 
    return make_coupon_dict(system)
 
@app.put("/coupons/all",tags=['coupon'])
async def update_coupons(newcoupon : dict) -> dict: 
# def put_coupons(newcoupon : dict) -> dict:
    for key_sys in make_coupon_dict(system).keys(): 
        for key_item in newcoupon.keys(): 
            if key_item == key_sys : 
                system.modify_coupon(key_item,newcoupon[key_item]["discount_value"],newcoupon[key_item]["name"]) 
                return {"data":f"coupon at code {key_item} has been update"}
    for key in newcoupon.keys():
        return {"data":f"coupon at code {key} is not found"}

@app.post("/coupons/all",tags=['coupon']) 
async def add_coupons(newcoupon : dict) -> dict:
# def post_coupons(newcoupon : dict) -> dict:
    for key_item in newcoupon.keys(): 
        for key_sys in make_coupon_dict(system).keys(): 
            if key_item == key_sys :
                return {"data":f"coupon have already been added"} 
    for key_item in newcoupon.keys(): 
        system.add_coupon(key_item,newcoupon[key_item]["discount_value"],newcoupon[key_item]["name"])        
        return {"data":f"add new coupon with code {key_item} successfully"}

@app.delete("/coupons/all",tags=['coupon'])
async def delete_coupons(code : dict) ->dict : 
# def delete_coupons(code : str) -> dict:
    for key in make_coupon_dict(system).keys(): 
        if key == code["code"] : 
            system.delete_coupon(key)
            return {"data":f"coupon with code {code} have been deleted"}
    return {"data":f"delete coupon with code {code} is not found"}