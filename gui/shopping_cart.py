import tkinter as tk
import requests, json
import io
import urllib.request 
from PIL import Image, ImageTk

class ShoppingCart(tk.Frame):
        
    def __init__(self,name,master = None): 
        super().__init__(master) 
        self.master = master 
        self.name = name

    def get_cart_data(self):
        r = requests.get(f'http://127.0.0.1:8000/system/shopping_cart/')
        print(r.json())

    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)
    