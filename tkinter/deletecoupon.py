import tkinter as tk
import requests 
import json
# create main window
root = tk.Tk()

# create form labels and entries
code_label = tk.Label(root, text="Code:")
code_label.pack()
code_entry = tk.Entry(root)
code_entry.pack()

def submit():
    code = code_entry.get()
    add_coupon = {"code":code} 
    r =  requests.delete("http://127.0.0.1:8000/coupons/all",data = json.dumps(add_coupon))
    print(r.json())
# create submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()
# create submit button function 
root.mainloop()


