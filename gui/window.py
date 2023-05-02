import sys 
sys.path.append('./class_object/')  
sys.path.append('./')
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from login_gui import LoginPage, SignupPage
from make_review import MakeReview
from search_gui import SearchPage
from PIL import Image, ImageTk  
from Tool_gui import Tool_GUI
from cart_gui import CartGui
from tool_widget import ToolWidget
from admin_gui import AdminGui
import random
import requests
from profile_page import ProfileGUI
# # from tkinter import messagebox
# # from tkinter import ttk
import io
import urllib.request

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x700")
        self.resizable(False, False)
        self.title("Login/Search App")
        self.photo = None 

        # Create the menu bar
        menubar = tk.Menu(self)
        accountbar = tk.Menu(self)
        self.config(menu=menubar)
        self.first_name = ''
        self.authority = 'guest'

        # Create the Pages menu with commands to switch to each page
        pages_menu = tk.Menu(menubar, tearoff=0)
        pages_menu.add_command(label="Home", command=self.show_home)
        pages_menu.add_command(label="Search", command=self.show_search)
        pages_menu.add_command(label="Login", command=self.show_login)
        pages_menu.add_command(label="Sign Up", command=self.show_sign_up)
        # pages_menu.add_command(label="Create Address",command=self.show_create_address)
        # pages_menu.add_command(label="Edit and delete address",command=self.show_edit_address)
        pages_menu.add_command(label="Profile",command=self.show_profile)
        menubar.add_cascade(label="Pages", menu=pages_menu)


        # Create the account bar

        # Create the pages
        self.home_page = tk.Frame(self)
        tk.Label(self.home_page, text="This is the Home page").pack()
        tk.Label(self.home_page, text="Recommended Tools", font=("Helvetica", 30)).place(x=260, y=280)
        self.name = tk.Label(self.home_page, text=self.first_name)


        self.admin_page = AdminGui(self)
        self.cart_page = CartGui(self)
        self.search_page = SearchPage(link='category', search_type='Category', master=self)
        self.search_page.add_new_search(link='category/tools', search_type='Tool')
        self.login_page = LoginPage(self)
        self.sign_up_page = SignupPage(self)
        
    
        self.profile_page = ProfileGUI(self)
      


        self.make_payment_page = self.cart_page.makepayment
        self.managetool_page = self.admin_page.managetool
        self.managecoupon_page = self.admin_page.managecoupon
        self.managewholesale_page = self.admin_page.managewholesale
        self.create_cart_button()
        self.create_admin_button()
        self.create_refresh_button()
        self.tool_data = self.get_tool_data()
        self.tool_widgets = [ ]
        self.make_tool_widget(self.get_tool_data())
        self.current_tool_widget = [ ]
        self.current_home_widget = [self.cart_button,self.name,self.refresh_button] 
        self.random_tool_list = self.random_tool_to_show()

        self.tool_page = self.tool_widgets[0].tool_page
        self.make_review_page = self.tool_widgets[0].make_review_page

        self.image1 = self.get_image("https://cdn-icons-png.flaticon.com/512/649/649438.png?w=740&t=st=1682418903~exp=1682419503~hmac=9f666ca6e05c302741f8531345f3fc24865b0a54bd5eed15bd969a63e2e7f431", 150, 150)
        self.image1_label = Label(self.home_page, image = self.image1)
        Label(self.home_page, image=self.image1).place(x=80, y=50)
        self.label1 = Label(self.home_page, text="World wild shipping", font=("Helvetica", 12))
        self.label1.place(x=90, y=210)

        self.image2 = self.get_image("https://cdn-icons-png.flaticon.com/512/1230/1230503.png?w=740&t=st=1682419235~exp=1682419835~hmac=a50c1749ef9f3af3a3c39e5189051db83e07480458eebba875580c16f831a4c7", 150, 150)
        self.image2_label = Label(self.home_page, image = self.image2)
        Label(self.home_page, image=self.image2).place(x=280, y=50)
        Label(self.home_page, text="30 days return", font=("Helvetica", 12)).place(x=300, y=210)
        # Show the initial page

        self.image3 = self.get_image("https://cdn-icons-png.flaticon.com/512/649/649451.png?w=740&t=st=1682420117~exp=1682420717~hmac=9c97285763503fd2b3f9f47313bd2bf611bd598a64b4898c679bf95a2164bffc", 150, 150)
        self.image3_label = Label(self.home_page, image = self.image3)
        Label(self.home_page, image=self.image3).place(x=480, y=50)
        Label(self.home_page, text="wholesale price", font=("Helvetica", 12)).place(x=510, y=210)
        # Show the initial page

        self.image4 = self.get_image("https://cdn-icons-png.flaticon.com/512/1175/1175149.png?w=740&t=st=1682420264~exp=1682420864~hmac=07b81a259160ed6af3e780639e51443439a980e4b926e81ed552e07f0a653679", 150, 150)
        self.image4_label = Label(self.home_page, image = self.image4)
        Label(self.home_page, image=self.image4).place(x=680, y=50)
        Label(self.home_page, text="wholesale price", font=("Helvetica", 12)).place(x=720, y=210)
        # Show the initial page

        self.show_home()

   

    def make_tool_widget(self, dict_json):
        # print(self.first_name)
        for key, value in dict_json.items():
            name = key
            image = self.get_image(value.get('_image')[0],150,150) 
            widget = ToolWidget(name=name, image=image, master=self)
            widget.set_button_command(command=lambda w=widget:self.to_tool_page(w))
            self.tool_widgets.append(widget)
        
    def create_cart_button(self): 
        self.cart_button = tk.Button(self,text="cart",command=self.show_cart)
        self.cart_button.pack()  
        self.cart_button.place(x =600,y = 600)
    def create_refresh_button(self): 
        self.refresh_button = tk.Button(self,text="refresh",command=self.show_home) 
        self.refresh_button.pack() 
        self.refresh_button.place(x=400,y=600)
    def create_admin_button(self):
        self.admin_button = tk.Button(self,text="admin",command=self.show_admin)
        self.admin_button.pack()  
        self.admin_button.place(x =500,y = 600)


    def get_tool_data(self):
        return requests.get(f'http://127.0.0.1:8000/system/category/tools?search=').json()
    
    def first_name_user(self): 
        user = requests.get("http://127.0.0.1:8000/me").json() 
        for key in user.keys(): 
            if key == 'username': 
                username = user["username"]["user"]  
                # print(user) 
                self.authority = user['authority']
                firstname = requests.get(f'http://127.0.0.1:8000/user/?username={username}').json()
                return firstname
        return {"first_name":"guest"}
    def random_tool_to_show(self):
        random_tool = []
        while len(random_tool) < 4:
            tool = self.tool_widgets[random.randint(0, len(self.tool_widgets)-1)]
            if tool not in random_tool:
                random_tool.append(tool)
        return random_tool

    def show_tool_widget(self, widgets_list, start_x=100, start_y=350, page=None):
        if page is None:
            page=self.home_page

        self.hide_tool_widget()
        self.current_tool_widget = widgets_list
        row = 0
        for i, widget in enumerate(self.current_tool_widget):
            widget.button.pack(in_=page)
            widget.description.pack(in_=page)
            row = 400 * (i//4)
            widget.set_coords(start_x+(i*200), start_y+row)
    def show_home_widget(self):
        self.delete_name()
        self.name = tk.Label(self.home_page, text=self.first_name)
        self.name.pack() 
        self.name.place(x=800,y=20)
        self.cart_button.pack(in_= self.home_page)
        self.admin_button.pack(in_= self.home_page) 
        self.refresh_button.pack(in_= self.home_page)
        

    def hide_home_widget(self): 
        self.name.pack(in_=None)
        self.cart_button.pack(in_=None)
        self.admin_button.pack(in_=None)
        self.refresh_button.pack(in_= None)

    def delete_name(self):
        self.name.destroy()

    def hide_tool_widget(self):
        for widget in self.current_tool_widget:
            widget.unpack()
        self.current_tool_widget = []

    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)
    
    def to_tool_page(self, widget):
        self.make_review_page = widget.make_review_page
        self.tool_page = widget.tool_page
        self.tool_page.get_tool_details()
        self.show_tool()

    def show_home(self):  
        self.first_name = self.first_name_user()
        self.first_name = self.first_name["first_name"]
        self.show_home_widget()
        self.make_tool_widget(self.get_tool_data())
        self.tool_page.pack_forget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        self.admin_page.pack_forget()
        self.cart_page.pack_forget()
        self.profile_page.pack_forget()
        self.managewholesale_page.pack_forget()
        self.home_page.pack(fill=tk.BOTH, expand=1)
        self.make_payment_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.show_tool_widget(self.random_tool_list, start_x=75, start_y=350)

        
    def show_review(self): 
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        self.login_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.profile_page.pack_forget()
        self.managewholesale_page.pack_forget()
        self.make_review_page.pack(fill=tk.BOTH, expand=1)

    def show_profile(self):

        self.make_review_page.pack_forget()
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        self.login_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.managewholesale_page.pack_forget()
        self.profile_page.show_profile()
        self.profile_page.pack(fill=tk.BOTH,expand=1)
    
    def show_search(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.login_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.managewholesale_page.pack_forget()
        self.profile_page.pack_forget()
        self.search_page.pack(fill=tk.BOTH, expand=1)
        self.make_review_page.pack_forget()

    def show_login(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.profile_page.pack_forget()
        self.managewholesale_page.pack_forget()
        self.login_page.pack(fill=tk.BOTH, expand=1)

    def show_tool(self): 
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.login_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.profile_page.pack_forget()
        self.managewholesale_page.pack_forget()
        self.tool_page.pack(fill=tk.BOTH, expand=1)

    def show_sign_up(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.cart_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.admin_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.managewholesale_page.pack_forget()
        self.sign_up_page.pack(fill=tk.BOTH, expand=1)
    
    def show_cart(self):
        if self.authority == "admin": 
            self.show_home()
            messagebox.showinfo(title="notification", message="admin have no cart")
        else : 

            self.hide_home_widget()
            self.sign_up_page.pack_forget()
            self.tool_page.pack_forget()
            self.home_page.pack_forget()
            self.hide_tool_widget()
            self.search_page.pack_forget()
            self.login_page.pack_forget()
            self.make_review_page.pack_forget()
            self.make_payment_page.pack_forget()
            self.admin_page.pack_forget()
            self.managetool_page.pack_forget()
            self.managecoupon_page.pack_forget() 
            self.managewholesale_page.pack_forget()
            self.cart_page.update_data()
            self.cart_page.pack(fill=tk.BOTH, expand=1)
    
    def show_admin(self): 
        if self.authority == "admin":
            self.cart_page.pack_forget()
            self.hide_home_widget()
            self.sign_up_page.pack_forget()
            self.tool_page.pack_forget()
            self.home_page.pack_forget()
            self.hide_tool_widget()
            self.search_page.pack_forget()
            self.login_page.pack_forget()
            self.make_review_page.pack_forget()
            self.make_payment_page.pack_forget()
            self.managetool_page.pack_forget()
            self.managecoupon_page.pack_forget() 
            self.managewholesale_page.pack_forget()
            self.admin_page.pack(fill=tk.BOTH, expand=1)
        else : 
            self.show_home()
            messagebox.showinfo(title="notification", message="you must login as a admin first")
    
    def show_payment(self):
        self.cart_page.pack_forget()
        self.hide_home_widget()
        self.sign_up_page.pack_forget()
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.admin_page.pack_forget()
        self.make_review_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack_forget() 
        self.managewholesale_page.pack_forget()
        self.make_payment_page.pack(fill=tk.BOTH, expand=1) 

    def show_managetool(self): 
        self.cart_page.pack_forget()
        self.hide_home_widget()
        self.sign_up_page.pack_forget()
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.admin_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget() 
        self.managecoupon_page.pack_forget() 
        self.managewholesale_page.pack_forget()
        self.managetool_page.pack(fill=tk.BOTH, expand=1)

    def show_managecoupon(self): 
        self.cart_page.pack_forget()
        self.hide_home_widget()
        self.sign_up_page.pack_forget()
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.admin_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.managetool_page.pack_forget()
        self.managecoupon_page.pack(fill=tk.BOTH, expand=1)
        self.profile_page.pack_forget()
        self.managewholesale_page.pack_forget()
    
    def show_managewholesale(self): 
        self.cart_page.pack_forget()
        self.hide_home_widget()
        self.sign_up_page.pack_forget()
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        self.hide_tool_widget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.admin_page.pack_forget()
        self.make_review_page.pack_forget()
        self.make_payment_page.pack_forget()
        self.managetool_page.pack_forget()
        self.profile_page.pack_forget()
        self.managecoupon_page.pack_forget()
        self.managewholesale_page.pack(fill=tk.BOTH, expand=1)
if __name__ == "__main__":
    app = Window()
    app.mainloop()