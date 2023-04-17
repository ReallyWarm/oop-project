import sys
sys.path.append('./class_object/')
from fastapi import FastAPI
from system import System
from customerinfo import CustomerInfo

app = FastAPI()
Sys = System()

def make_customerlist(Sys:System):
    customer = dict()
    for member in Sys.get_customerinfo:
        customer = {"first_name": member.first_name,"last_name": member.last_name,"email": member.email,"company": member.company}
        return customer
    

@app.post('/customer/{first_name}/')
async def create_customer(first_name:str, last_name:str, email:str, company_name:str) ->dict:
    new_customer = CustomerInfo(first_name, last_name, email, company_name)
    Sys.add_customerInfo(new_customer)
    return {"first_name":first_name, "last_name":last_name,"email":email, "company_name":company_name}

@app.post('/customer/address/{name}/')
async def create_address(name:str, company:str, country:str, state:str,
                 city:str, address:str, phone_number:str, postal_code:str)->dict:
    for i in make_customerlist(Sys):
        if i["first_name"] == name:
            i.create_address(name,company, country, state, city, address, phone_number,postal_code)
            
            return {"data":"You have create the address successfully."}
        
        return{"data":"Unable to create the address."}
            
@app.get('/customer/address/{address}',tags=['address'])   
async def get_address(name:str)->dict:
    for i in make_customerlist(name):
        if i["first_name"] == name:
            return {"data": i.get_address(name)}
        
        return {"data": "Not found this address."}
          
    
# not finished have not done the test all the features yet I will do it continue. 