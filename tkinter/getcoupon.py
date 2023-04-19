import tkinter as tk
import requests 
import json

# create main window
root = tk.Tk()
root.title("Coupon Data")
root.geometry("400x400")

# create header label
header_label = tk.Label(root, text="Coupon Data", font=("Arial", 16, "bold"))
header_label.pack(pady=10)

# make request to API
r = requests.get("http://127.0.0.1:8000/coupons/all") 
data = r.json() 

# create label for each data item
for key in data: 
    label = tk.Label(root, text= f"{key} : {data[key]}", font=("Arial", 7))
    label.pack(pady=5)

# run main loop
root.mainloop()