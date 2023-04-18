import sys
sys.path.append('./class_object/')
from fastapi import FastAPI
from system import System
from customerinfo import CustomerInfo
from order import Order
from tool import Tool

app = FastAPI()
Sys = System()

#System customer information object (database)
customer = [ CustomerInfo('NorNor', 'Sawongnam', 'NorNor@gmail.com', 'Kmitl'), 
                CustomerInfo('พรี่โอมใจเกเร', 'สองศรี', 'Thanasak@gmail.com', 'Kmitl'),
                CustomerInfo("Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")]

for i in range(len(customer)):
     Sys.add_customerinfo(customer[i])

#System addresses  (database) 
customer[0].create_address('NorNor','จารย์แดง จำกัด','Thailand','Udon Thani','-','-','0210567473','10010')
customer[1].create_address('พรี่โอมใจเกเร','ใจเกเร จำกัด','Thailand','Udon Thani','-','-','0810567473','10010')
customer[2].create_address('Prakrittipon','KMIL','Thailand','Bangkok','Pha ya tai','sol.12 24/89','0901276842','11120')   

order1 = Order([], '34000', 'NorNor', 'Success', '12.00')
order2 = Order(['test_drill','น็อต'], '12000', 'พรี่โอมใจเกเร', 'Success', '150.00')
customer[0].store_order(order1)
customer[1].store_order(order2)
test_drill = Tool('01x', 'Testing drill', 'POWER',
                      'idk', 10, None, 1000.00, 'Drills')
customer[2].create_review(test_drill, "test_review1", "good_tool", 4.5, "4/1/2023")   

#create a new customer
@app.post('/customer/{first_name}/')
async def create_customer(customer:dict)->dict:
    new_customer = CustomerInfo(customer["first_name"], customer["last_name"], customer["email"],customer["company_name"])
    Sys.add_customerinfo(new_customer)
    return {'data':new_customer}

#create a new address
@app.post('/customer/address/{name}/')
async def create_address(newaddress:dict)->dict:
    for customer in Sys.customerinfo:
        if customer.first_name == newaddress["name"]:
            customer.create_address(newaddress["name"],newaddress["company"],newaddress["country"],newaddress[ "state"], newaddress["city"], newaddress["address"], newaddress["phone_number"],newaddress["postal_code"])
            return {"data":"You have create the address successfully."}
            
    return{"data":"Unable to create the address."}

# #delete the address     
@app.delete('/cusrtomer/address/{name}',tags=['address'])     
async def delete_address(data:dict) ->dict:
    for customer in Sys.customerinfo:
        if customer.first_name == data["name"]:
            customer.delete_address(data["name"])
            return {"data":"You have delete the address successfully"}
    return {"data":"Unable to delete the address"}    

#get the address              
@app.get('/customer/address/{address}',tags=['address'])   
async def get_address(name:str)->dict:
  for customer in Sys.customerinfo:
      if customer.first_name == name:
          address = customer.get_address(name)
          return {"data":f'Your address  {address}'}
  return {"data":"Sorry cannot found your address in system. Please try again!"}    
      
# edit the address       
@app.put('/customer/address/')
async def edit_address(address:dict) ->dict:
    for customer in Sys.customerinfo:
        if customer.first_name == address["name"]:
            customer.get_address(address["name"]).edit_address(company=address["company"],country=address["country"],state=address[ "state"], city=address["city"], address=address["address"], phone_number=address["phone_number"],postal_code=address["postal_code"])
            return {"data":f"Your edit address is successfully {customer.address}"}
    return {"data":"Unable to edit address. Please try again"}

@app.get('/customer/order{name}')
async def check_order(name:str)->dict:
    for customer in Sys.customerinfo:
        if customer.first_name == name:
            order = customer.my_order
            return {"data":f"Your order is {order}"}
    return {"data":"Not found this order. Please try again"}    

@app.get('/customer/review{name}')
async def check_review(name:str)->dict:
    for customer in Sys.customerinfo:
        if customer.first_name == name:
            return {"data":f"Your review is {customer.my_reviewed}"}
    return {"data":"Not found this review. Please try again"}
