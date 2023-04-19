import tkinter as tk
from tkinter import messagebox
import json
import requests

class ManageProfilePage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent 
        
        # create label for page title
        title_label = tk.Label(self, text="Delete the address", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # create labels and entry fields for user information
        username_label = tk.Label(self, text="Username:", font=("Arial", 12))
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)
        
  
        delete_button = tk.Button(self, text="Delete", font=("Arial", 12), command=self.delete_changes)
        delete_button.grid(row=9, column=0, columnspan=2, pady=20)
        
        
    def delete_changes(self):
        # save changes to user information
        user_info = {
            "name":self.username_entry.get()
        }
        
        r = requests.delete("http://127.0.0.1:8000/customer/address",data=json.dumps(user_info))
        res = json.loads(r.text)
        # show message box indicating changes have been saved
        if  res == {"data":"Unable to delete the address"}:
            messagebox.showinfo(title='Error',message="You don't have account in this system. Please try again")
            print(r.json())
        else:
             messagebox.showinfo(title='Notice',message="Success delete the address")
             print(r.json())
        
# create tkinter window
root = tk.Tk()

# create manage profile page
manage_profile_page = ManageProfilePage(root)

# add manage profile page to tkinter window
manage_profile_page.pack()

# start tkinter event loop
root.mainloop()