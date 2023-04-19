import requests
import json
input = {"wholesale_add":{"code":"12x","amount":12,"discount_value":68}}
update = {"wholesale_modify":{"code":"12x","amount":54,"discount_value":18}}
delete = {"code":"12x"}   

# get wholesale
r = requests.get("http://127.0.0.1:8000/wholesale/all") 
print(r.json())  

# # add wholesale 
r = requests.post("http://127.0.0.1:8000/wholesale/all",data = json.dumps(input))
r = requests.get("http://127.0.0.1:8000/wholesale/all") 
print(r.json()) 

#update wholesale
r = requests.put("http://127.0.0.1:8000/wholesale/all",data=json.dumps(update)) 
r = requests.get("http://127.0.0.1:8000/wholesale/all") 
print(r.json()) 

# delete wholesale 
r = requests.delete("http://127.0.0.1:8000/wholesale/all",data = json.dumps(delete))
r = requests.get("http://127.0.0.1:8000/wholesale/all") 
print(r.json()) 