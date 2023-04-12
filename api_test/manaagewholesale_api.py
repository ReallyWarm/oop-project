from fastapi import FastAPI
import requests
import json
#r = requests.get("http://127.0.0.1:8000/wholesale/all ")


wholesale =  {  "hammer":
            {
                "code":"099x", 
                "amount": 45,
                "discount_value": 80,
            }
}



r = requests.post("http://127.0.0.1:8000/wholesale/all", data = json.dumps(wholesale))
print(r) 

# x = requests.get("http://127.0.0.1:8000/wholesale/all")
# print(x)


