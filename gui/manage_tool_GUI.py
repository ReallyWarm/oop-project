from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import requests
import json

class add_tool:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("add tool")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        self.root.configure(background="#f7f7f7")
        self.root.config(cursor="hand2")

        Label(text="add tool", fg="#333", font=("Helvetica", 18, "bold")).pack(pady=20)

        Label(text="product code:", font=("Helvetica", 12)).place(x=50, y=60)
        self.ent1 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent1.place(x=50, y=90, width=400)

        Label(text="tool_name:", font=("Helvetica", 12)).place(x=50, y=120)
        self.ent2 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID) 
        self.ent2.place(x=50, y=150, width=400)

        Label(text="tool_description:", font=("Helvetica", 12)).place(x=50, y=180)
        self.ent3 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent3.place(x=50, y=210, width=400)

        Label(text="tool_brand:", font=("Helvetica", 12)).place(x=50, y=240)
        self.ent4 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent4.place(x=50, y=270, width=400)

        Label(text="tool_amount:", font=("Helvetica", 12)).place(x=50, y=300)
        self.ent5 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent5.place(x=50, y=330, width=400)

        Label(text="tool_image:", font=("Helvetica", 12)).place(x=50, y=360)
        self.ent6 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent6.place(x=50, y=390, width=400)

        Label(text="tool_price:", font=("Helvetica", 12)).place(x=50, y=420)
        self.ent7 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent7.place(x=50, y=450, width=400)

        Label(text="tool_category:", font=("Helvetica", 12)).place(x=50, y=480)
        self.ent8 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)
        self.ent8.place(x=50, y=510, width=400)

        Button(text="Submit new tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.add_tool).place(x=180, y=550)

        self.root.mainloop()

    def add_tool(self):
        
        if self.ent1.get() is not '' and self.ent2.get() is not '' and  self.ent3.get() is not '' and  self.ent4.get() \
            is not '' and  self.ent5.get() is not '' and  self.ent6.get() is not '' and  self.ent7.get() is not '' \
            and  self.ent8.get() is not '':
        
            input_data = {
                "product_code": self.ent1.get(),
	            "tool_name":self.ent2.get(),
	            "tool_description": self.ent3.get(),
	            "tool_brand": self.ent4.get(),
	            "tool_amount": self.ent5.get(),
	            "tool_image": self.ent6.get(),
	            "tool_price": self.ent7.get(),
	            "tool_category": self.ent8.get()
            }

            r = requests.post("http://127.0.0.1:8000/system/category/tools/", json=input_data)
            respon = json.loads(r.text)
            if respon == {'ADD Tool': "ADD Tool successfully added"}:
                messagebox.showinfo(title="ADD_TOOL Response", message="ADD Tool successfully added")
            elif respon == {'ADD Tool': "already have this tool in system"}:
                messagebox.showinfo(title="ADD_TOOL Response", message="already have this tool in system")
            print(respon)
        else :
            messagebox.showinfo(title="ADD_TOOL Response", message="Need more information")
add_tool()
