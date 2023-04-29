import tkinter as tk
import requests, json 
import io
import urllib.request 
from PIL import Image, ImageTk 

class AdminGui(tk.Frame): 
    def __init__(self,master):
        super().__init__(master)
        self.master = master 

    def create_widget(self): 
        self.back_to_home_button = tk.Button(self,text="home",command=self.Home)
        self.back_to_home_button.pack() 
        self.back_to_home_button.place(x=800, y=5) 

    def Home(self): 
        self.master.show_home()