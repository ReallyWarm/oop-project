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
        self.firstname_title = tk.Label(self,text="First Name", font= ('Arail',12,'bold'))
        self.lastname_title = tk.Label(self,text="Last Name", font=('Arail',12,'bold'))
        self.email_title = tk.Label(self,text="E-mail", font=('Arail',12,'bold'))
        self.company_title = tk.Label(self,text="Company", font=('Arail',12,'bold'))
        self.address_title = tk.Label(self,text="Address", font=('Arail',12,'bold'))
        self.order_title = tk.Label(self,text="Order", font=('Arail',12,'bold'))
        self.review_title = tk.Label(self,text="Review", font=('Arail',12,'bold'))
        self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        self.address_text = tk.Text(self,height=5,width=40)
        self.order_text = tk.Text(self,height=5,width=40)
        self.review_text = tk.Text(self,height=5,width=40)
        
        # self.create_widget()
        
    def user_name_data(self): 
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_username']
        return {"data":"guest"}
    
    def user_email(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_email']
        return {"data":"guest"}
    
    def user_firstname(self):
        user =requests.get("http://127.0.0.1:8000/me").json()  
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_first_name']
        return {"data":"guest"}
    
    def user_lastname(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_last_name']
        return {"data":"guest"}
    
    def user_company(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_company_name']
        return {"data":"guest"}
    
    def user_address(self):
        user =requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_addresses']
        return {"data":"guest"}
    
     
    def user_order(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_my_order']
        return {"data":"guest"}
     
    
    def user_review(self):
        user =requests.get("http://127.0.0.1:8000/me").json()
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user/?username={name}').json()
                return username['first_name']['_my_review']
        return {"data":"guest"}
     
    # idea delete all pages and paste a new item
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
   
    def update_username(self):
        self.username = self.user_name_data()
        self.username_label = tk.Label(self, text=self.username, font=("Arial", 18, "bold"))
        self.username_label.pack()
        print(self.username)
        
    def update_firstname(self):
        self.firstname = self.user_firstname()
        self.firstname_title = tk.Label(self,text="First Name", font= ('Arail',12,'bold'))
        self.firstname_title.pack()
        self.firstname_label = tk.Label (self,text=self.firstname,font=("Arial", 12))
        self.firstname_label.pack()
        print(self.firstname)
    
    
    def update_lastname(self):
        self.lastname = self.user_lastname()
        self.lastname_title = tk.Label(self,text="Last Name", font=('Arail',12,'bold'))
        self.lastname_title.pack()
        self.lastname_label = tk.Label(self,text=self.lastname,font=('Arail',12))
        self.lastname_label.pack()
        print(self.lastname)
    
    def update_email(self):
        self.email = self.user_email()
        self.email_title = tk.Label(self,text="E-mail", font=('Arail',12,'bold'))
        self.email_title.pack()
        self.email_label = tk.Label(self,text=self.email,font=('Arail',12))
        self.email_label.pack()
        print(self.email)
        
    def update_company(self):
        self.company =self.user_company()
        self.company_title = tk.Label(self,text="Company", font=('Arail',12,'bold'))
        self.company_title.pack()
        self.company_label = tk.Label(self,text=self.company,font=('Arail',12))
        self.company_label.pack()
        print(self.company)
    
    def update_address(self):
        self.address = self.user_address()
        self.address_title = tk.Label(self,text="Address", font=('Arail',12,'bold'))
        self.address_title.pack()
        self.address_text = tk.Text(self,height=5,width=40)
        self.address_text.insert('end',self.address)
        self.address_text.pack()
        print(self.address)
        
    def update_order(self):
        self.order = self.user_order()
        self.order_title = tk.Label(self,text="Order", font=('Arail',12,'bold'))
        self.order_title.pack()
        self.order_text = tk.Text(self,height=5,width=40)
        self.order_text.insert('end',self.order)
        self.order_text.pack()
        print(self.order)

    def update_review(self):
        self.review = self.user_review() 
        self.review_title = tk.Label(self,text="Review", font=('Arail',12,'bold'))
        self.review_title.pack()
        self.review_text = tk.Text(self,height=5,width=40)
        self.review_text.insert('end',self.review)  
        self.review_text.pack()
        print(self.review)
        
    def create_widget(self):
        
        #create username label
        self.username_label.pack()
      
        #create title firstname
        # self.firstname_title = tk.Label(self,text="First Name:", font= ('Arail',12,'bold'))
        self.firstname_title.pack()
        
        #show firstname data
        self.firstname_label.pack()
      
        #create title lastname
        # self.lastname_title = tk.Label(self,text="Last Name:", font=('Arail',12,'bold'))
        self.lastname_title.pack()
       
    #    #show lastname data
        self.lastname_label.pack()
        
    #     #create title email
    #     # self.email_title = tk.Label(self,text="E-mail:", font=('Arail',12,'bold'))
        self.email_title.pack()
      
    #     #show email data
        self.email_label.pack()
       
        #create title company
        # self.company_title = tk.Label(self,text="Company:", font=('Arail',12,'bold'))
        self.company_title.pack()
      
        #show company data
        self.company_label.pack()
        
       
        #create title address
        # self.address_title = tk.Label(self,text="Address:", font=('Arail',12,'bold'))
        self.address_title.pack()
        
        #show address
        self.address_text.insert('end',self.address)
        self.address_text.pack()
       
        #create title order
        # self.order_title = tk.Label(self,text="Order:", font=('Arail',12,'bold'))
        self.order_title.pack()
       
        #show order data
        self.order_text.insert('end',self.order)
        self.order_text.pack()
       
        #create title review
        # self.review_title = tk.Label(self,text="Review:", font=('Arail',12,'bold'))
        self.review_title.pack()
        
        #show review data
        self.review_text.insert('end',self.review)
        self.review_text.pack()
      
        
 