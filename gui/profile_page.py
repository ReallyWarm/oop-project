import tkinter as tk
from user_profile import Profile
from create_address import CreateAddressGUI
from delete_edit_address import EditDeleteAddressGUI

class ProfileGUI(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master =master
        self.user_profile = Profile(self)
        self.create_address = CreateAddressGUI(self)
        self.edit_delete_address = EditDeleteAddressGUI(self)
        self.create_widget()
      
        
    def show_create_address(self):
        self.edit_delete_address.pack_forget()
        self.user_profile.pack_forget()
        self.create_address.pack()    
        
    def show_edit_delete_address(self):
        self.user_profile.pack_forget()
        self.create_address.pack_forget()    
        self.edit_delete_address.pack()
        
    def show_profile(self):
        self.create_address.pack_forget()    
        self.edit_delete_address.pack_forget() 
        self.user_profile.pack()
        
    def create_widget(self):
        self.show_profile()
        self.create_address_button = tk.Button(self, text="Create Address", font=("Arial", 12), command=self.show_create_address)
        self.create_address_button.pack()
        self.create_address_button.place(x=150, y=600)
        
        self.edit_delete_address_button = tk.Button(self, text='Edit and delete Address' , font=("Arial", 12), command=self.show_edit_delete_address)
        self.edit_delete_address_button.pack()
        self.edit_delete_address_button.place(x=450,y=600)
        
        self.back_to_profile_button = tk.Button(self, text='Back to Profile', font=("Arial", 12), command=self.show_profile)
        self.back_to_profile_button.pack()
        self.back_to_profile_button.place(x=700,y=650)    