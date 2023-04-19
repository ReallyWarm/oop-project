from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import requests
import json

class make_review_GUI:
    def __init__(self, user, tool):
        self.user = user
        self.tool = tool
        self.root = Tk()
        self.root.title("Make Review")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="white")
        self.root.config(cursor="hand2")
        Label(text="write review").pack(anchor='center')
        self.ent1 = Entry(self.root)
        self.ent1.place(x = 50, y= 100)
        self.ent2 = Text(width= 20, height= 10)
        self.ent2.place(x = 50, y=200)
        rating = StringVar()
        self.ent3 = ttk.Combobox(self.root, width=30, textvariable=rating)
        self.ent3['value'] = (0,1,2,3,4,5)
        self.ent3.place(x = 50, y=400)
        self.ent3.current()
        Button(text="sent review", command=self.send_review).place(x=300, y=400)
        self.root.mainloop()

    def send_review(self):
        data = {
	            "User":self.user,
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
            messagebox.showinfo(title="review respon",message="your review is added!")
        print(respon)

make_review_GUI('NorNor','Testing drill')