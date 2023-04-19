import tkinter as tk
import requests 
import json
# create main window
root = tk.Tk()
r = requests.get("http://127.0.0.1:8000/coupons/all") 
dict = r.json() 
print(r.json())
for key in r.json(): 
    label = tk.Label(root, text= f"{key} : {dict[key]}")
    label.pack()

# run main loop
root.mainloop()