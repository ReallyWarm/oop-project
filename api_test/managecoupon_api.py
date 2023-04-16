import requests 
import json 
newcoupon = {"12x":{"discount_value":15,"name":"wow"}}
coupon_modify = {"12x":{"discount_value":20,"name":"Ha Ha"}}
code_delete = {"code":"12x"}
# get coupon  
r = requests.get("http://127.0.0.1:8000/coupons/all")  
print(r.json()) 

# add coupon
r = requests.post("http://127.0.0.1:8000/coupons/all",data = json.dumps(newcoupon))
print(r.json()) 

r = requests.get("http://127.0.0.1:8000/coupons/all")  
print(r.json()) 

# modify coupon
r = requests.put("http://127.0.0.1:8000/coupons/all",data = json.dumps(coupon_modify))
print(r.json()) 
r = requests.get("http://127.0.0.1:8000/coupons/all")  
print(r.json()) 

#delete coupon 
r = requests.delete("http://127.0.0.1:8000/coupons/all",data = json.dumps(code_delete))
print(r.json()) 
r = requests.get("http://127.0.0.1:8000/coupons/all")  
print(r.json()) 