import tkinter as tk
import requests, json
from tkinter import messagebox
import io
import urllib.request 
from PIL import Image, ImageTk

class WishlistGui(tk.Frame): 

    def __init__(self,master): 
        super().__init__(master) 
        self.list_tool =[]
        self.master = master
        self.total = None
        self.create_normal_widget()

        self.send_to_cart_button = tk.Button(self,text="Send to Cart",command=self.send_to_cart)
        self.send_to_cart_button.pack()
        self.send_to_cart_button.place(x=660,y=500)

    def send_to_cart(self):
        if len(self.in_wishlist) == 0:
            messagebox.showinfo(title="notification",message="Please add item first")
            return
        r = requests.get(f'http://127.0.0.1:8000/system/wishlist/')
        in_wishlist = r.json()['_wish_product']
        for item in in_wishlist:
            item_info = item
            tool_info = item_info['_tool']

            tool_name = tool_info['_name']
            tool_stock = tool_info['_amount']
            amount = item_info['_buy_amount']
            if tool_stock <= 0:
                messagebox.showinfo(title="notification",message=f"The {tool_name} has been out of stock.")
                input_data = {"tool_name": tool_name}
                r = requests.delete(f'http://127.0.0.1:8000/system/wishlist/delete_item/', json=input_data)
                print(r, r.json())

            elif tool_stock < amount:
                messagebox.showinfo(title="notification",message=f"The {tool_name}'s stock has been updated.")
                input_data = {"tool_name": self.tool_name, "quantity": tool_stock}
                r = requests.put(f'http://127.0.0.1:8000/system/wishlist/', json=input_data)
                print(r, r.json())

        r = requests.post(f'http://127.0.0.1:8000/system/wishlist/send_to_cart')
        print(r, r.json())
        self.update_data()

    def update_data(self): 
        if self.total is not None:
            self.destroy_widget()
        self.widget.destroy()
        self.get_wishlist_data()
        #self.get_info_in_list()
        self.show_item_widget()
        self.show_total_price_widget()

    def show_page(self):
        self.update_data()
        self.pack(fill=tk.BOTH, expand=1)

    def create_normal_widget(self):
        self.widget = tk.Label(self,text="")
        self.widget.pack()

        self.clear_wishlist_button = tk.Button(self,text="clear wishlist",command=self.clear_wishlist)
        self.clear_wishlist_button.place(x=800, y=50)

        self.tool_name_label = tk.Label(self,text="tool name", font=("Helvetica", 16)).place(x = 20, y = 70)
        self.tool_image_label = tk.Label(self,text="tool image", font=("Helvetica", 16)).place(x = 180, y = 70)
        self.tool_price_label = tk.Label(self,text="tool price", font=("Helvetica", 16)).place(x = 370, y = 70)
        self.tool_amoung_label = tk.Label(self,text="tool Quantity", font=("Helvetica", 16)).place(x = 520, y = 70)
        self.tool_total_price_label = tk.Label(self,text="total price", font=("Helvetica", 16)).place(x = 670, y = 70)


        self.back_to_home_button = tk.Button(self,text="home",command=self.Home)
        self.back_to_home_button.place(x=800, y=5)

        self.head_label = tk.Label(self, text="My Wishlist", font=("Helvetica", 18)).place(x = 20, y = 20)
        self.total_price_label = tk.Label(self, text="Total Price", font=("Helvetica", 18)).place(x = 20, y = 600)
        
    def show_total_price_widget(self):
        self.total = tk.Label(self, text=self.total_price, font=("Helvetica", 18))
        self.total.place(x = 170, y = 600)

    def show_item_widget(self):
        self.image_list = []
        for i in range(4): 
            for j in range(5): 
                self.widget = tk.Label(self, text="                        ", font=("Helvetica", 12))
                self.widget.place(x = 20+160*j,y = 120+120*i)
        for i,list_component in enumerate(self.list_tool) :
            for j,component in enumerate(list_component) : 
                if j != 1:
                    self.widget= tk.Label(self, text=component, font=("Helvetica", 12))
                    self.widget.place(x = 20+160*j,y = 120+120*i)
                else:
                    self.image = self.get_image(component, 100, 100)
                    self.image_list.append(self.image)
                    
        for item in range(len(self.image_list)):
            self.widget= tk.Label(self, image = self.image_list[item])
            self.widget.place(x = 180,y = 120+120*item)

    def destroy_widget(self):
        self.total.destroy()

    def get_wishlist_data(self):
        r = requests.get(f'http://127.0.0.1:8000/system/wishlist/')
        self.in_wishlist = r.json()['_wish_product'] # got list // dict
        self.get_info_in_list()

        self.total_price = r.json()['_total_price']

    def clear_wishlist(self):
        requests.delete(f'http://127.0.0.1:8000/system/wishlist/delete_wishlist/')
        self.widget.destroy()
        for i in range(4): 
            for j in range(5): 
                self.widget = tk.Label(self, text="                        ", font=("Helvetica", 12))
                self.widget.place(x = 20+160*j,y = 120+120*i)
        self.update_data()

    def get_info_in_list(self):
        self.list_tool = []
        for item in range(len(self.in_wishlist)):
            list_components= []
            self.item_info = self.in_wishlist[item]
            self.get_tool_info = self.item_info['_tool']

            tool_name = self.get_tool_info['_name']
            amount = self.item_info['_buy_amount']
            tool_stock = self.get_tool_info['_amount']

            # require data
            self.tool_name = tool_name      
            self.tool_image = self.get_tool_info['_image']
            self.total_price = self.item_info['_items_price'] 
            self.amount = amount
            self.tool_price = self.get_tool_info['_price']

            list_components.append(self.tool_name) 
            list_components.append(self.tool_image[0])  
            list_components.append(self.tool_price) 
            list_components.append(self.amount) 
            list_components.append(self.total_price)
            self.list_tool.append(list_components)

    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)

    def Home(self):  
        self.master.show_home()