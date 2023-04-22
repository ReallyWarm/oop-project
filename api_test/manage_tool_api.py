import requests
import json
tool_info = {
	"product_code": "01x",
	"tool_name":"Testing drill",
	"tool_description": "POWER",
	"tool_brand": "idk",
	"tool_amount": "10",
	"tool_image": "None",
	"tool_price": "100.00",
	"tool_category": "Drills"
}

updating_tool = {
	
	"tool_name":"Testing drill",
	"tool_description": "POWER",
	"tool_brand": "idk",
	"tool_price": "20.00",
	"product_code": "01x",
	"tool_category": "Drills"
}

deleting_tool = "Testing drill"   

# add tool 
# r = requests.post("http://127.0.0.1:8000/system/category/tools/",data = json.dumps(tool_info))
# print(r.json()) 

# modify tool
# r = requests.put("http://127.0.0.1:8000/system/category/tools/",data=json.dumps(updating_tool)) 
# print(r.json()) 

# delete tool 
r = requests.delete("http://127.0.0.1:8000/system/category/tools/?deleting_tool=okm")
print(r.json()) 