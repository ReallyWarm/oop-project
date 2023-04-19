import tkinter as tk
import requests
import json

class SignupPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.firstname_label = tk.Label(self, text="First name:")
        self.firstname_label.pack()

        self.firstname_entry = tk.Entry(self)
        self.firstname_entry.pack()

        self.lastname_label = tk.Label(self, text="Last name:")
        self.lastname_label.pack()

        self.lastname_entry = tk.Entry(self)
        self.lastname_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.company_label = tk.Label(self, text="Company name:")
        self.company_label.pack()

        self.company_entry = tk.Entry(self)
        self.company_entry.pack()

        self.signup_button = tk.Button(self, text="Signup", command=self.do_signup)
        self.signup_button.pack()

    def do_signup(self):
        self.master.switch_to_signup_page()

class LoginPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.do_login)
        self.login_button.pack()

        self.logout_button = tk.Button(self, text="Logout", command=self.do_logout)
        self.logout_button.pack()

        self.switch_button = tk.Button(self, text="Search Page", command=self.switch_to_search_page)
        self.switch_button.pack()

    def do_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        data = {"username": username, "password": password}
        r = requests.post('http://127.0.0.1:8000/login', params=data)
        print(r, r.json())

    def do_logout(self):
        r = requests.post('http://127.0.0.1:8000/logout')
        print(r, r.json())

    def switch_to_search_page(self):
        self.master.switch_to_search_page()


class SearchPage(tk.Frame):
    def __init__(self, master=None, link='', search_type=''):
        super().__init__(master)
        self.master = master
        self.link = link
        self.search_type = search_type
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self, text=f"Search {self.search_type}:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Search", command=self.do_search)
        self.search_button.pack()

        self.switch_button = tk.Button(self, text="Login Page", command=self.switch_to_login_page)
        self.switch_button.pack()

        self.swap_button = tk.Button(self, text="Swap Search", command=self.swap_to_other_search)
        self.swap_button.pack()

    def do_search(self):
        query = self.search_entry.get()
        r = requests.get(f'http://127.0.0.1:8000/system/{self.link}?search={query}')
        print(r, r.json())

    def switch_to_login_page(self):
        self.master.switch_to_login_page()

    def swap_to_other_search(self):
        self.master.swap_search_page()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.resizable(False, False)
        self.title("Login/Search App")
        self.signup_page = SignupPage(self)
        self.login_page = LoginPage(self)
        self.all_search_page = [SearchPage(self, link='category', search_type='Category'),
                                SearchPage(self, link='category/tools', search_type='Tool')]
        self.active_search_index = 0

        # create the menu bar
        menubar = tk.Menu(self)
        user_menu = tk.Menu(menubar, tearoff=0)
        user_menu.add_command(label="Login", command=self.switch_to_login_page())
        user_menu.add_command(label="Signup")
        user_menu.add_separator()
        user_menu.add_command(label="Logout", command=self.login_page.do_logout())
        menubar.add_cascade(label="User", menu=user_menu)
        search_menu = tk.Menu(menubar, tearoff=0)
        search_menu.add_command(label="Search", command=self.switch_to_search_page)
        menubar.add_cascade(label="Search", menu=search_menu)

        self.config(menu=menubar)
        self.switch_to_login_page()

    def switch_to_login_page(self):
        for page in self.all_search_page: 
            page.pack_forget()
        self.signup_page.pack_forget()
        self.login_page.pack(fill=tk.BOTH, expand=1)

    def switch_to_signup_page(self):
        for page in self.all_search_page: 
            page.pack_forget()
        self.signup_page.pack(fill=tk.BOTH, expand=1)
        self.login_page.pack_forget()

    def switch_to_search_page(self):
        self.login_page.pack_forget()
        self.signup_page.pack_forget()
        self.all_search_page[self.active_search_index].pack(fill=tk.BOTH, expand=1)

    def swap_search_page(self):
        self.all_search_page[self.active_search_index].pack_forget()
        if self.active_search_index < len(self.all_search_page) - 1:
            self.active_search_index += 1
        else:
            self.active_search_index = 0
        self.all_search_page[self.active_search_index].pack(fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
