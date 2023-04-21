import tkinter as tk
import requests 
import json

# create main window
root = tk.Tk()
root.title("Add Coupon")
root.geometry("300x300")

# create form labels and entries
code_label = tk.Label(root, text="Code:")
code_label.pack()
code_entry = tk.Entry(root)
code_entry.pack(pady=5)

discount_label = tk.Label(root, text="Discount Value:")
discount_label.pack()
discount_value = tk.Entry(root)
discount_value.pack(pady=5)

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# create submit button function 
def submit():
    discount = discount_value.get() 
    name = name_entry.get()
    code = code_entry.get()
    add_coupon = {code:{"discount_value":discount,"name":name}} 
    r =  requests.post("http://127.0.0.1:8000/coupons/all", data=json.dumps(add_coupon))
    print(r.json())
    code_entry.delete(0, tk.END)
    discount_value.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    code_entry.focus()

# create submit button

submit_button = tk.Button(root, text="Submit", command=submit, font=("Arial", 12), bg="#4caf50", fg="#fff")
submit_button.pack(pady=20)

# focus the code entry field on startup
# code_entry.focus()

# run main loop
root.mainloop()
