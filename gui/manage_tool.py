import tkinter as tk
import requests, json
from make_review import MakeReview
from tkinter import ttk
from tkinter import messagebox
import io
import urllib.request 
from PIL import Image, ImageTk 
from datetime import datetime

class ManageTool(tk.Frame): 
    def __init__(self,master): 
        super().__init__(master)
        self.todo_dropdown()
        self.back_button()
        self.show_now = 0
        # self.status = "empty"
        # self.create_widget()

    def todo_dropdown(self):
        self.choice = tk.StringVar(self, value="chose to do")
        self.combo = ttk.Combobox(self, textvariable=self.choice)
        self.combo["values"] = ("add tool", "manage tool", "delete tool")
        self.combo.place(x = 500, y = 50)
        self.bt1=tk.Button(self, text="ส่งข้อมูล", command=self.show_selected)
        self.bt1.place(x = 700, y = 50)

    def show_selected(self):
        print(self.choice.get())
        if self.show_now == 0:
            if self.choice.get() == "add tool":
                self.create_add_tool_widget()
                self.show_now = 1
            elif self.choice.get() == "manage tool":
                self.search_to_modify()
                self.show_now = 2
            elif self.choice.get() == "delete tool":
                self.search_to_delete()
                self.show_now = 3

        else:
            if self.choice.get() == "manage tool":
                self.delete_widget()
                self.search_to_modify()
                self.show_now = 2
            elif self.choice.get() == "delete tool":
                self.delete_widget()
                self.search_to_delete()
                self.show_now = 3
            elif self.choice.get() == "add tool":
                self.delete_widget()
                self.create_add_tool_widget()
                self.show_now = 1



    def back_button(self):
        self.back_to_home_button = tk.Button(self,text="back",command=self.Back)
        self.back_to_home_button.pack() 
        self.back_to_home_button.place(x=800, y=5)

# ------------------------------------------------------------ add tool -----------------------------------------------------------------

    def create_add_tool_widget(self):
        self.text1 = tk.Label(self, text="add tool", fg="#333", font=("Helvetica", 18, "bold"))
        self.text1.pack()
        self.text1.place(x=200)

        self.text2 =  tk.Label(self, text="product code:", font=("Helvetica", 12))
        self.text2.pack()
        self.text2.place(x=50, y=60)
        self.ent1 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent1.place(x=50, y=90, width=400)

        self.text3 =  tk.Label(self, text="tool_name:", font=("Helvetica", 12))
        self.text3.pack()
        self.text3.place(x=50, y=120)
        self.ent2 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID) 
        self.ent2.place(x=50, y=150, width=400)

        self.text4 =  tk.Label(self, text="tool_description:", font=("Helvetica", 12))
        self.text4.pack()
        self.text4.place(x=50, y=180)
        self.ent3 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent3.place(x=50, y=210, width=400)

        self.text5 =  tk.Label(self, text="tool_brand:", font=("Helvetica", 12))
        self.text5.pack()
        self.text5.place(x=50, y=240)
        self.ent4 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent4.place(x=50, y=270, width=400)

        self.text6 =  tk.Label(self, text="tool_amount:", font=("Helvetica", 12))
        self.text6.pack()
        self.text6.place(x=50, y=300)
        self.ent5 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent5.place(x=50, y=330, width=400)

        self.text7 =  tk.Label(self, text="tool_image:", font=("Helvetica", 12))
        self.text7.pack()
        self.text7.place(x=50, y=360)
        self.ent6 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent6.place(x=50, y=390, width=400)

        self.text8 =  tk.Label(self, text="tool_price:", font=("Helvetica", 12))
        self.text8.pack()
        self.text8.place(x=50, y=420)
        self.ent7 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent7.place(x=50, y=450, width=400)

        self.text9 =  tk.Label(self, text="tool_category:", font=("Helvetica", 12))
        self.text9.pack()
        self.text9.place(x=50, y=480)
        self.ent8 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent8.place(x=50, y=510, width=400)

        self.button = tk.Button(self, text="Submit new tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.add_tool)
        self.button.pack()
        self.button.place(x=180, y=550)

    def add_tool(self):
        
        if self.ent1.get() != '' and self.ent2.get() != '' and  self.ent3.get() != '' and  self.ent4.get() \
            != '' and  self.ent5.get() != '' and  self.ent6.get() != '' and  self.ent7.get() != '' \
            and  self.ent8.get() != '':
        
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

            r = requests.post("http://127.0.0.1:8000/system/category/subtype/tools/", json=input_data)
            respon = json.loads(r.text)
            if respon == {'ADD Tool':"add tool successfully"}:
                tk.messagebox.showinfo(title="ADD_TOOL Response", message="ADD Tool successfully added")
                self.master.make_tool_widget(self.ent2.get(), self.ent6.get())
            elif respon =={'ADD Tool':"Already have this Tool"}:
                tk.messagebox.showinfo(title="ADD_TOOL Response", message="Already have this Tool")
            print(respon)
        else :
            tk.messagebox.showinfo(title="ADD_TOOL Response", message="Need more information")

    def delete_widget(self):
        self.text1.destroy()
        self.text2.destroy()
        self.text3.destroy()
        self.text4.destroy()
        self.text5.destroy()
        self.text8.destroy()
        self.text9.destroy()
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent7.destroy()
        self.ent8.destroy()
        self.button.destroy()

        if self.show_now == 1:
            self.text6.destroy()
            self.text7.destroy()        
            self.ent5.destroy()
            self.ent6.destroy()

        if self.show_now == 2 or self.show_now == 3:
            # if self.status == "writed":
            #     pass
            # else:
            self.search.destroy()
            self.search_ent.destroy()
            self.search_button.destroy()
        
        # self.status = "empty"

# ---------------------------------------------------------------- modify tool -------------------------------------------------------------

    def search_to_modify(self):
        self.text1 = tk.Label(self, text="manage tool", fg="#333", font=("Helvetica", 18, "bold"))
        self.text1.pack()
        self.text1.place(x=200)
        self.search =  tk.Label(self, text="search product:", font=("Helvetica", 12))
        self.search.pack()
        self.search.place(x=500 , y=100)
        self.search_ent = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.search_ent.pack()
        self.search_ent.place(x=500, y=200, width=400)
        self.search_button = tk.Button(self, text="Search", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.manage_tool_widget)
        self.search_button.pack()
        self.search_button.place(x=500, y=300)

    # for write again
    # def manage_tool_status_check(self):
    #     if self.status == "writed":
    #         self.delete_widget()
    #         self.manage_tool_widget()
    #     else:
    #         self.manage_tool_widget()

    def manage_tool_widget(self):
        self.input_name = self.search_ent.get()
        if ' ' in self.input_name : 
            self.input_name = self.input_name.replace(' ','%20')
        r = requests.get(f'http://127.0.0.1:8000/system/category/show_tools/?tool_name={self.input_name}')
        respon = json.loads(r.text)
        if respon == {'GET Tool':'Invalid Tool'}:
            tk.messagebox.showinfo(title="MANAGE_TOOL Response", message="WRONG NAME INPUT")
        self.tool_code = r.json()['tool code']
        self.tool_name = r.json()['tool name']
        self.tool_description = r.json()['tool description']
        self.tool_brand = r.json()['tool brand']
        self.tool_price = r.json()['tool price']
        self.tool_category = r.json()['tool category']

        

        self.text2 =  tk.Label(self, text="product code:", font=("Helvetica", 12))
        self.text2.pack()
        self.text2.place(x=50, y=60)
        self.ent1 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent1.insert(0, self.tool_code)
        self.ent1.place(x=50, y=90, width=400)

        self.text3 =  tk.Label(self, text="tool_name:", font=("Helvetica", 12))
        self.text3.pack()
        self.text3.place(x=50, y=120)
        self.ent2 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent2.insert(0, self.tool_name)
        self.ent2.place(x=50, y=150, width=400)

        self.text4 =  tk.Label(self, text="tool_description:", font=("Helvetica", 12))
        self.text4.pack()
        self.text4.place(x=50, y=180)
        self.ent3 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent3.insert(0, self.tool_description)
        self.ent3.place(x=50, y=210, width=400)

        self.text5 =  tk.Label(self, text="tool_brand:", font=("Helvetica", 12))
        self.text5.pack()
        self.text5.place(x=50, y=240)
        self.ent4 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent4.insert(0, self.tool_brand)
        self.ent4.place(x=50, y=270, width=400)

        self.text8 =  tk.Label(self, text="tool_price:", font=("Helvetica", 12))
        self.text8.pack()
        self.text8.place(x=50, y=300)
        self.ent7 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent7.insert(0, self.tool_price)
        self.ent7.place(x=50, y=330, width=400)

        self.text9 =  tk.Label(self, text="tool_category:", font=("Helvetica", 12))
        self.text9.pack()
        self.text9.place(x=50, y=360)
        self.ent8 = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.ent8.insert(0, self.tool_category)
        self.ent8.place(x=50, y=390, width=400)

        self.button = tk.Button(self, text="Submit modified tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.modify_tool)
        self.button.pack()
        self.button.place(x=180, y=550)

        # self.status = "writed"

    def modify_tool(self):
        if self.ent1.get() != '' and self.ent2.get() != '' and  self.ent3.get() != '' and  self.ent4.get() != '' and  self.ent7.get() != ''  and  self.ent8.get() != '':
        
            input_data = {
                "product_code": self.ent1.get(),
	            "tool_name":self.ent2.get(),
	            "tool_description": self.ent3.get(),
	            "tool_brand": self.ent4.get(),
	            "tool_price": self.ent7.get(),
	            "tool_category": self.ent8.get()
            }

            r = requests.put("http://127.0.0.1:8000/system/category/subtype/tools/", json=input_data)
            respon = json.loads(r.text)
            if respon == {"MODIFY Tool": "change tool infomation successfully"}:
                tk.messagebox.showinfo(title="MANAGE_TOOL Response", message="MODIFY Tool successfully")
        else :
            tk.messagebox.showinfo(title="MANAGE_TOOL Response", message="Need more information")

    #-------------------------------------------------------------------- delete tool -----------------------------------------------------------

    def search_to_delete(self):
        self.text1 = tk.Label(self, text="delete tool", fg="#333", font=("Helvetica", 18, "bold"))
        self.text1.pack()
        self.text1.place(x=200)
        self.search =  tk.Label(self, text="search product:", font=("Helvetica", 12))
        self.search.pack()
        self.search.place(x=500 , y=100)
        self.search_ent = tk.Entry(self, font=("Helvetica", 12), bd=1, relief=tk.SOLID)
        self.search_ent.pack()
        self.search_ent.place(x=500, y=200, width=400)
        self.search_button = tk.Button(self, text="Search", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.delete_tool_widget)
        self.search_button.pack()
        self.search_button.place(x=500, y=300)

    # def delete_tool_status_check(self):
    #     if self.status == "writed":
    #         self.delete_widget()
    #         self.delete_tool_widget()
    #     else:
    #         self.delete_tool_widget()

    def delete_tool_widget(self):
        # if self.status == "writed":
        #     self.delete_widget()
        self.input_name = self.search_ent.get()
        if ' ' in self.input_name : 
            self.input_name = self.input_name.replace(' ','%20')
        r = requests.get(f'http://127.0.0.1:8000/system/category/show_tools/?tool_name={self.input_name}')
        respon = json.loads(r.text)
        if respon == {'GET Tool':'Invalid Tool'}:
            tk.messagebox.showinfo(title="MANAGE_TOOL Response", message="WRONG NAME INPUT")
        self.tool_code = r.json()['tool code']
        self.tool_name = r.json()['tool name']
        self.tool_description = r.json()['tool description']
        self.tool_brand = r.json()['tool brand']
        self.tool_price = r.json()['tool price']
        self.tool_category = r.json()['tool category']

        self.text1 = tk.Label(self, text="Delete tool", fg="#333", font=("Helvetica", 18, "bold"))
        self.text1.pack()
        self.text1.place(x=200)

        self.text2 =  tk.Label(self, text="product code:", font=("Helvetica", 12))
        self.text2.pack()
        self.text2.place(x=50, y=60)
        self.ent1 = tk.Label(self, text = self.tool_code, bd=1, relief=tk.SOLID)
        self.ent1.pack()
        self.ent1.place(x=50, y=90, width=400)

        self.text3 =  tk.Label(self, text="tool_name:", font=("Helvetica", 12))
        self.text3.pack()
        self.text3.place(x=50, y=120)
        self.ent2 = tk.Label(self, text = self.tool_name, bd=1, relief=tk.SOLID)
        self.ent2.pack()
        self.ent2.place(x=50, y=150, width=400)

        self.text4 =  tk.Label(self, text="tool_description:", font=("Helvetica", 12))
        self.text4.pack()
        self.text4.place(x=50, y=180)
        self.ent3 = tk.Label(self, text = self.tool_description, bd=1, relief=tk.SOLID)
        self.ent3.pack()
        self.ent3.place(x=50, y=210, width=400)

        self.text5 =  tk.Label(self, text="tool_brand:", font=("Helvetica", 12))
        self.text5.pack()
        self.text5.place(x=50, y=240)
        self.ent4 = tk.Label(self, text = self.tool_brand, bd=1, relief=tk.SOLID)
        self.ent4.pack()
        self.ent4.place(x=50, y=270, width=400)

        self.text8 =  tk.Label(self, text="tool_price:", font=("Helvetica", 12))
        self.text8.pack()
        self.text8.place(x=50, y=300)
        self.ent7 = tk.Label(self, text = self.tool_price, bd=1, relief=tk.SOLID)
        self.ent7.pack()
        self.ent7.place(x=50, y=330, width=400)

        self.text9 =  tk.Label(self, text="tool_category:", font=("Helvetica", 12))
        self.text9.pack()
        self.text9.place(x=50, y=360)
        self.ent8 = tk.Label(self, text = self.tool_category, bd=1, relief=tk.SOLID)
        self.ent8.pack()
        self.ent8.place(x=50, y=390, width=400)

        self.button = tk.Button(self, text="delete modified tool", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.delete_tool)
        self.button.pack()
        self.button.place(x=180, y=550)

        # self.status = "writed"

    def delete_tool(self):
        r = requests.delete(f'http://127.0.0.1:8000/system/category/subtype/tools/?deleting_tool={self.tool_name}')
        respon = json.loads(r.text)
        if respon == {'DELETE Tool':"delete tool successfully"}:
            tk.messagebox.showinfo(title="DELETE_TOOL Response", message="delete tool successfully")
        elif respon == {'DELETE Tool':'Invalid Tool'}:
            tk.messagebox.showinfo(title="DELETE_TOOL Response", message="WRONG NAME INPUT")

    

    def Back(self): 
        self.master.show_admin()