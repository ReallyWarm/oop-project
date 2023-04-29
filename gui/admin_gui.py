import tkinter as tk
import requests, json 
import io
import urllib.request  
from manage_tool import ManageTool 
from manage_coupon_gui import ManageCoupon
from PIL import Image, ImageTk 

class AdminGui(tk.Frame): 
    def __init__(self,master):
        super().__init__(master)
        self.master = master 
        self.create_widget()
        self.managetool = ManageTool(master)
        self.managecoupon = ManageCoupon(master)

    def create_widget(self): 
        self.back_to_home_button = tk.Button(self,text="home",command=self.Home)
        self.back_to_home_button.pack() 
        self.back_to_home_button.place(x=800, y=5)   
        self.managetool_label = tk.Button(self,text="manage tool",command=self.to_managetool)
        self.managetool_label.pack() 
        self.managetool_label.place(x=600, y=5) 
        self.managecoupon_label = tk.Button(self,text="manage coupon",command=self.to_managecoupon)
        self.managecoupon_label.pack() 
        self.managecoupon_label.place(x=400, y=5) 

    def to_managetool(self): 
        self.master.show_managetool()

    def to_managecoupon(self): 
        self.master.show_managecoupon()
        # self.managecoupon.create_widget()
        
    def Home(self): 
        self.master.show_home()