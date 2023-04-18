import requests
import json

input_customer = {"first_name": "John", "last_name": "wick","email": "john@gmail.com","company_name": "continental"}

input_address = {"name": "John", "company": "continental","country": "United States","state": "Los Angeles",
                 "city": "Los Angeles","address":"-","phone_number":"-","postal_code":"-"}

edit_address ={"name": "John", "company": "continental","country": "Thailand","state": "-",
                 "city": "Bangkok","address":"-","phone_number":"-","postal_code":"-"}

delete_address ={"name": "John"}



#add customer
r= requests.post("http://127.0.0.1:8000/customer/{first_name}",data=json.dumps(input_customer))
print(r.json())

#create address
r= requests.post("http://127.0.0.1:8000/customer/address/{name}",data=json.dumps(input_address))
print(r.json())

#delete address
r= requests.delete("http://127.0.0.1:8000/customer/address/{name}",data=json.dumps(delete_address))
print(r.json())

#get address
r = requests.get("http://127.0.0.1:8000/customer/address/{address}?name=John")
print(r.json())

#edit address
r = requests.put("http://127.0.0.1:8000/customer/address{address}",data=json.dumps(edit_address))
print(r.json())

#check review
r = requests.get("http://127.0.0.1:8000/customer/reviewPrakrittipon")
print(r.json())

r = requests.get("http://127.0.0.1:8000/customer/orderNorNor")
print(r.json())