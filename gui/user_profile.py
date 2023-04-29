import tkinter as tk
import requests
# from create_address import CreateAddressGUI
# from delete_edit_address import EditDeleteAddressGUI

class Profile(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master =master
        self.username = self.user_name_data()
        self.email = self.user_email()
        self.firstname = self.user_firstname()
        self.lastname = self.user_lastname()
        self.company =self.user_company()
        self.address = self.user_address()
        self.order = self.user_order()
        # self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        # self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        # self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        # self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        # self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        # self.address_text = tk.Text(self,height=10,width=80)
        # self.create_address = CreateAddressGUI(self)
        # self.edit_delete_address = EditDeleteAddressGUI(self)
        self.create_widget()
        
    def user_name_data(self): 
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_username']
        return {"data":"guest"}
    
    def user_email(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_email']
        return {"data":"guest"}
    
    def user_firstname(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_first_name']
        return {"data":"guest"}
    
    def user_lastname(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_last_name']
        return {"data":"guest"}
    
    def user_company(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_company_name']
        return {"data":"guest"}
    
    def user_address(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_addresses']
        return {"data":"guest"}
    
     
    def user_order(self):
        user =dict(requests.get("http://127.0.0.1:8000/me").json() ) 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['data']['_my_order']
        return {"data":"guest"}
    
     
    # def delete_data(self):
    #     self.username_label.destroy()
    #     self.lastname_label.destroy()
    #     self.email_label.destroy()
    #     self.company_label.destroy()
    #     self.address_text.destroy()
     
    def create_widget(self):
        
    
        self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        self.username_label.grid(row=0,column=1,columnspan=2,pady=30)
        # self.username_label.pack()
        # self.username_label.place(x=400,y=0)
        
        self.firstname_title = tk.Label(self,text="First Name:", font= ('Arail',12,'bold'))
        self.firstname_title.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        # self.firstname_title.pack()
        # self.firstname_title.place(x=30,y=50)
        self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        self.firstname_label.grid(row=1, column=1, padx=10, pady=5)
        # self.firstname_label.pack()
        # self.firstname_label.place(x=120,y=50)
        
        self.lastname_title = tk.Label(self,text="Last Name:", font=('Arail',12,'bold'))
        self.lastname_title.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        # self.lastname_title.pack()
        # self.lastname_title.place(x=350,y=50)
        self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        self.lastname_label.grid(row=2, column=1, padx=10, pady=5)
        # self.lastname_label.pack()
        # self.lastname_label.place(x=450,y=50)
        
        self.email_title = tk.Label(self,text="E-mail:", font=('Arail',12,'bold'))
        self.email_title.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        # self.email_title.pack()
        # self.email_title.place(x=30,y=100)
        self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        self.email_label.grid(row=3, column=1, padx=10, pady=5)
        # self.email_label.pack()
        # self.email_label.place(x=100,y=100)
        
        self.company_title = tk.Label(self,text="Company:", font=('Arail',12,'bold'))
        self.company_title.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        # self.company_title.pack()
        # self.company_title.place(x=300,y=100)
        self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        self.company_label.grid(row=4, column=1, padx=10, pady=5)
        # self.company_label.pack()
        # self.company_label.place(x=400,y=100)
        
        self.address_title = tk.Label(self,text="Address:", font=('Arail',12,'bold'))
        self.address_title.grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        # self.address_title.pack()
        # self.address_title.place(x=30,y=150)
        self.address_text = tk.Text(self,height=10,width=80)
        self.address_text.insert('end',self.address)
        self.address_text.grid(row=5, column=1, padx=10, pady=5)
        # self.address_text.pack()
        # self.address_text.place(x=105,y=150)


        self.order_title = tk.Label(self,text="Order:", font=('Arail',12,'bold'))
        self.order_title.grid(row=6, column=0, padx=10, pady=5, sticky=tk.E)
        # self.order_title.pack()
        # self.order_title.place(x=30,y=350)
        self.order_text = tk.Text(self,height=5,width=40)
        self.order_text.insert('end',self.order)
        self.order_text.grid(row=6, column=1, padx=10, pady=5)
        # self.order_text.pack()
        # self.order_text.place(x=100,y=350)
        
        
        
        # self.view_order_button = tk.Button(self, text="Your order", font=("Arial", 12), command=self.show_order)
        # self.view_order_button.pack()
        # self.view_order_button.place(x=500, y=600)
        
        # self.view_review_button = tk.Button(self, text="Your review", font=("Arial", 12), command=self.show_review)
        # self.view_review_button.pack()
        # self.view_review_button.place(x=650, y=600)
        
   