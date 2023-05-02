from fastapi import FastAPI,Form,Request
import sys
sys.path.append('./class_object/')
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials
from system import System
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from customerinfo import CustomerInfo
from app_database import add_database_users, add_database_system, add_database_userdata


app = FastAPI()
system = System()
add_database_users(system)
add_database_system(system)
add_database_userdata(system)

def object_to_dict(object):
    return object.__dict__

# CATEGORY
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

# SEARCH
@app.get("/system/category/")
async def search_category(search:str=''):
    return system.category.search_by_category(search)

@app.get("/system/category/subtype/")
async def search_category(search:str=''):
    return system.category.search_by_subtype(search)

@app.get("/system/category/subtype/tools/")
async def search_category(search:str=''):
    return system.category.search_by_name(search)

# MANAGE TOOL
@app.get("/system/category/show_tools/", tags = ['Manage Tool'])
async def get_tool(tool_name:str):
    for name, tool in system.category.search_by_name('').items():
        if str(name) == tool_name:
            return {'tool code':tool.code,
                    'tool name':tool.name,
                    'tool description':tool.description,
                    'tool brand':tool.brand,
                    'tool amount':tool.amount,
                    'tool image':tool.image,
                    'tool price':tool.price,
                    'tool wholesale':tool.wholesales,
                    'tool reviews':tool.review_list,
                    'tool rating' : tool.rating,
                    'tool category':tool.type_of_tool,
                    'input': tool_name
                    }
    return {'GET Tool':'Invalid Tool'}

@app.post("/system/category/subtype/tools/", tags = ['Manage Tool'])
async def add_tool(tool_data:dict):
    for name, tool in system.category.search_by_name('').items():
        if tool_data["tool_name"] == name:
            return {'ADD Tool':"Already have this Tool"}
    system.create_tool(tool_data["product_code"], tool_data["tool_name"], tool_data["tool_description"], tool_data["tool_brand"],
                       tool_data["tool_amount"], tool_data["tool_image"], tool_data["tool_price"], tool_data['tool_category'])
    return {'ADD Tool':"add tool successfully"}

@app.put("/system/category/subtype/tools/", tags = ['Manage Tool'])
async def modify_tool(changing_tool_data:dict):
    print(changing_tool_data["tool_name"])
    print("------------------------------------------------------")
    for name, tool in system.category.search_by_name('').items():
        print(name)
        if name == changing_tool_data["tool_name"]:
            system.modify_tool(tool,changing_tool_data["tool_name"],
                               changing_tool_data["tool_description"],
                                changing_tool_data["tool_brand"], 
                                changing_tool_data["tool_price"],
                                changing_tool_data["product_code"], 
                                changing_tool_data['tool_category'])
            return {'MODIFY Tool':"change tool infomation successfully"}        
    return {'MODIFY Tool':'Invalid Tool'}

@app.delete("/system/category/subtype/tools/", tags = ['Manage Tool'])
async def delete_tool(deleting_tool:str):
    for name, tool in system.category.search_by_name('').items():
        if name == deleting_tool:
            system.delete_tool(tool)
            return {'DELETE Tool':"delete tool successfully"}   
    return {'DELETE Tool':'Invalid Tool'}


# MANAGE COUPON
def make_coupon_dict(system : System): 
    dict = {}
    for item in system.server_coupons :
        dict[item.code] = {"name":item.name, "discount_value":item.discount_value}
    return dict

@app.get("/coupons/all",tags = ['coupon'])
def  get_coupons() -> dict: 
    return make_coupon_dict(system)

@app.post("/coupons/used_coupon/",tags = ['coupon']) 
async def add_used_coupon(code:str): 
    current_user = system.get_login() 
    coupon = system.search_coupon(code)
    if coupon in current_user.used_coupon: 
        return {"message":"aready in used coupon"}
    current_user.store_used_coupon(coupon)
    return {"message":"add used coupon successfully"}

@app.get("/coupons/active_coupon/",tags = ['coupon'])
async def get_active_coupon(username:str): 
    dict ={}
    current_user = system.search_user(username)
    for coupon in system.server_coupons: 
        if coupon not in current_user.used_coupon: 
            dict[coupon.code]={"name": coupon.name,"discount_value": coupon.discount_value}
    return dict

@app.put("/coupons/all",tags=['coupon'])
async def update_coupons(newcoupon : dict) -> dict: 
    for key_sys in make_coupon_dict(system).keys(): 
        for key_item in newcoupon.keys(): 
            if key_item == key_sys : 
                system.modify_coupon(key_item,newcoupon[key_item]["discount_value"],newcoupon[key_item]["name"]) 
                return {"data":f"coupon at code {key_item} has been update"} 
                
    for key in newcoupon.keys():
        return {"data":f"coupon at code {key} is not found"}

@app.post("/coupons/all",tags=['coupon']) 
async def add_coupons(newcoupon : dict) -> dict:
    for key_item in newcoupon.keys(): 
        for key_sys in make_coupon_dict(system).keys(): 
            if key_item == key_sys :
                return {"data":f"coupon have already been added"}  

    for key_item in newcoupon.keys(): 
        system.add_coupon(key_item,newcoupon[key_item]["discount_value"],newcoupon[key_item]["name"])        
        return {"data":f"add new coupon with code {key_item} successfully"}

@app.delete("/coupons/all",tags=['coupon'])
async def delete_coupons(code : dict) ->dict : 
    for key in make_coupon_dict(system).keys(): 
        if key == code["code"] : 
            system.delete_coupon(key) 
            return {"data":f"coupon with code {code} have been deleted"}
    return {"data":f"delete coupon with code {code} is not found"}

# MANAGE WHOLESALE
def system_wholesale() -> dict :  
    dict = {}
    for ws in system.wholesales : 
        dict[ws.code]={"discount_value":ws.discount_value,"amount":ws.amount}
    return dict

def get_wholesale(tool : Tool) -> dict :  
    dict = {} 
    for ws in tool.wholesales : 
        dict[ws.code]={"discount_value":ws.discount_value,"amount":ws.amount}
    return dict

@app.get("/wholesale/all",tags = ['wholesale']) 
async def show_wholesale()->dict : 
    return system_wholesale()

@app.put("/wholesale/all",tags = ['wholesale']) 
async def update_wholesale(data : dict) ->dict :
    code = data["wholesale_modify"]["code"]
    for key_sys in system_wholesale().keys(): 
        if key_sys == data["wholesale_modify"]["code"] : 
                system.modify_wholesale(data["wholesale_modify"]["code"],data["wholesale_modify"]["amount"],data["wholesale_modify"]["discount_value"])
                return {"data":f"wholesale at code {code} has been update"} 
                   
    return {"data":f"wholesale at code {code} is not found"} 

@app.post("/wholesale/all",tags = ['wholesale'])  
async def add_wholesale(data: dict) -> dict:   
    code = data["wholesale_add"]["code"] 
    for key_sys in system_wholesale().keys(): 
        if key_sys == code: 
            return {"data":f"wholesale at code {code} has been update"}
    system.add_wholesale(data["wholesale_add"]["code"],data["wholesale_add"]["amount"],data["wholesale_add"]["discount_value"])
    return {"data":f"wholesale at code {code} has been update"}

@app.delete("/wholesale/all",tags = ['wholesale']) 
async def delete_wholesale(data : dict) ->dict: 
    code = data["code"]
    for code in system_wholesale() : 
        if code == data["code"]: 
            system.delete_wholesale(data["code"])
            return {"data":f"wholesale with code {code} have been deleted"} 
    return {"data":f"wholesale with code {code} is not found"}

# MANAGE CUSTOMER

#create a new address
@app.post('/customer/address/',tags=['address'])
async def create_address(newaddress:dict)->dict:
    for customer in system.customerinfos:
        if customer.username == newaddress["name"]:
            if len(customer.address) == 0:
                customer.create_address(newaddress["name"],newaddress["company"],newaddress["country"],newaddress[ "state"], newaddress["city"], newaddress["address"], newaddress["phone_number"],newaddress["postal_code"])
                return {"data":f"You have create the address successfully.You address is {customer.address}"}
            
    return{"data":"Unable to create the address."}

# #delete the address     
@app.delete('/customer/address',tags=['address'])     
async def delete_address(name:str) ->dict:
    for customer in system.customerinfos:
        if customer.username == name:
            customer.delete_address(name)
            return {"data":f"You have delete the address successfully.Your address is{customer.address}"}
    return {"data":"Unable to delete the address"}    

#get the address              
@app.get('/customer/address',tags=['address'])   
async def get_address(name:str)->dict:
  for customer in system.customerinfos:
      if customer.username == name:
          address = customer.get_address(name)
          return {"data":f'{address}'}
  return {"data":"Sorry cannot found your address in system. Please try again!"}    
      
# edit the address       
@app.put('/customer/address/',tags=['address'])
async def edit_address(address:dict) ->dict:
    for customer in system.customerinfos:
        if customer.username == address["name"]:
            customer.get_address(address["name"]).edit_address(company=address["company"],country=address["country"],state=address[ "state"], city=address["city"], address=address["address"], phone_number=address["phone_number"],postal_code=address["postal_code"])
            return {"data":f"Your edit address is successfully {customer.address}"}
    return {"data":"Unable to edit address. Please try again"}

@app.get('/customer/order',tags=['customer'])
async def check_order(name:str)->dict:
    for customer in system.customerinfos:
        if customer.username == name:
            order = customer.my_order
            return {"data":f"{order},"}
    return {"data":"Not found this order. Please try again"}    

@app.get('/customer/review',tags=['customer'])
async def check_review(name:str)->dict:
    for customer in system.customerinfos:
        if customer.username == name:
            return {"data":f"{customer.my_reviewed},"}
    return {"data":"Not found this review. Please try again"}

# make review
@app.get('/tool/review_list',tags=['review'])
async def get_reveiw(name:str) -> dict:
    for tool_name, tool in system.category.search_by_name('').items():
        if tool_name == name:
            return {"Data": tool.review_list}
    return {"data": "Not found this tool. Please try again"}


@app.get('/tool/rating',tags=['review'])
async def get_rating(name:str) -> dict:
    for tool_name, tool in system.category.search_by_name('').items():
        if tool_name == name:
            return {"Data": tool.rating}
    return {"data":"Not found this tool. Please try again"}


@app.post('/tool/make_review',tags=['review'])
async def create_review(review: dict) -> dict:
    check = 0
    check2 = 0 
    for tool_name, tool in system.category.search_by_name('').items(): 
        if tool_name == review["tool"]: 
            check = 1 
    if(check != 1): 
        return {"data": "Not found this tool. Please try again"}
    for reviewer in system.customerinfos: 
        if reviewer.first_name == review["User"]: 
            check2 = 1 
    if(check2 != 1):  
        return {"data": "Not found this tool. Please try again"}
    for tool_name, tool in system.category.search_by_name('').items():
        if tool_name == review["tool"]:
            for reviewer in system.customerinfos:
                if reviewer.first_name == review["User"]:
                    if float(review["rating"]) <= 5.00:
                        reviewer.create_review(tool, review["head_review"], review["comment"], float(review["rating"]), review["date_of_review"])
                        return {"data": "A new review is added!"}
    return {"data": "Invalid rating"}

# shopping cart
@app.post("/system/shopping_cart/", tags = ['shopping_cart'])
async def add_to_cart(chosed_item:dict):
    for name, tool in system.category.search_by_name('').items():
        if name == chosed_item['tool_name']:
            system.add_to_cart(tool,chosed_item['quantity'])
            return {'ADD TO CART':"add to cart successfully"}
    return {'ADD TO CART':"Invalid Tool"}

@app.get("/system/shopping_cart/", tags = ['shopping_cart'])
async def get_cart():
    if system.get_active_cart() != None:
        return system.get_active_cart()
    else:
        return {'GET CART':"No active cart"}

@app.delete("/system/shopping_cart/delete_cart/", tags= ['shopping_cart'])
async def clear_cart():
    if system.get_active_cart() != None:
        system.get_active_cart().clear_cart()
        return {'CLEAR CART':"clear cart successfully"}
    else:
        return {'GET CART':"No active cart"}

@app.delete("/system/shopping_cart/delete_item/", tags= ['shopping_cart'])
async def delete_item(chosed_item:dict):
    for name, tool in system.category.search_by_name('').items():
        if name == chosed_item['tool_name']:
            system.get_active_cart().delete_item(tool)
            return {'DELETE ITEM':"delete item successfully"}
    return {'DELETE ITEM':"Invalid Tool"}

# LOGIN
@app.post('/signup', summary="Create new user", response_model=dict)
async def create_user(signup_data:dict):
    # {"username":"","password":"","first_name":"","last_name":"","email":"","company_name":""}
    for _, item in signup_data.items():
        if not item:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please fill up all the forms.")
    user = system.search_user(signup_data['username'])
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exist")
    new_customer = CustomerInfo(signup_data["username"], system.auth.get_password_hash(signup_data["password"]), 
                                signup_data["first_name"], signup_data["last_name"], 
                                signup_data["email"], signup_data["company_name"])
    system.add_customerinfo(new_customer)
    return {'data':new_customer}

@app.post("/login", summary="Create access tokens for login user", response_model=dict)
async def login_for_access_token(form_data: HTTPBasicCredentials = Depends()):
    input_user = system.search_user(form_data.username)
    this_user = system.auth.authenticate_user(input_user, form_data.password)
    if not this_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password")
    
    access_token = system.auth.create_access_token(data={"sub": this_user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logout", summary="Delete access tokens", response_model=dict)
async def logout_to_invalidate_token(current_user: dict = Depends(system.get_current_user)):
    system.auth.invalidate_token()
    return {"logout":current_user.get("user")}

@app.get("/me", response_model=dict)
async def read_users_me(current_user: dict = Depends(system.get_current_user)):
    authority = 'customer'
    if system.check_admin():
        authority = 'admin'
    return {'username':current_user,'authority':authority}

@app.get("/user/",response_model=dict) 
async def get_user_first_name(username:str): 
    return {"first_name":system.search_user(username).first_name}

@app.get("/user//",response_model=dict) 
async def get_user(username:str): 
    return {"first_name":system.search_user(username)}

# PAYMENT
@app.post("/cart/payment", summary="Making payment", response_model=dict)
async def make_payment(payment_data:dict):
    current_user = system.get_login()
    status = system.make_payment(payment_data['card'], current_user, payment_data['address'], payment_data['coupon'])
    return {"status":status}

if __name__ == "__main__": 
    print(system.search_user('NorNor007').first_name)
    import uvicorn
    uvicorn.run("main:app", reload=True)
