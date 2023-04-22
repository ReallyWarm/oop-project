import tkinter as tk
import requests 
import json

# create main window
root = tk.Tk()
root.title("Coupon Form")
root.geometry("400x300")
root.config(bg="#f5f5f5")

# create form labels and entries
code_label = tk.Label(root, text="Code:", bg="#f5f5f5", font=("Arial", 12))
code_label.pack(pady=10)
code_entry = tk.Entry(root, font=("Arial", 12))
code_entry.pack()

discount_label = tk.Label(root, text="Discount value:", bg="#f5f5f5", font=("Arial", 12))
discount_label.pack(pady=10)
discount_value = tk.Entry(root, font=("Arial", 12))
discount_value.pack()

name_label = tk.Label(root, text="Name:", bg="#f5f5f5", font=("Arial", 12))
name_label.pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack()

def submit():
    discount =discount_value.get() 
    name = name_entry.get()
    code = code_entry.get()
    add_coupon = {code:{"discount_value":discount,"name":name}} 
    r =  requests.put("http://127.0.0.1:8000/coupons/all",data = json.dumps(add_coupon))
    print(r.json())

# create submit button
submit_button = tk.Button(root, text="Submit", command=submit, font=("Arial", 12), bg="#4caf50", fg="#fff")
submit_button.pack(pady=20)

# create submit button function 
root.mainloop()