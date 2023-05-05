import tkinter as tk
import requests, json
from tkinter import messagebox 

class ManagetypeOfTool(tk.Frame): 
    def __init__(self,master): 
        super().__init__(master) 
        self.master = master 
        self.create_widget()
    def create_widget(self): 
        self.back_to_home_button = tk.Button(self,text="back",command=self.Back)
        self.back_to_home_button.place(x=800, y=5)

        self.text1 = tk.Label(self, text="add type of tool", fg="#333", font=("Helvetica", 18, "bold"))
        self.text1.pack()
        self.text1.place(x=200)

        self.text1 =  tk.Label(self, text="add type of tool:", font=("Helvetica", 12))
        self.text1.pack()
        self.text1.place(x=50, y=60)
        self.ent1 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent1.place(x=50, y=90, width=400)

        self.text2 =  tk.Label(self, text="add subtype of tool:", font=("Helvetica", 12))
        self.text2.pack()
        self.text2.place(x=50, y=120)
        self.ent2 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID) 
        self.ent2.place(x=50, y=150, width=400)

        self.button = tk.Button(self, text="Submit new type of tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.add_new_type)
        self.button.pack()
        self.button.place(x=180, y=450)

        self.button = tk.Button(self, text="Submit new subtype of tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.add_new_subtype)
        self.button.pack()
        self.button.place(x=180, y=550)

    def add_new_type(self):
        if self.ent1.get() != '':
        
            input_data = {
                "type_of_tool": self.ent1.get()
            }

            r = requests.post("http://127.0.0.1:8000/system/category/typeoftools/", json=input_data)
            respon = json.loads(r.text)
            if respon =={"ADD TypeOfTool": "Already have a type of tool"}:
                tk.messagebox.showinfo(title="ADD TypeOfTool", message="Already have a type of tool")
            elif respon =={"ADD TypeOfTool": "Add type of tool successfully"}:
                tk.messagebox.showinfo(title="ADD TypeOfTool", message="Add type of tool successfully")
        else :
            tk.messagebox.showinfo(title="Response", message="Need more information")

    def add_new_subtype(self):
        if self.ent1.get() != '' and self.ent2.get():
        
            input_data = {
                "type_of_tool": self.ent1.get(),
	            "subtype_if_tool":self.ent2.get(),
            }

            r = requests.post("http://127.0.0.1:8000/system/category/subtypeoftools/", json=input_data)
            respon = json.loads(r.text)
            if respon == {'ADD SubtypeOfTool': "Already have a subtype of tool"}:
                tk.messagebox.showinfo(title="ADD SubtypeOfTool", message="Already have a subtype of tool")
                self.master.make_tool_widget(self.ent2.get(), self.ent6.get())
            elif respon =={'ADD SubtypeOfTool':"Add subtype of tool successfully"}:
                tk.messagebox.showinfo(title="ADD SubtypeOfTool", message="Add subtype of tool successfully")
            elif respon =={"ADD SubtypeOfTool":"do not have this type of tool"}:
                tk.messagebox.showinfo(title="ADD SubtypeOfTool", message="do not have this type of tool")
        else :
            tk.messagebox.showinfo(title="ADD_TOOL Response", message="Need more information")


    def Back(self): 
        self.master.show_admin()