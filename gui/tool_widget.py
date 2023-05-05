import tkinter as tk
from tkinter import Button, Label
from make_review import MakeReview
from Tool_gui import Tool_GUI
from PIL import ImageTk

class ToolWidget():
    def __init__(self, image:'ImageTk.PhotoImage', master,name=''):
        self.name = name
        self.im = image
        self.button = Button(master, image=self.im)
        self.button.pack()
        self.button.place(x=0,y=0)
        self.description = Label(master, text=name) 
        self.description.pack()
        self.description.place(x=0,y=self.im.height()+20)
        self.make_review_page = MakeReview(user=master.first_name, tool=name, master=master) 
        self.tool_page = Tool_GUI(master=master, name=name)
        self.unpack()

    def set_button_command(self, command):
        self.button['command'] = command

    def set_coords(self, x, y):
        self.button.place(x=x,y=y)
        self.description.place(x=x,y=y+self.im.height()+20)

    def unpack(self):
        self.button.pack(in_=None)
        self.description.pack(in_=None)
        self.button.pack_forget()
        self.description.pack_forget()