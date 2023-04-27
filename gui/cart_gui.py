import tkinter as tk 

class CartGui(tk.Frame): 

    def __init__(self,master): 
        super().__init__(master) 
        self.master = master
        self.create_widget()
    def create_widget(self): 
        self.back_button = tk.Button(self,text="home",command=self.Home)
        self.back_button.pack()

    def Home(self):  
        self.master.show_home() 