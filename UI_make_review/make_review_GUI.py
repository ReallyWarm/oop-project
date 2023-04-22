from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import requests
import json

class make_review_GUI:
    def __init__(self, user, tool):
        self.user = user
        self.tool = tool
        self.root = Tk()
        self.root.title("Make Review")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(background="#f7f7f7")  # Set background color
        self.root.config(cursor="hand2")
        
        # Create a label for the heading
        Label(text="Write Review", fg="#333", font=("Helvetica", 18, "bold")).pack(pady=20)
        
        # Create a label for the review title
        Label(text="Title:", font=("Helvetica", 12)).place(x=50, y=60)
        self.ent1 = Entry(self.root, font=("Helvetica", 12), bd=1, relief=SOLID)  # Set border properties
        self.ent1.place(x=50, y=90, width=400)
        
        # Create a label for the review comment
        Label(text="Comment:", font=("Helvetica", 12)).place(x=50, y=130)
        self.ent2 = Text(width=40, height=10, font=("Helvetica", 12), bd=1, relief=SOLID)  # Set border properties
        self.ent2.place(x=50, y=160)
        
        # Create a label for the review rating
        Label(text="Rating:", font=("Helvetica", 12)).place(x=50, y=350)
        rating = StringVar()
        self.ent3 = ttk.Combobox(self.root, width=30, textvariable=rating, font=("Helvetica", 12))
        self.ent3['value'] = (0,1,2,3,4,5)
        self.ent3.place(x=50, y=380)
        self.ent3.current()
        
        # Create a button to send the review
        Button(text="Submit Review", font=("Helvetica", 12, "bold"), bg="#333", fg="#fff", command=self.send_review).place(x=180, y=430)
        
        self.root.mainloop()

    def send_review(self):
        data = {
                "User":self.user,
                "tool":self.tool,
                "head_review":self.ent1.get(),
                "comment":self.ent2.get("1.0","end-1c"),
                "rating":self.ent3.get(),
                "date_of_review":datetime.now().strftime("%d-%m-%Y")
            }
        
        # date = data["date_of_review"]
        # print(date)
        r = requests.post("http://127.0.0.1:8000/tool/make_review",json = data)
        respon = json.loads(r.text)
        if respon == {'data': 'A new review is added!'}:
            messagebox.showinfo(title="Review Response", message="Your review has been added!")
        print(respon)

make_review_GUI('NorNor','Testing drill')