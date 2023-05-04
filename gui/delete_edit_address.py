import tkinter as tk
from tkinter import messagebox
import json
import requests


class EditDeleteAddressGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.address_info = self.user_address_info_data() # get customer address in customerinfo
        self.address_name = self.user_address_name()
        self.address_company = self.user_address_company()
        self.address_country = self.user_address_country()
        self.address_state = self.user_address_state()
        self.address = self.user_address()
        self.address_city = self.user_address_city()
        self.address_phone = self.user_address_phone()
        self.address_postal = self.user_address_postal()
        self.create_widget()
        self.create_button()

    def user_address_info_data(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                return address['data']
        return {"data":"guest"}
    
    def user_address_name(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[0]
        return {"data":"guest"}
    
    def user_address_company(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[1]
        return {"data":"guest"}
    
    def user_address_country(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[2]
        return {"data":"guest"}
    
    def user_address_state(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[3]
        return {"data":"guest"}
    
    def user_address_city(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[4]
        return {"data":"guest"}

    def user_address(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[5]
        return {"data":"guest"}

    def user_address_phone(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[6]
        return {"data":"guest"}
    
    def user_address_postal(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address_name = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                address = address_name['data']
                data = address.split(',')
                return data[7]
        return {"data":"guest"}

    def create_widget(self):
      # create label for page title
        self.title_label = tk.Label(self, text="Edit and Delete the address", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # create labels and entry fields for user information
        self.username_label = tk.Label(self, text="Username:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.insert(0,self.address_name)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.company_label = tk.Label(self, text="Company:", font=("Arial", 12))
        self.company_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.company_entry = tk.Entry(self, width=30)
        self.company_entry.insert(0,self.address_company)
        self.company_entry.grid(row=2, column=1, padx=10, pady=5)

        self.country_label = tk.Label( self, text="Country:", font=("Arial", 12))
        self.country_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.country_entry = tk.Entry(self, width=30)
        self.country_entry.insert(0,self.address_country)
        self.country_entry.grid(row=3, column=1, padx=10, pady=5)

        self.state_label = tk.Label(self, text="State:", font=("Arial", 12))
        self.state_label.grid( row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.state_entry = tk.Entry(self, width=30)
        self.state_entry.insert(0,self.address_state)
        self.state_entry.grid(row=4, column=1, padx=10, pady=5)

        self.city_label = tk.Label(self, text="City:", font=("Arial", 12))
        self.city_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        self.city_entry = tk.Entry(self, width=30)
        self.city_entry.insert(0,self.address_city)
        self.city_entry.grid(row=5, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self, text="Address:", font=("Arial", 12))
        self.address_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
        self.address_entry = tk.Entry(self, width=30)
        self.address_entry.insert(0,self.address)
        self.address_entry.grid(row=6, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self, text="Phone number:", font=("Arial", 12))
        self.phone_label.grid( row=7, column=0, padx=10, pady=5, sticky=tk.E)
        self.phone_entry = tk.Entry(self, width=30)
        self.phone_entry.insert(0,self.address_phone)
        self.phone_entry.grid(row=7, column=1, padx=10, pady=5)

        self.postal_label = tk.Label(self, text="Postal code:", font=("Arial", 12))
        self.postal_label.grid( row=8, column=0, padx=10, pady=5, sticky=tk.E)
        self.postal_entry = tk.Entry(self, width=30)
        self.postal_entry.insert(0,self.address_postal)
        self.postal_entry.grid(row=8, column=1, padx=10, pady=5)

    def refresh_changes(self):
        try:
            self.address_name = self.user_address_name()
            self.username_entry.delete(0,'end')
            self.username_entry.insert(0,self.address_name)
            
            self.address_company = self.user_address_company()
            self.company_entry.delete(0,'end')
            self.company_entry.insert(0,self.address_company)
            
            self.address_country = self.user_address_country()
            self.country_entry.delete(0,'end')
            self.country_entry.insert(0,self.address_country)
            
            self.address_state = self.user_address_state()
            self.state_entry.delete(0,'end')
            self.state_entry.insert(0,self.address_state)
            
            self.address = self.user_address()
            self.address_entry.delete(0,'end')
            self.address_entry.insert(0,self.address)
            
            self.address_city = self.user_address_city()
            self.city_entry.delete(0,'end')
            self.city_entry.insert(0,self.address_city)
            
            self.address_phone = self.user_address_phone()
            self.phone_entry.delete(0,'end')
            self.phone_entry.insert(0,self.address_phone)
            
            self.address_postal = self.user_address_postal()
            self.postal_entry.delete(0,'end')
            self.postal_entry.insert(0,self.address_postal)
        except:
            print('Error')    
            
    def create_button(self):
        # create save button
        self.edit_button = tk.Button(self, text="Edit", font=("Arial", 12), command=self.save_changes)
        self.edit_button.grid(row=9, column=0, columnspan=1, pady=20)

        # delete button
        self.delete_button = tk.Button(self, text="Delete", font=("Arial", 12), command=self.delete_changes)
        self.delete_button.grid(row=9, column=1, columnspan=1, pady=20)
        
        self.refresh_button = tk.Button(self, text="Refresh", font=("Arial",12) ,command=self.refresh_changes)
        self.refresh_button.grid(row=9, column=2,columnspan=1,pady=20)

    def save_changes(self):
        # save changes to user information
        self.new_add = {
            "name": self.username_entry.get(),
            "company": self.company_entry.get(),
            "country": self.country_entry.get(),
            "state": self.state_entry.get(),
            "city": self.city_entry.get(),
            "address": self.address_entry.get(),
            "phone_number": self.phone_entry.get(),
            "postal_code": self.postal_entry.get()
        }
        self.name = self.new_add["name"]
        r1 = requests.put("http://127.0.0.1:8000/customer/address/", data=json.dumps(self.new_add))
        res1 = json.loads(r1.text)
        # show message box indicating changes have been saved
        if res1 == {"data": "Unable to edit address. Please try again"}:
            messagebox.showinfo(
                title='Error', message="You don't have account in this system. Please try again")
            # print(r1.json())
        else:
            r2 = requests.get(
                f"http://127.0.0.1:8000/customer/address?name={self.name}")
            res2 = json.loads(r2.text)
            messagebox.showinfo(
                title='Notice', message=f"Success edit the address {res2['data']}")

    def delete_changes(self):
        # save changes to user information
        if self.address_info is not None:
            self.name = self.username_entry.get()
            r = requests.delete(f"http://127.0.0.1:8000/customer/address?name={self.name}")
            res = json.loads(r.text)
        # show message box indicating changes have been saved
            if res == {"data": "Unable to delete the address"}:
                messagebox.showinfo( title='Error', message="You don't have account in this system. Please try again")
                print(r.json())
            else:
                messagebox.showinfo(title='Notice', message="Success delete the address")
                r2 = requests.get(f"http://127.0.0.1:8000/customer/address?name={self.name}")
                res2 = json.loads(r2.text)
                print(res2['data'])
                print(r2.json())
        else:
            messagebox.showinfo( title='Error', message="You don't have account in this system. Please try again")
            print(r.json())
