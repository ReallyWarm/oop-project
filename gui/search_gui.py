import tkinter as tk
import requests

class SearchPage(tk.Frame):
    def __init__(self, link:str, search_type:str, master=None):
        super().__init__(master)
        self.master = master
        self.link = []
        self.link.append(link)
        self.search_type = []
        self.search_type.append(search_type)
        self.search_index = 0
        self.create_widgets()

    def add_new_search(self, link:str, search_type:str):
        self.link.append(link)
        self.search_type.append(search_type)

    def create_widgets(self):
        self.search_label = tk.Label(self, text=f"Search {self.search_type[self.search_index]}:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.do_search)
        self.search_button.pack()

        self.swap_button = tk.Button(self, text="Swap Search", command=self.swap_to_other_search)
        self.swap_button.pack()

    def do_search(self):
        query = self.search_entry.get()
        r = requests.get(f'http://127.0.0.1:8000/system/{self.link[self.search_index]}?search={query}')

        if self.search_index == 1:
            name = [key for key in r.json().keys()]
            widget_searched = []
            for tool_widget in self.master.tool_widgets:
                if tool_widget.name in name:
                    widget_searched.append(tool_widget)
            self.master.show_tool_widget(widget_searched, start_x=75, start_y=200, page=self)

    def swap_to_other_search(self):
        if len(self.link) - 1 > self.search_index:
            self.search_index += 1
        else:
            self.search_index = 0
        self.search_label.configure(text=f"Search {self.search_type[self.search_index]}:")
        self.master.hide_tool_widget()
