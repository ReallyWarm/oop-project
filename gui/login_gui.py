import tkinter as tk
from tkinter import messagebox
import requests, json

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

        self.all_entry = []
        self.all_entry.extend([self.username_entry, self.password_entry])

    def do_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        data = {"username": username, "password": password}
        r = requests.post('http://127.0.0.1:8000/login', params=data)
        print(r, r.json())
        if r.status_code == 200:
            for entry in self.all_entry: 
                entry.delete(0, 'end')
            messagebox.showinfo(title="notification",message=f"Logged in!")
            self.master.show_home()
        else:
            messagebox.showinfo(title="notification",message=r.json().get('detail'))

    def do_logout(self):
        r = requests.post('http://127.0.0.1:8000/logout')
        print(r, r.json())
        if r.status_code == 200:
            messagebox.showinfo(title="notification",message=f"Logged out!")
            self.master.show_home()

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

        self.all_entry = []
        self.all_entry.extend([self.username_entry, self.password_entry, self.firstname_entry, self.lastname_entry, self.email_entry, self.company_entry])

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
        if r.status_code == 200:
            for entry in self.all_entry: 
                entry.delete(0, 'end')
            messagebox.showinfo(title="notification",message=f"Account created!")
            self.master.show_home()
        else:
            messagebox.showinfo(title="notification",message=r.json().get('detail'))
