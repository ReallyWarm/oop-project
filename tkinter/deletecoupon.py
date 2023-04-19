import tkinter as tk
import requests 
import json

# create main window
root = tk.Tk()
root.geometry("400x300")
root.title("Coupon Deletion Form")

# create form labels and entries
code_label = tk.Label(root, text="Code:", font=("Arial", 14))
code_label.pack(pady=10)
code_entry = tk.Entry(root, font=("Arial", 14))
code_entry.pack()

# create submit button function 
def submit():
    code = code_entry.get()
    add_coupon = {"code":code} 
    r =  requests.delete("http://127.0.0.1:8000/coupons/all",data = json.dumps(add_coupon))
    print(r.json())

# create submit button
submit_button = tk.Button(root, text="Delete Coupon", font=("Arial", 14), command=submit)
submit_button.pack(pady=20)

# run main loop
root.mainloop()


