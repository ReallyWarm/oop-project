import sys
sys.path.append('./class_object/')
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from category import Category
from fastapi import FastAPI
from system import System
from app_database import add_database_users, add_database_system, add_database_userdata

app = FastAPI()
system = System()

add_database_users(system)
add_database_system(system)
add_database_userdata(system)

import random
import requests
import json

class Home:
    def __init__(self):
        self.root = Tk()
        self._category = Category()
        self.root.title("Home")
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.configure(background="#f7f7f7") 
        self.root.config(cursor="hand2")
        Button(text="send random", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.random_show).grid(row=4, column=4)
        self.root.mainloop()

    @property
    def category(self) -> 'Category':
        return self._category

    def random_tool_to_show(self):
        show_random_tool = []
        while show_random_tool.size() <= 4:
            a = random.randint(0, len(self.category._all_tools))
            tool = self.category._all_tools[a]
            for item in show_random_tool:
                if item == a:
                    continue
                else:
                    show_random_tool.append(tool)

    def show_random_tool(self):
        #
    



Home()