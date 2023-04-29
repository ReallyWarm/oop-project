import tkinter as tk
import requests, json
from make_review import MakeReview
import io
import urllib.request 
from PIL import Image, ImageTk
from make_payment_gui import MakePayment
class CartGui(tk.Frame): 

    def __init__(self,master): 
        super().__init__(master) 
        self.list_tool =[]
        self.master = master
        self.total = 0
        self.shipping = 0
        self.final_cost = 0
        self.get_cart_data()
        self.create_normal_widget()
        self.show_total_cart_widget()
        # self.update_data()
        self.makepayment = MakePayment(master=self.master,submaster=self) 
        self.makepayment_button = tk.Button(self,text="Make Payment",command=self.make_payment)
        self.makepayment_button.pack()
        self.makepayment_button.place(x=660,y=500)
    def make_payment(self): 
        self.master.show_payment()
        self.makepayment.final_price = self.final_price
        self.makepayment.final_show = self.final_price
    def update_data(self): 
        
        self.destroy_widget()
        self.get_cart_data()
        #self.get_info_in_list()
        self.show_item_widget()
        self.show_total_cart_widget()

    def create_normal_widget(self): 
        self.get = tk.Button(self,text="update cart",command=self.update_data)
        self.get.pack() 
        self.get.place(x=800, y=50)

        self.clear_cart_button = tk.Button(self,text="clear cart",command=self.clear_cart)
        self.clear_cart_button.pack()
        self.clear_cart_button.place(x=800, y=100)

        self.tool_name_label = tk.Label(self,text="tool name", font=("Helvetica", 16)).place(x = 20, y = 70)
        self.tool_image_label = tk.Label(self,text="tool image", font=("Helvetica", 16)).place(x = 180, y = 70)
        self.tool_price_label = tk.Label(self,text="tool price", font=("Helvetica", 16)).place(x = 370, y = 70)
        self.tool_amoung_label = tk.Label(self,text="tool Quantity", font=("Helvetica", 16)).place(x = 520, y = 70)
        self.tool_total_price_label = tk.Label(self,text="total price", font=("Helvetica", 16)).place(x = 670, y = 70)


        self.back_to_home_button = tk.Button(self,text="home",command=self.Home)
        self.back_to_home_button.pack() 
        self.back_to_home_button.place(x=800, y=5)

        self.head_label = tk.Label(self, text="My Cart", font=("Helvetica", 18)).place(x = 20, y = 20)
        self.total_price_label = tk.Label(self, text="Total Price", font=("Helvetica", 18)).place(x = 20, y = 600)
        self.shipping_cost_label = tk.Label(self, text="Shipping Cost", font=("Helvetica", 18)).place(x = 320, y = 600)
        self.final_price_label = tk.Label(self, text="Final Price", font=("Helvetica", 18)).place(x = 620, y = 600)
        
    def show_total_cart_widget(self):
        self.total = tk.Label(self, text=self.total_price, font=("Helvetica", 18))
        self.total.pack()
        self.total.place(x = 170, y = 600)
        self.shipping = tk.Label(self, text=self.shipping_cost, font=("Helvetica", 18))
        self.shipping.pack()
        self.shipping.place(x = 470, y = 600)
        self.final_cost = tk.Label(self, text=self.final_price, font=("Helvetica", 18))
        self.final_cost.pack()
        self.final_cost.place(x = 770, y = 600)

    def show_item_widget(self):
        self.image_list = []
        for i in range(4): 
            for j in range(5): 
                self.widget = tk.Label(self, text="                        ", font=("Helvetica", 12))
                self.widget.pack() 
                self.widget.place(x = 20+160*j,y = 120+120*i)
        for i,list_component in enumerate(self.list_tool) :
            for j,component in enumerate(list_component) : 
                if j != 1:
                    self.widget= tk.Label(self, text=component, font=("Helvetica", 12))
                    self.widget.pack() 
                    self.widget.place(x = 20+160*j,y = 120+120*i)
                else:
                    self.image = self.get_image(component, 100, 100)
                    self.image_list.append(self.image)
                    
        for item in range(len(self.image_list)):
            self.widget= tk.Label(self, image = self.image_list[item])
            self.widget.pack()
            self.widget.place(x = 180,y = 120+120*item)

    def destroy_widget(self):
        #print("destroyed")
        self.total.destroy()
        self.shipping.destroy()
        self.final_cost.destroy()
        

    def get_cart_data(self):
        r = requests.get(f'http://127.0.0.1:8000/system/shopping_cart/')
        # print(r.json())
        self.in_cart = r.json()['_cart'] # got list // dict
        # self.item_info = self.in_cart[0] # got dict tool with info
        self.get_info_in_list()
        self.total_price = r.json()['_total_price']
        self.shipping_cost = r.json()['_shipping_price']
        self.final_price = r.json()['_final_price']
        #print(self.in_cart)

    def clear_cart(self):
        requests.delete(f'http://127.0.0.1:8000/system/shopping_cart/delete_cart/')
        self.widget.destroy()
        for i in range(4): 
            for j in range(5): 
                self.widget = tk.Label(self, text="                        ", font=("Helvetica", 12))
                self.widget.pack() 
                self.widget.place(x = 20+160*j,y = 120+120*i)
        self.update_data()
        # canvas = tk.Canvas()
        # canvas.pack()
        # self.invinsble_square = canvas.create_rectangle(50, 50, 600, 600, fill="white")

    def get_info_in_list(self):
        self.list_tool = []
        for item in range(len(self.in_cart)):
            print(item) 
            list_components= []
            self.item_info = self.in_cart[item]
            self.get_tool_info = self.item_info['_tool']

            # require data
            self.tool_name = self.get_tool_info['_name']
            #self.item_tool_name = tk.Label(self, text=self.tool_name, font=("Helvetica", 12))
            
            self.tool_image = self.get_tool_info['_image']
            # self.item_tool_image = tk.Label(self, image=self.tool_image[0])

            self.total_price = self.item_info['_items_price']
            #self.item_total_price = tk.Label(self, text=self.total_price, font=("Helvetica", 12)) 

            self.amount = self.item_info['_buy_amount']
            #self.item_quantity = tk.Label(self, text=self.amount, font=("Helvetica", 12))
            
            self.tool_price = self.get_tool_info['_price']
            #self.item_tool_price = tk.Label(self, text=self.tool_price, font=("Helvetica", 12))

            list_components.append(self.tool_name) 
            list_components.append(self.tool_image[0])  
            list_components.append(self.tool_price) 
            list_components.append(self.amount) 
            list_components.append(self.total_price)
            self.list_tool.append(list_components)

        # print(self.list_tool)
            
        

    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)

    def Home(self):  
        self.master.show_home()