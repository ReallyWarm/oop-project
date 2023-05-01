import tkinter as tk 
from tkinter import ttk  
from tkinter import messagebox
from datetime import datetime 
import requests,json
class MakeReview(tk.Frame): 
    def __init__(self,user,tool,master): 
        super().__init__(master)
        self.master = master 
        self.user = user  
        self.tool = tool
        self.create_widget()
    def create_widget(self): 
        # Create a label for the heading
        tk.Label(self,text="Write Review", fg="#333", font=("Helvetica", 18, "bold")).pack(pady=20)
        
        # Create a label for the review title
        tk.Label(self,text="Title:", font=("Helvetica", 12)).place(x=50, y=60)
        self.ent1 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)  # Set border properties
        self.ent1.place(x=50, y=90, width=400)
        
        # Create a label for the review comment
        tk.Label(self,text="Comment:", font=("Helvetica", 12)).place(x=50, y=130)
        self.ent2 = tk.Text(self,width=40, height=10, font=("Helvetica", 12), bd=1, relief=tk.SOLID)  # Set border properties
        self.ent2.place(x=50, y=160)
        
        # Create a label for the review rating
        tk.Label(self,text="Rating:", font=("Helvetica", 12)).place(x=50, y=400)
        rating = tk.StringVar(self)
        self.ent3 = ttk.Combobox(self, width=30, textvariable=rating, font=("Helvetica", 12))
        self.ent3['value'] = (0,1,2,3,4,5)
        self.ent3.place(x=50, y=440)
        self.ent3.current()
        
        # Create a button to send the review
        tk.Button(self,text="Submit Review", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.send_review).place(x=180, y=500)
    def send_review(self): 
        data = {
                "User":self.master.first_name,
                "tool":self.tool,
                "head_review":self.ent1.get(),
                "comment":self.ent2.get("1.0","end-1c"),
                "rating":self.ent3.get(),
                "date_of_review":datetime.now().strftime("%d-%m-%Y")
            }
        
        # date = data["date_of_review"]
        # print(date)
        r = requests.post("http://127.0.0.1:8000/tool/make_review",json = data)
        respon = json.loads(r.text)
        if respon == {'data': 'A new review is added!'}:
            messagebox.showinfo(title="Review Response", message="Your review has been added!")
        else:
            messagebox.showinfo(title="Review Response", message="Yor must login first")
        # print(respon) 
        # print(self.master.first_name)