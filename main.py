import sys
sys.path.append('./class_object/')
import secrets
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasicCredentials, HTTPBearer, HTTPBasic
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from system import System
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from customerinfo import CustomerInfo
from app_database import add_database_users, add_database_system, add_database_userdata

app = FastAPI()
system = System()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login",scheme_name="JWT")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "608672d916b11ac31e9ac553d5418caec4052bca348f2d06d4440aaacce155b0"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

@app.get("/system/category/tools/")
async def search_category(search:str=''):
    return system.category.search_by_name(search)

# MANAGE TOOL
@app.post("/system/category/tools/")
async def add_tool(tool_data:dict):
    system.create_tool(tool_data["code"], tool_data["name"], tool_data["description"], tool_data["brand"],
                       tool_data["amount"], tool_data["image"], tool_data["price"], tool_data['type_of_tool'])
    return {'ADD Tool':tool_data["name"]}

# MANAGE COUPON
def make_coupon_dict(system : System): 
    dict = {}
    for item in system.server_coupon :
        dict[item.code] = {"name":item.name, "discount_value":item.discount_value}
    return dict

@app.get("/coupons/all",tags = ['coupon'])
async def get_coupons() -> dict:  
    return make_coupon_dict(system)
 
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
    
@app.get("/wholesale/all",tags = ['wholesale']) 
async def show_wholesale()->dict : 
    return system_wholesale()

@app.put("/wholesale/all",tags = ['wholesale']) 
async def update_wholesale(data : dict) ->dict :
    code = data["tool_modify"]["code"]
    for key_sys in system_wholesale().keys(): 
        if key_sys == data["tool_modify"]["code"] : 
                system.modify_wholesale(data["tool_modify"]["code"],data["tool_modify"]["amount"],data["tool_modify"]["discount_value"])
                return {"data":f"wholesale at code {code} has been update"} 
                   
    return {"data":f"wholesale at code {code} is not found"} 

@app.post("/wholesale/all",tags = ['wholesale'])  
async def add_wholesale(data: dict) -> dict:   
    pass

@app.delete("/wholesale/all",tags = ['wholesale']) 
async def delete_wholesale(data : dict) ->dict: 
    code = data["code"]
    for code in system_wholesale() : 
        if code == data["code"]: 
            system.delete_wholesale(data["code"])
            return {"data":f"wholesale with code {code} have been deleted"} 
    return {"data":f"wholesale with code {code} is not found"}

# MANAGE CUSTOMER
#create a new customer
@app.post('/customer/{first_name}/')
async def create_customer(customer:dict)->dict:
    new_customer = CustomerInfo(customer["first_name"], customer["last_name"], customer["email"],customer["company_name"])
    system.add_customerinfo(new_customer)
    return {'data':new_customer}

#create a new address
@app.post('/customer/address/{name}/')
async def create_address(newaddress:dict)->dict:
    for customer in system.customerinfos:
        if customer.first_name == newaddress["name"]:
            customer.create_address(newaddress["name"],newaddress["company"],newaddress["country"],newaddress[ "state"], newaddress["city"], newaddress["address"], newaddress["phone_number"],newaddress["postal_code"])
            return {"data":"You have create the address successfully."}
            
    return{"data":"Unable to create the address."}

# #delete the address     
@app.delete('/cusrtomer/address/{name}',tags=['address'])     
async def delete_address(data:dict) ->dict:
    for customer in system.customerinfos:
        if customer.first_name == data["name"]:
            customer.delete_address(data["name"])
            return {"data":"You have delete the address successfully"}
    return {"data":"Unable to delete the address"}    

#get the address              
@app.get('/customer/address/{address}',tags=['address'])   
async def get_address(name:str)->dict:
  for customer in system.customerinfos:
      if customer.first_name == name:
          address = customer.get_address(name)
          return {"data":f'Your address  {address}'}
  return {"data":"Sorry cannot found your address in system. Please try again!"}    
      
# edit the address       
@app.put('/customer/address/')
async def edit_address(address:dict) ->dict:
    for customer in system.customerinfos:
        if customer.first_name == address["name"]:
            customer.get_address(address["name"]).edit_address(company=address["company"],country=address["country"],state=address[ "state"], city=address["city"], address=address["address"], phone_number=address["phone_number"],postal_code=address["postal_code"])
            return {"data":f"Your edit address is successfully {customer.address}"}
    return {"data":"Unable to edit address. Please try again"}

@app.get('/customer/order{name}')
async def check_order(name:str)->dict:
    for customer in system.customerinfos:
        if customer.first_name == name:
            order = customer.my_order
            return {"data":f"Your order is {order}"}
    return {"data":"Not found this order. Please try again"}    

@app.get('/customer/review{name}')
async def check_review(name:str)->dict:
    for customer in system.customerinfos:
        if customer.first_name == name:
            return {"data":f"Your review is {customer.my_reviewed}"}
    return {"data":"Not found this review. Please try again"}

# LOGIN

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str):
    return system.search_user(username)
    
def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# def get_current_user(credentials: HTTPBasicCredentials = Depends(HTTPBearer())):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     token = credentials.credentials

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         if payload is None:
#             raise credentials_exception
#         return credentials
#     except JWTError:
#         raise credentials_exception

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_username = username
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_username)
    if user is None:
        raise credentials_exception
    return object_to_dict(user)

@app.post('/signup', summary="Create new user", response_model=dict)
async def create_user(signup_data:dict):
    # {"username":"","password":"","first_name":"","last_name":"","email":"","company_name":""}
    user = system.search_user(signup_data['username'])
    if user is not None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this username already exist")
    new_customer = CustomerInfo(signup_data["username"], get_password_hash(signup_data["password"]), 
                                signup_data["first_name"], signup_data["last_name"], 
                                signup_data["email"], signup_data["company_name"])
    system.add_customerinfo(new_customer)
    return {'data':new_customer}

@app.post("/login", summary="Create access tokens for login user", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me", response_model=dict)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user
