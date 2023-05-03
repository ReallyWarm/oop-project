import tkinter as tk
import requests

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
        self.review = self.user_review()
       
        self.create_widget()
        
    def user_name_data(self): 
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                return username['first_name']['_username']
        return {"data":"guest"}
    
    def user_email(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                return username['first_name']['_email']
        return {"data":"guest"}
    
    def user_firstname(self):
        user =requests.get("http://127.0.0.1:8000/me").json()  
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                return username['first_name']['_first_name']
        return {"data":"guest"}
    
    def user_lastname(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                return username['first_name']['_last_name']
        return {"data":"guest"}
    
    def user_company(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                return username['first_name']['_company_name']
        return {"data":"guest"}
    
    def user_address(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                address = requests.get(f'http://127.0.0.1:8000/customer/address?name={name}').json()
                return address['data']
        return {"data":"guest"}

    
     
    def user_order(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                order = requests.get(f'http://127.0.0.1:8000/customer/order?name={name}').json()
                print(order)
                string_sent = "" 
                for pay_id in order.keys(): 
                        # totalprice = 0
                    string_sent  += "payment id :" + str(pay_id)
                    string_sent += "\n" 
                    for key in order[pay_id]:  
                        if key == "order":
                            for tool in order[pay_id]["order"] :
                                string_sent += str(tool["_tool"]["_name"]) + " amount : " +str(tool['_buy_amount']) + " price_per_unit  " +str(tool["_tool"]["_price"]) +" item_price " +str(tool['_items_price'])
                                string_sent += "\n" 
                        if key == "total price":
                            string_sent += "\n"
                            string_sent += " total price " + str(order[pay_id]["total price"])
                    string_sent += "\n" + "\n"
                return string_sent
        return {"data":"guest"}
     
    
    def user_review(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                review = requests.get(f'http://127.0.0.1:8000/customer/review?name={name}').json()
                return review['data']
        return {"data":"guest"}
     

    def create_widget(self):
        
        
        self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        self.username_label.pack()
        
        self.firstname_title = tk.Label(self,text="First Name", font= ('Arail',12,'bold'))
        self.firstname_title.pack()
        self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        self.firstname_label.pack()
        
        self.lastname_title = tk.Label(self,text="Last Name", font=('Arail',12,'bold'))
        self.lastname_title.pack()
        self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        self.lastname_label.pack()
        
        self.email_title = tk.Label(self,text="E-mail", font=('Arail',12,'bold'))
        self.email_title.pack()
        self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        self.email_label.pack()
        
        self.company_title = tk.Label(self,text="Company", font=('Arail',12,'bold'))
        self.company_title.pack()
        self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        self.company_label.pack()
        
        self.address_title = tk.Label(self,text="Address", font=('Arail',12,'bold'))
        self.address_title.pack()
        self.address_text = tk.Text(self,height=5,width=40)
        self.address_text.insert('end',self.address)
        self.address_text.pack()
        
        
        self.order_title = tk.Label(self,text="Order", font=('Arail',12,'bold'))
        self.order_title.pack()
        self.order_text = tk.Text(self,height=5,width=40)
        self.order_text.insert('end',self.order)
        self.order_text.pack()
        
        self.review_title = tk.Label(self,text="Review", font=('Arail',12,'bold'))
        self.review_title.pack()
        self.review_text = tk.Text(self,height=5,width=40)
        self.review_text.insert('end',self.review)
        self.review_text.pack()
        
    def delete_data(self):
        
        self.username_label.destroy()
        self.firstname_label.destroy()
        self.firstname_title.destroy()
        self.lastname_label.destroy()
        self.lastname_title.destroy()
        self.email_label.destroy()
        self.email_title.destroy()
        self.company_label.destroy()
        self.company_title.destroy()
        self.address_text.destroy()
        self.address_title.destroy()
        self.order_text.destroy()
        self.order_title.destroy()
        self.review_text.destroy()
        self.review_title.destroy()
        
        
    def update_username(self):
        self.username = self.user_name_data()
        self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        self.username_label.pack()
        
        
    def update_firstname(self):
        self.firstname = self.user_firstname()
        self.firstname_title = tk.Label(self,text="First Name", font= ('Arail',12,'bold'))
        self.firstname_title.pack()
        self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        self.firstname_label.pack()
        
    
    
    def update_lastname(self):
        self.lastname = self.user_lastname()
        self.lastname_title = tk.Label(self,text="Last Name", font=('Arail',12,'bold'))
        self.lastname_title.pack()
        self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        self.lastname_label.pack()
        
    
    def update_email(self):
        self.email = self.user_email()
        self.email_title = tk.Label(self,text="E-mail", font=('Arail',12,'bold'))
        self.email_title.pack()
        self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        self.email_label.pack()
        
        
    def update_company(self):
        self.company =self.user_company()
        self.company_title = tk.Label(self,text="Company", font=('Arail',12,'bold'))
        self.company_title.pack()
        self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        self.company_label.pack()
        
    
    def update_address(self):
        self.address = self.user_address()
        self.address_title = tk.Label(self,text="Address", font=('Arail',12,'bold'))
        self.address_title.pack()
        self.address_text = tk.Text(self,height=5,width=40)
        self.address_text.insert('end',self.address)
        self.address_text.pack()
        
    def update_review(self):
        self.review = self.user_review() 
        self.review_title = tk.Label(self,text="Review", font=('Arail',12,'bold'))
        self.review_title.pack()
        self.review_text = tk.Text(self,height=5,width=40)
        self.review_text.insert('end',self.review)  
        self.review_text.pack()
        
    def update_order(self):
        self.order = self.user_order()
        self.order_title = tk.Label(self,text="Order", font=('Arail',12,'bold'))
        self.order_title.pack()
        self.order_text = tk.Text(self,height=5,width=40)
        self.order_text.insert('end',self.order)
        self.order_text.pack()
        
    def update_data(self):
        self.delete_data()
        self.update_username()
        self.update_firstname()
        self.update_lastname()
        self.update_email()
        self.update_company()
        self.update_address()
        self.update_order()
        self.update_review()