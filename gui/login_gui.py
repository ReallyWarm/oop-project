import tkinter as tk
import requests, json

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.resizable(False, False)
        self.title("Login/Search App")

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

        # Create the pages
        self.home_page = tk.Frame(self)
        tk.Label(self.home_page, text="This is the Home page").pack()

        self.search_page = SearchPage(link='category', search_type='Category', master=self)
        self.search_page.add_new_search(link='category/tools', search_type='Tool')

        self.login_page = LoginPage(self)

        self.sign_up_page = SignupPage(self)

        # Show the initial page
        self.show_home()

    def show_home(self):
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.home_page.pack(fill=tk.BOTH, expand=1)

    def show_search(self):
        self.home_page.pack_forget()
        self.login_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.search_page.pack(fill=tk.BOTH, expand=1)

    def show_login(self):
        self.home_page.pack_forget()
        self.search_page.pack_forget()
        self.sign_up_page.pack_forget()
        self.login_page.pack(fill=tk.BOTH, expand=1)

    def show_sign_up(self):
        self.home_page.pack_forget()
        self.search_page.pack_forget()
        self.login_page.pack_forget()
        self.sign_up_page.pack(fill=tk.BOTH, expand=1)

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

    def do_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        data = {"username": username, "password": password}
        r = requests.post('http://127.0.0.1:8000/login', params=data)
        print(r, r.json())

    def do_logout(self):
        r = requests.post('http://127.0.0.1:8000/logout')
        print(r, r.json())

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
        username = self.username_entry.get()
        password = self.password_entry.get()
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        email = self.email_entry.get()
        company = self.company_entry.get()
        data = {"username": username, "password": password, "first_name": firstname, "last_name": lastname, "email": email, "company_name": company}
        r = requests.post('http://127.0.0.1:8000/signup', data=json.dumps(data))
        print(r, r.json())

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
        print(len(self.link), self.search_index)
        query = self.search_entry.get()
        r = requests.get(f'http://127.0.0.1:8000/system/{self.link[self.search_index]}?search={query}')
        print(r, r.json())

    def swap_to_other_search(self):
        if len(self.link) - 1 > self.search_index:
            self.search_index += 1
        else:
            self.search_index = 0
        self.search_label.configure(text=f"Search {self.search_type[self.search_index]}:")

if __name__ == "__main__":
    app = Window()
    app.mainloop()