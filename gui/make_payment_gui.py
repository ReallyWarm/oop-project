import tkinter as tk
import requests, json
from make_review import MakeReview
import io
import urllib.request 
from PIL import Image, ImageTk 
from datetime import datetime

class MakePayment(tk.Frame): 

    def __init__(self,master=None,submaster=None): 
        super().__init__(master)
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
        self.get_cart_data()
        self.destroy_widget()
        self.clear_item()
        self.show_total_payment_widget()
        self.create_receipt_widget()

        self.get_coupon_info()
        # self.show_final_price()
        self.show_coupon_info()

    def get_cart_data(self):
        r = requests.get(f'http://127.0.0.1:8000/system/shopping_cart/')
        print("-------------------------------------------------------")
        print("get_cart_data pass")
        print(r.json())
        print("--------------------------------------------------")
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
            print(item) 
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
        print(user) 
        self.coupon_list = []
        self.number_click =[]
        for key in user.keys(): 
            if key == 'username': 
                username = user["username"]["user"]
                coupon = requests.get(f"http://127.0.0.1:8000/coupons/active_coupon/?username={username}").json()
                print(coupon)
                for key in coupon.keys(): 
                    self.code_coupon.append(key)
                    component_list = []   
                    component_list.append(coupon[key]['name'])
                    component_list.append(coupon[key]['discount_value'])
                    self.coupon_list.append(component_list)
                    self.number_click.append(0)
        print(self.coupon_list)
    def show_final_price(self):
        print(self.final_price)
        self.final_price_label = tk.Label(self,text="        ")
        self.final_price_label.pack()
        self.final_price_label.place(x=500,y=500)
        self.final_price_label = tk.Label(self,text=self.final_show)
        self.final_price_label.pack()
        self.final_price_label.place(x=500,y=500)

    def show_coupon_info(self): 
        for j in range(20): 
            self.clear = tk.Label(self,text="                                                     ")
            self.clear.pack()
            self.clear.place(x=700,y=20+20*j)
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
                discount = coupon[index][1]*self.final_price/100
                self.to_use_coupon(discount)
                check2 = 1
        if check2==0 :
            self.to_unuse_coupon()
        print(self.number_click)
            
    def to_use_coupon(self,discount_value): 
        self.final_show = self.final_price - discount_value
        self.final_price_label = tk.Label(self, text="final price             {}".format(self.final_show))
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        # self.show_final_price()
    def to_unuse_coupon(self): 
        self.final_show = self.final_price
        self.final_price_label = tk.Label(self, text="final price             {}".format(self.final_show))
        self.final_price_label.pack()
        self.final_price_label.place(x=50, y=650)
        # self.show_final_price()
    def confirm_button(self): 
        for index,i in enumerate(self.number_click): 
            if i % 2 == 1:
                code  =  self.code_coupon[index]
                self.message = requests.post(f"http://127.0.0.1:8000/coupons/used_coupon/?code={code}").json()
                requests.delete(f'http://127.0.0.1:8000/system/shopping_cart/delete_cart/')
                self.final_price = 0
                self.shipping_cost = 0
                self.final_show = 0
                print(self.message)
                print(code)
    