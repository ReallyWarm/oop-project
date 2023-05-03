import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox
import requests 
import json  

class ManageWholesale(tk.Frame): 
    def __init__(self,master): 
        super().__init__(master)
        self.event = None
        self.wholeale_list = []
        self.get_wholesalewidget = [] 
        self.add_wholesalewidget = []
        self.modify_wholesalewidget = []
        self.create_widget()
        self.get_wholesale_info()
        self.do_dropdown()

    def create_widget(self):  
        tk.Label(self,text="manage wholesale", font=("Helvetica", 18)).place(x=290,y=30)
        
        self.back_to_admin_button = tk.Button(self,text="back",command=self.Back)
        self.back_to_admin_button.pack() 
        self.back_to_admin_button.place(x=800, y=5) 

        
    def get_wholesale_info(self): 
        wholesale_all = requests.get("http://127.0.0.1:8000/wholesale/all").json()
        self.wholesale_list = []
        for key in wholesale_all: 
            components = [] 
            components.append(key)
            components.append(wholesale_all[key]['discount_value']) 
            components.append(wholesale_all[key]['amount'])
            self.wholesale_list.append(components) 


    def create_getwholesale_widget(self): 
        self.get_wholesalewidget = [] 
        for wholesale in self.wholesale_list: 
            self.button_widget = tk.Button(self,text=f"{wholesale[0]} {wholesale[2]} {wholesale[1]}",command = lambda x=wholesale[0],y=wholesale[2],z=wholesale[1]:self.modify_wholesale(x,y,z))
            self.get_wholesalewidget.append(self.button_widget) 

    def add_wholesale(self): 
        self.code_label = tk.Label(self, text="Code:") 
        self.code_label_input = tk.Entry(self)
        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_label_input = tk.Entry(self) 
        self.discount_label = tk.Label(self, text="Discount value:")
        self.discount_label_input = tk.Entry(self)   
        self.title = tk.Label(self, text="Add wholesale")
        self.summit_button_label = tk.Button(self,text="summit",command=self.submit_button)
        self.add_wholesalewidget = [self.code_label,self.code_label_input,self.amount_label,self.amount_label_input,self.discount_label,self.discount_label_input,self.title,self.summit_button_label]

    def show_add_wholesale(self): 
        for i,widget in enumerate(self.add_wholesalewidget): 
            widget.pack(in_ = self) 
            widget.place(x=300,y=100+ 30*i)

    def hide_add_wholesale(self): 
        for widget in self.add_wholesalewidget:  
            widget.pack(in_ = None) 
            widget.pack_forget()
    
    def modify_wholesale(self,code,amount,discount_value): 
        self.hide_getwidget() 
        self.create_modify_widget(code,amount,discount_value) 
        self.show_modify() 

    def update_wholesale(self,code): 
        amount = self.mamount_label_input.get() 
        discount_value = self.mdiscount_label_input.get() 
        if not discount_value.isdigit(): 
            messagebox.showinfo(title="notification",message="discount_value must be integer")
            return 
        if int(discount_value) <= 0 : 
            messagebox.showinfo(title="notification",message="discount_value must be positive integer") 
            return
        if not amount.isdigit(): 
            messagebox.showinfo(title="notification",message="amount must be integer")
            return  
        if int(amount) <= 0 : 
            messagebox.showinfo(title="notification",message="amount must be positive integer") 
            return
        dict_put = {"wholesale_modify":{"code":code,"amount":amount,"discount_value":discount_value}}
        message = requests.put("http://127.0.0.1:8000/wholesale/all",data=json.dumps(dict_put))
        self.mamount_label_input.delete(0,tk.END)
        self.mdiscount_label_input.delete(0,tk.END) 
        self.get_wholesale_info() 
        self.show_selected(self.event)

    def delete_button(self,code):  
        dict_delete = {"code":code}
        message = requests.delete("http://127.0.0.1:8000/wholesale/all",data=json.dumps(dict_delete))
        self.get_wholesale_info() 
        self.show_selected(self.event)

    def submit_button(self):  
        amount = self.amount_label_input.get() 
        code = self.code_label_input.get() 
        discount_value = self.discount_label_input.get() 
        if not discount_value.isdigit(): 
            messagebox.showinfo(title="notification",message="discount_value must be integer")
            return 
        if int(discount_value) <= 0 : 
            messagebox.showinfo(title="notification",message="discount_value must be positive integer") 
            return
        if not amount.isdigit(): 
            messagebox.showinfo(title="notification",message="amount must be integer")
            return 
        if int(amount) <= 0 : 
            messagebox.showinfo(title="notification",message="amount must be positive integer") 
            return
        dict_add = {"wholesale_add":{"code":code, "amount":amount,"discount_value":discount_value}}
        for wholesale in self.wholesale_list:  
            if wholesale[0] == code : 
                messagebox.showinfo(title="notification",message="this code had already added")
                return
        message = requests.post("http://127.0.0.1:8000/wholesale/all",data=json.dumps(dict_add))
        self.amount_label_input.delete(0,tk.END) 
        self.code_label_input.delete(0,tk.END) 
        self.discount_label_input.delete(0,tk.END)
        self.get_wholesale_info() 

    
    
    def create_modify_widget(self,code,amount,discount_value): 

        self.mdiscount_label = tk.Label(self, text="Discount Value:")
        self.mdiscount_label_input = tk.Entry(self) 
        self.mdiscount_label_input.insert(0,discount_value)
        self.mamount_label = tk.Label(self, text="Amount:")
        self.mamount_label_input = tk.Entry(self)  
        self.mamount_label_input.insert(0,amount)
        self.mtitle = tk.Label(self, text="mofidy")
        self.modify_button_label = tk.Button(self,text="update",command= lambda x=code : self.update_wholesale(x))
        self.delete_button_label = tk.Button(self,text="delete",command= lambda x=code : self.delete_button(x))
        self.modify_wholesalewidget = [self.mdiscount_label,self.mdiscount_label_input,self.mamount_label,self.mamount_label_input,self.mtitle,self.modify_button_label,self.delete_button_label]

    def hide_modify(self): 
        for m_widget in self.modify_wholesalewidget: 
            m_widget.pack(in_ =None) 
            m_widget.pack_forget()

    def show_modify(self): 
        for i,m_widget in enumerate(self.modify_wholesalewidget): 
            m_widget.pack(in_ =self) 
            m_widget.place(x=300,y=100 + 50*i)

    def do_dropdown(self): 
        self.choice = tk.StringVar(self, value="chose to do")
        self.combo = ttk.Combobox(self, textvariable=self.choice)
        self.combo["values"] = ("add wholesale","modify wholesale")
        self.combo.bind("<<ComboboxSelected>>",self.show_selected)
        self.combo.place(x = 550, y = 50) 

    
    def show_selected(self,event):
        self.event = event
        if self.choice.get() == "modify wholesale":
            self.create_getwholesale_widget()
            self.show_getwidget()
            self.hide_add_wholesale() 
            self.hide_modify()
        
        elif self.choice.get() == "add wholesale":
            self.hide_getwidget() 
            self.add_wholesale() 
            self.show_add_wholesale()
            self.hide_modify()

    def show_getwidget(self): 
        for i,wholesale in enumerate(self.get_wholesalewidget):
            wholesale.pack(in_ = self)
            wholesale.place(x = 300,y = 100 + 50*i)
    
    def hide_getwidget(self): 
        for wholesale in self.get_wholesalewidget: 
            wholesale.pack(in_ = None)
            wholesale.pack_forget()

    def Back(self): 
        self.master.show_admin()