import requests,json 
r = requests.get('http://127.0.0.1:8000/me')
print(r.json())