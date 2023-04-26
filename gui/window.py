import sys 
sys.path.append('./class_object/')  
sys.path.append('./')
import tkinter as tk
from tkinter import *
from login_gui import LoginPage, SignupPage
from make_review import MakeReview
from search_gui import SearchPage
from PIL import Image, ImageTk  
from Tool_gui import Tool_GUI
import random
# # from tkinter import messagebox
# # from tkinter import ttk
import io
import urllib.request
from system import System
# from category import Category 
from app_database import add_database_users, add_database_system, add_database_userdata

system = System() 
add_database_users(system) 
add_database_system(system) 
add_database_userdata(system)
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x700")
        self.resizable(False, False)
        self.title("Login/Search App")
        self.photo = None 
        self._category = system.category
        # Create the menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create the Pages menu with commands to switch to each page
        pages_menu = tk.Menu(menubar, tearoff=0)
        pages_menu.add_command(label="Home", command=self.show_home)
        pages_menu.add_command(label="Search", command=self.show_search)
        pages_menu.add_command(label="Login", command=self.show_login)
        pages_menu.add_command(label="Sign Up", command=self.show_sign_up)
        menubar.add_cascade(label="Pages", menu=pages_menu)

        self.image_list = self.random_tool_to_show()

        # Create the pages
        self.home_page = tk.Frame(self)
        tk.Label(self.home_page, text="This is the Home page").pack()

        self.search_page = SearchPage(link='category', search_type='Category', master=self)
        self.search_page.add_new_search(link='category/tools', search_type='Tool')
        self.login_page = LoginPage(self)
        self.sign_up_page = SignupPage(self) 
        self.tool_page = Tool_GUI(tool =self.image_list[0],master =self)
        self.make_review_page = MakeReview(user = 'NorNor',tool=self.image_list[0].name,master=self)

        self.image1 = self.get_image("https://cdn-icons-png.flaticon.com/512/649/649438.png?w=740&t=st=1682418903~exp=1682419503~hmac=9f666ca6e05c302741f8531345f3fc24865b0a54bd5eed15bd969a63e2e7f431", 150, 150)
        self.image1_label = Label(self.home_page, image = self.image1)
        Label(self.home_page, image=self.image1).place(x=80, y=50)
        self.label1 = Label(self.home_page, text="World wild shipping", font=("Helvetica", 12))
        self.label1.place(x=90, y=210)

        self.image2 = self.get_image("https://cdn-icons-png.flaticon.com/512/1230/1230503.png?w=740&t=st=1682419235~exp=1682419835~hmac=a50c1749ef9f3af3a3c39e5189051db83e07480458eebba875580c16f831a4c7", 150, 150)
        self.image2_label = Label(self.home_page, image = self.image2)
        Label(self.home_page, image=self.image2).place(x=280, y=50)
        Label(self.home_page, text="30 days return", font=("Helvetica", 12)).place(x=300, y=210)
        # Show the initial page

        self.image3 = self.get_image("https://cdn-icons-png.flaticon.com/512/649/649451.png?w=740&t=st=1682420117~exp=1682420717~hmac=9c97285763503fd2b3f9f47313bd2bf611bd598a64b4898c679bf95a2164bffc", 150, 150)
        self.image3_label = Label(self.home_page, image = self.image3)
        Label(self.home_page, image=self.image3).place(x=480, y=50)
        Label(self.home_page, text="wholesale price", font=("Helvetica", 12)).place(x=510, y=210)
        # Show the initial page

        self.image4 = self.get_image("https://cdn-icons-png.flaticon.com/512/1175/1175149.png?w=740&t=st=1682420264~exp=1682420864~hmac=07b81a259160ed6af3e780639e51443439a980e4b926e81ed552e07f0a653679", 150, 150)
        self.image4_label = Label(self.home_page, image = self.image4)
        Label(self.home_page, image=self.image4).place(x=680, y=50)
        Label(self.home_page, text="wholesale price", font=("Helvetica", 12)).place(x=720, y=210)
        # Show the initial page
        self.show_random_tool()

        self.show_home()
    @property
    def category(self): 
        return self._category
    def random_tool_to_show(self):
        show_random_tool = []
        while len(show_random_tool) < 4:
            tool = self.category._all_tools[random.randint(0, len(self.category._all_tools)-1)]
            if tool not in show_random_tool:
                show_random_tool.append(tool)
        return show_random_tool

    def show_random_tool(self):
        #print(self.image_list)
        # tool 1
        self.im = self.get_image(self.image_list[0]._image[0],150,150)
        self.button1 = Button(self.home_page, image=self.im, command= self.jump_to_next_tool1)
        self.button1.pack()
        self.button1.place(x=100,y=350)
        self.description1 = Label(self.home_page,text =self.image_list[0].name) 
        self.description1.pack() 
        self.description1.place(x=100,y=550) 


        # tool 2
        self.im2 = self.get_image(self.image_list[1]._image[0],150,150)
        self.button2 = Button(self.home_page, image=self.im2, command= self.jump_to_next_tool2)
        self.button2.pack()
        self.button2.place(x=300,y=350) 
        self.description2 = Label(self.home_page,text = self.image_list[1].name) 
        self.description2.pack() 
        self.description2.place(x=300,y=550)  

        # tool 3 
        self.im3 = self.get_image(self.image_list[2]._image[0],150,150)
        self.button3 = Button(self.home_page, image=self.im3, command= self.jump_to_next_tool3)
        self.button3.pack()
        self.button3.place(x=500,y=350)  
        self.description3 = Label(self.home_page,text = self.image_list[2].name) 
        self.description3.pack() 
        self.description3.place(x=500,y=550)  

        # tool 4
        self.im4 = self.get_image(self.image_list[3]._image[0],150,150)
        self.button4 = Button(self.home_page, image=self.im4, command= self.jump_to_next_tool4)
        self.button4.pack()
        self.button4.place(x=700,y=350) 
        self.description4 = Label(self.home_page,text = self.image_list[3].name) 
        self.description4.pack() 
        self.description4.place(x=700,y=550) 
    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)
    def jump_to_next_tool1(self):
        self.make_review_page = MakeReview(user = 'NorNor',tool=self.image_list[0].name,master=self) 
        self.tool_page = Tool_GUI(master = self,tool =self.image_list[0])
        self.show_tool()
    def jump_to_next_tool2(self): 
        self.make_review_page = MakeReview(user = 'NorNor',tool=self.image_list[0].name,master=self) 
        self.tool_page = Tool_GUI(master = self,tool =self.image_list[1])
        self.show_tool()
    def jump_to_next_tool3(self):
        self.make_review_page = MakeReview(user = 'NorNor',tool=self.image_list[0].name,master=self) 
        self.tool_page = Tool_GUI(master=self,tool=self.image_list[2])
        self.show_tool()
    def jump_to_next_tool4(self): 
        self.make_review_page = MakeReview(user = 'NorNor',tool=self.image_list[0].name,master=self) 
        self.tool_page = Tool_GUI(master=self,tool=self.image_list[3])
        self.show_tool()
        
    def show_home(self):
        self.tool_page.pack_forget()
        self.search_page.pack_forget()
        #self.search_page.place_forget()
        self.login_page.pack_forget()
        #self.login_page.place_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        #self.sign_up_page.place_forget()
        self.home_page.pack(fill=tk.BOTH, expand=1)
        
    def show_review(self): 
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        #self.home_page.place_forget()
        self.search_page.pack_forget()
        #self.search_page.place_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        self.login_page.pack_forget()
        #self.sign_up_page.place_forget()
        self.make_review_page.pack(fill=tk.BOTH, expand=1)
    def show_search(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        #self.home_page.place_forget()
        self.login_page.pack_forget()
        #self.login_page.place_forget()
        self.sign_up_page.pack_forget()
        #self.sign_up_page.place_forget()
        self.search_page.pack(fill=tk.BOTH, expand=1)
        self.make_review_page.pack_forget()

    def show_login(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        #self.home_page.place_forget()
        self.search_page.pack_forget()
        #self.search_page.place_forget()
        self.sign_up_page.pack_forget()
        self.make_review_page.pack_forget()
        #self.sign_up_page.place_forget()
        self.login_page.pack(fill=tk.BOTH, expand=1)
    def show_tool(self): 
        self.home_page.pack_forget()
        #self.home_page.place_forget()
        self.search_page.pack_forget()
        #self.search_page.place_forget()
        self.sign_up_page.pack_forget()
        self.login_page.pack_forget()
        self.make_review_page.pack_forget()
        #self.login_page.place_forget()
        self.tool_page.pack(fill=tk.BOTH, expand=1)
    def show_sign_up(self):
        self.tool_page.pack_forget()
        self.home_page.pack_forget()
        #self.home_page.place_forget()
        self.search_page.pack_forget()
        #self.search_page.place_forget()
        self.login_page.pack_forget()
        self.make_review_page.pack_forget()
        #self.login_page.place_forget()
        self.sign_up_page.pack(fill=tk.BOTH, expand=1)

    def get_image(self,url,width,height): 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        # self.photo = ImageTk.PhotoImage(im)
        
        return ImageTk.PhotoImage(im)

        # display the image in a label
    

if __name__ == "__main__":
    app = Window()
    app.mainloop()