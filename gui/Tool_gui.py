import tkinter as tk
import requests, json
from make_review import MakeReview
class Tool_GUI(tk.Frame) : 

    def __init__(self,tool,master = None): 
        super().__init__(master) 
        self.tool = tool
        self.master = master 
        self.create_widget()
    def create_widget(self): 
        self.test_label = tk.Label(self,text = self.tool.name) 
        self.test_label.pack()
        self.back_button = tk.Button(self,text="home",command=self.Home)
        self.back_button.pack()
        self.back_button = tk.Button(self,text="review",command=self.show_make_review)
        self.back_button.pack()
    def Home(self):  
        self.master.show_home() 
        
    def show_make_review(self): 
        self.master.show_review()
