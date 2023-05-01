import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as sd
import requests, json
from make_review import MakeReview
import io
import urllib.request 
from PIL import Image, ImageTk 
from datetime import datetime

class MakePayment(tk.Frame): 

    def __init__(self,master=None,submaster=None): 
        super().__init__(master)
        self.choose_address = {}
        self.show_recript_address = tk.Label(self,text=f"default")
        self.final_show = 0
        self.final_price = 0
        self.code_coupon = []
        self.coupon_list = []
        self.number_click =[]
        self.get_cart_data()
        self.create_normal_widget()
        self.show_total_payment_widget()
        self.create_receipt_widget()
        self.submaster = submaster
        self.master = master
        self.get_coupon_info()
        self.create_widget()
        self.show_coupon_info()

    def create_normal_widget(self): 
        self.back_button = tk.Button(self,text="back",command=self.back)
        self.back_button.pack()
        self.back_button.place(x=500,y=500)

        self.update_payment_button = tk.Button(self,text="update payment",command=self.update_payment).place(x=400,y=400)

        self.receipt_label = tk.Label(self,text="receipt", font=("Helvetica", 12, "bold")).place(x=150, y=25)

        self.date = tk.Label(self, text="buy date           {}".format(datetime.now().strftime("%d-%m-%Y"))).place(x=100, y=75)

        self.decolate_1 = tk.Label(self,text="___________________________________________________________________").place(x=25, y=100)

        self.name_label = tk.Label(self,text="tool name").place(x = 50, y = 125)
        self.price_label = tk.Label(self,text="tool price").place(x = 125, y = 125)
        self.amoung_label = tk.Label(self,text="tool Quantity").place(x = 200, y = 125)
        self.total_price_label = tk.Label(self,text="total price").place(x = 275, y = 125)

        

        self.decolate_2 = tk.Label(self,text="___________________________________________________________________").place(x=25, y=500)

    def show_total_payment_widget(self):
        self.total_price_label = tk.Label(self, text="total item price                       ")
        self.total_price_label.pack()
        self.total_price_label.place(x=50, y=550)
        self.shipping_cost_label = tk.Label(self, text="shipping cost                        ")
        self.shipping_cost_label.pack()
        self.shipping_cost_label.place(x=50, y=600)
        self.final_price_label = tk.Label(self, text="final price                            ")
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)


        self.total_price_label = tk.Label(self, text="total item price             {}".format(self.total_price))
        self.total_price_label.pack()
        self.total_price_label.place(x=50, y=550)
        self.shipping_cost_label = tk.Label(self, text="shipping cost             {}".format(self.shipping_cost))
        self.shipping_cost_label.pack()
        self.shipping_cost_label.place(x=50, y=600)
        self.final_price_label = tk.Label(self, text="final price                          ")
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        self.final_price_label = tk.Label(self, text="final price             {}".format(self.final_show))
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)

    def create_receipt_widget(self): 
        for i,list_component in enumerate(self.list_tool) :
            for j,component in enumerate(list_component) : 
                self.widget= tk.Label(self, text=component)
                self.widget.pack() 
                self.widget.place(x = 50+75*j,y = 175+50*i)

    def destroy_widget(self):
        self.total_price_label.destroy()
        self.shipping_cost_label.destroy()
        self.final_price_label.destroy()

    def clear_item(self):
        for i in range(4): 
            for j in range(5): 
                self.widget = tk.Label(self, text="                        ", font=("Helvetica", 12))
                self.widget.pack() 
                self.widget.place(x = 50+75*j,y = 175+50*i)


    def update_payment(self):
        # print(self.choose_address)
        self.get_cart_data()
        self.destroy_widget()
        self.clear_item()
        self.show_total_payment_widget()
        self.create_receipt_widget()
        self.get_address()
        self.get_coupon_info()
        self.check_show_recript_address()
        self.show_coupon_info()
        self.show_address_info()

    def get_cart_data(self):
        r = requests.get(f'http://127.0.0.1:8000/system/shopping_cart/')
        # print("-------------------------------------------------------")
        # print("get_cart_data pass")
        # print(r.json())
        # print("--------------------------------------------------")
        self.in_cart = r.json()['_cart'] # got list // dict
        # self.item_info = self.in_cart[0] # got dict tool with info
        self.get_info_in_list()
        self.total_price = r.json()['_total_price']
        self.shipping_cost = r.json()['_shipping_price']
        self.final_price = r.json()['_final_price']

    def get_info_in_list(self):
        # print("get_info_in_list pass")
        self.list_tool = []
        for item in range(len(self.in_cart)):
            # print(item) 
            list_components= []
            self.item_info = self.in_cart[item]
            self.get_tool_info = self.item_info['_tool']

            # require data
            self.tool_name = self.get_tool_info['_name']
            
            self.total_price = self.item_info['_items_price']
            
            self.amount = self.item_info['_buy_amount']
            
            self.tool_price = self.get_tool_info['_price']

            list_components.append(self.tool_name) 
            list_components.append(self.tool_price) 
            list_components.append(self.amount) 
            list_components.append(self.total_price)
            self.list_tool.append(list_components)
    
    def back(self):
        self.master.show_cart()

    def create_widget(self): 
        self.back_button = tk.Button(self,text="back",command=self.back)
        self.back_button.pack()
        self.back_button.place(x=20,y=500)

        self.confirm_label = tk.Button(self,text="confirm",command=self.confirm_button)
        self.confirm_label.pack()
        self.confirm_label.place(x=500,y=500)
        

    def get_coupon_info(self): 
        user = requests.get("http://127.0.0.1:8000/me").json()
        # print(user) 
        self.coupon_list = []
        self.number_click =[]
        for key in user.keys(): 
            if key == 'username': 
                username = user["username"]["user"]
                coupon = requests.get(f"http://127.0.0.1:8000/coupons/active_coupon/?username={username}").json()
                # print(coupon)
                for key in coupon.keys(): 
                    self.code_coupon.append(key)
                    component_list = []   
                    component_list.append(coupon[key]['name'])
                    component_list.append(coupon[key]['discount_value'])
                    self.coupon_list.append(component_list)
                    self.number_click.append(0)

    def show_coupon_info(self): 
        for j in range(20): 
            self.clear = tk.Label(self,text="                                                     ")
            self.clear.pack()
            self.clear.place(x=700,y=20+15*j)
        for i,coupon in enumerate(self.coupon_list):
            self.button = tk.Button(self,text=coupon[0],command=lambda i=i,coupon=self.coupon_list:self.on_click(i,coupon))
            self.button.pack()
            self.button.place(x=700,y=20+40*i)
    
    def on_click(self,no,coupon): 
        check = 0
        for i in self.number_click: 
            if i % 2 ==1 and i != self.number_click[no]:
                check = 1
        if check == 0 : 
            self.number_click[no] += 1 

        check2 =0
        for index,i in enumerate(self.number_click): 
            if i % 2 == 1 :
                discount = int(coupon[index][1])*self.final_price/100
                self.to_use_coupon(discount)
                check2 = 1
        if check2==0 :
            self.to_unuse_coupon()
        # print(self.number_click)
            
    def to_use_coupon(self,discount_value): 
        self.final_show = self.final_price - discount_value
        self.final_price_label = tk.Label(self, text="final price                               ")
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        self.final_price_label = tk.Label(self, text="final price             {}".format(self.final_show))
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        # self.show_final_price()
    def to_unuse_coupon(self): 
        self.final_show = self.final_price
        self.final_price_label = tk.Label(self, text="final price                               ")
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        self.final_price_label = tk.Label(self, text="final price             {}".format(self.final_show))
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        # self.show_final_price()

    def on_click_address(self,index): 
        dict_add,list_add = self.get_address() 
        self.choose_address = dict_add[index]
        self.show_recript_address = tk.Label(self,text=f" send at {list_add[index][0]} {list_add[index][1]} {list_add[index][2]} {list_add[index][3]} {list_add[index][4]} {list_add[index][5]}")
        if self.choose_address != {}: 
            self.show_recript_address.pack(in_ = self)
            self.show_recript_address.place(x=50,y=470)
    
    def check_show_recript_address(self): 
        if self.choose_address == {}: 
            self.show_recript_address.pack(in_ = None)
            self.show_recript_address.pack_forget() 
        else : 
            self.show_recript_address.pack(in_ = self)
            self.show_recript_address.place(x=50,y=470)

    def show_address_info(self): 
        self.address_label = tk.Label(self,text="Choose address ",font=18)
        self.address_label.pack()
        self.address_label.place(x=600,y=305)
        dict_add,list_add = self.get_address()
        for i,address in enumerate(list_add):
            self.address_button = tk.Button(self,text=f"{address[0]} {address[1]} {address[3]} {address[4]} {address[5]}",command = lambda x = i: self.on_click_address(x))
            self.address_button.pack()
            self.address_button.place(x=600,y=350+20*i)
    def get_address(self): 
        user =requests.get("http://127.0.0.1:8000/me").json()  
        addresses = []
        for key in user.keys(): 
            if key == 'username': 
                name = user["username"]["user"]   
                username = requests.get(f'http://127.0.0.1:8000/user//?username={name}').json()
                # print(username['first_name']['_addresses']) 
                for com in username['first_name']['_addresses'] :
                    component = []
                    component.append(com["_company"])
                    component.append(com["_country"])
                    component.append(com["_state"])
                    component.append(com["_city"])
                    component.append(com["_address"])
                    component.append(com["_postal_code"]) 
                    addresses.append(component)
                # print(addresses)
                return username['first_name']['_addresses'],addresses
        return {"data":"guest"}
    def confirm_button(self):  
        for index,i in enumerate(self.number_click): 
            if i % 2 == 1:
                code  =  self.code_coupon[index]
                card = sd.askstring("credit card", "Please enter credit card:") 
                dict_payment = {'card':card,'address':self.choose_address['_name'],'coupon':code}
                message = requests.post("http://127.0.0.1:8000/cart/payment",data = json.dumps(dict_payment))
                print(message.json())
                self.final_price = 0
                self.shipping_cost = 0
                self.final_show = 0
                self.choose_address = {}
                messagebox.showinfo(title = "notification",message=message.json()["status"])
                return 
        code  =  None
        card = sd.askstring("credit card", "Please enter credit card:") 
        dict_payment = {'card':card,'address':self.choose_address['_name'],'coupon':code}
        message = requests.post("http://127.0.0.1:8000/cart/payment",data = json.dumps(dict_payment))
        print(message.json())
        self.final_price = 0
        self.shipping_cost = 0
        self.final_show = 0
        self.choose_address = {}
        messagebox.showinfo(title = "notification",message=message.json()["status"])
        return
    