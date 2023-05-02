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
        self.category_box = []
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
        self.master.hide_tool_widget()

        if self.search_type[self.search_index] == 'Tool':
            name_list = [key for key in r.json().keys()]
            self.show_searched_tool(name_list)

        if self.search_type[self.search_index] == 'Category':
            self.category_box.clear()
            for typename, typedata in r.json().items():
                subtype_list = [subtype_data.get('_subtypename') for subtype_data in typedata.get('_subtypes_of_tool')]

                dropdown_button = tk.Menubutton(self, text=typename, relief='raised')
                dropdown = tk.Menu(dropdown_button, tearoff=0)

                for subtype in subtype_list:
                    subtype_r = requests.get(f'http://127.0.0.1:8000/system/{self.link[self.search_index]}/subtype/?search={subtype}')
                    tool_list = [tool_data.get('_name') for subdata in subtype_r.json().values() for tool_data in subdata.get('_tools_list')]
                    dropdown.add_command(label=subtype, command=lambda tl=tool_list: self.show_searched_tool(tl))
                    
                dropdown_button["menu"] = dropdown
                self.category_box.append(dropdown_button)

            for i, category in enumerate(self.category_box):
                category.pack(expand=True)
                col = 125 * (i%6)
                row = 100 * (i//6)
                category.place(x=100+col, y=150+row)

    def swap_to_other_search(self):
        if len(self.link) - 1 > self.search_index:
            self.search_index += 1
        else:
            self.search_index = 0
        self.search_label.configure(text=f"Search {self.search_type[self.search_index]}:")
        self.master.hide_tool_widget()
        self.clear_category_box()

    def show_searched_tool(self, toolname_list):
        widget_searched = []
        for tool_widget in self.master.tool_widgets:
            if tool_widget.name in toolname_list:
                widget_searched.append(tool_widget)
        self.clear_category_box()
        self.master.show_tool_widget(widget_searched, start_x=75, start_y=150, page=self)

    def clear_category_box(self):
        for category_box in self.category_box:
            category_box.destroy()
        self.category_box.clear()
