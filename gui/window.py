import tkinter as tk
from login_gui import LoginPage, SignupPage
from search_gui import SearchPage

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")
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

if __name__ == "__main__":
    app = Window()
    app.mainloop()