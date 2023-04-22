import requests
import json

input_review = {
	"User":"NorNor",
	"tool":"Testing drill",
	"head_review":"review1",
	"comment":"good",
	"rating":"4",
	"date_of_review":"4/18/2023" 
}

input_tool = 'Testing drill'

#make review
r= requests.post("http://127.0.0.1:8000/tool/make_review",data=json.dumps(input_review))
print(r.json())

#get rating
r = requests.get("http://127.0.0.1:8000/tool/rating?name=Testing%20drill")
print(r.json())

#get review
r = requests.get("http://127.0.0.1:8000/tool/review_list?name=Testing%20drill")
print(r.json())

