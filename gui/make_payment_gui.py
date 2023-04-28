import tkinter as tk
import requests, json
from make_review import MakeReview
import io
import urllib.request 
from PIL import Image, ImageTk 

class MakePayment(tk.Frame): 

    def __init__(self,master=None): 
        super().__init__(master)
        self.create_widget()
    
    def create_widget(self): 
        self.back_button = tk.Button(self,text="back",command=self.back)
        self.back_button.pack()
        self.back_button.place(x=20,y=500)
    
    def back(self):
        self.master.show_cart()