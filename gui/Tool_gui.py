import tkinter as tk
import requests, json
from make_review import MakeReview
import io
import urllib.request 
from PIL import Image, ImageTk
class Tool_GUI(tk.Frame) : 

    def __init__(self,name,master = None): 
        super().__init__(master) 
        self.master = master 
        self.name = name
        self.chosen_amoung = 1
        self.create_widget()
        self.get_tool_details()
        self.show_amoung()

    def create_widget(self): 
        self.back_button = tk.Button(self,text="home",command=self.Home)
        self.back_button.pack()
        self.back_button.place(x=20,y=500)
        self.review_button = tk.Button(self,text="review",command=self.show_make_review)
        self.review_button.pack()
        self.review_button.place(x=80,y=500)
        self.incresse_amoung_button = tk.Button(self,text="+",command=self.incresse_amoung, font=("Helvetica", 24))
        self.incresse_amoung_button.pack()
        self.incresse_amoung_button.place(x=50,y=400)
        self.add_to_cart_button = tk.Button(self,text="add to cart",command=self.add_tool_to_cart)
        self.add_to_cart_button.pack()
        self.add_to_cart_button.place(x=180,y=450)
        self.decresse_amoung_button = tk.Button(self,text="-",command=self.decresse_amoung, font=("Helvetica", 24))
        self.decresse_amoung_button.pack()
        self.decresse_amoung_button.place(x=310,y=400)
        # self.get_tool_details()

    def show_amoung(self):
        self.chosen_amoung_lable = tk.Label(self, text=self.chosen_amoung, font=("Helvetica", 24))
        self.chosen_amoung_lable.pack()
        self.chosen_amoung_lable.place(x=190,y=400)

    def delete_amoung(self):
        self.chosen_amoung_lable.destroy()

    def get_tool_details(self): 
        name = self.name 
        if ' ' in name : 
            name = name.replace(' ','%20')
        r = requests.get(f'http://127.0.0.1:8000/system/category/show_tools/?tool_name={self.name}')
        self.tool_code = r.json()['tool code']
        self.tool_name = r.json()['tool name']
        self.tool_description = r.json()['tool description']
        self.tool_brand = r.json()['tool brand']
        self.tool_amoung = r.json()['tool amount']
        self.tool_price = r.json()['tool price']
        self.tool_image = r.json()['tool image']
        self.tool_wholesale = r.json()['tool wholesale']
        self.tool_review = r.json()['tool reviews']
        self.tool_rating = r.json()['tool rating']

        self.image1 = self.get_image(self.tool_image[0], 300, 300)
        self.image1_label = tk.Label(self, image = self.image1)
        tk.Label(self, image=self.image1).place(x=50, y=50)

        self.tool_name_label = tk.Label(self, text=self.tool_name, font=("Helvetica", 18))
        self.tool_name_label.place(x=400, y=50)

        self.tool_code_label = tk.Label(self, text=self.tool_code, font=("Helvetica", 12))
        self.tool_code_label.place(x=800, y=60)

        tk.Label(self, text="price", font=("Helvetica", 12)).place(x=150, y=350)

        self.tool_price_label = tk.Label(self, text=self.tool_price, font=("Helvetica", 12))
        self.tool_price_label.place(x=200, y=350)

        tk.Label(self, text='rating ', font=("Helvetica", 12)).place(x= 750, y=100)

        self.tool_rating_label = tk.Label(self, text=self.tool_rating, font=("Helvetica", 12))
        self.tool_rating_label.place(x=800, y=100)

        self.tool_description_label = tk.Label(self, text=self.tool_description, font=("Helvetica", 12))
        self.tool_description_label.place(x=400, y=110)

        self.tool_brand_label = tk.Label(self, text=self.tool_brand, font=("Helvetica", 12))
        self.tool_brand_label.place(x=400, y=80)

        tk.Label(self, text='review ', font=("Helvetica", 12)).place(x= 400, y=250)

        review_list = []
        
        for amount in range(len(self.tool_review)):
            
            review_details = []

            self.tool_review_label_reviewer = tk.Label(self, text=self.tool_review[amount]['_user_name'], font=("Helvetica", 12))
            review_details.append(self.tool_review_label_reviewer)
            # self.tool_review_label_reviewer.place(x=50, y=250+((amount-1))*60)

            self.tool_review_label_score = tk.Label(self, text=self.tool_review[amount]['_rating'], font=("Helvetica", 12))
            review_details.append(self.tool_review_label_score)
            # self.tool_review_label_score.place(x=50, y=280)

            self.tool_review_label_date = tk.Label(self, text=self.tool_review[amount]['_date_of_review'], font=("Helvetica", 12))
            review_details.append(self.tool_review_label_date)
            # self.tool_review_label_date.place(x=50, y=310)

            self.tool_review_label_head_review = tk.Label(self, text=self.tool_review[amount]['_head_of_review'], font=("Helvetica", 12))
            review_details.append(self.tool_review_label_head_review)
            # self.tool_review_label_head_review.place(x=150, y=250)

            self.tool_review_label_detail = tk.Label(self, text=self.tool_review[amount]['_comment'], font=("Helvetica", 12))
            review_details.append(self.tool_review_label_detail)
            # self.tool_review_label_detail.place(x=150, y=280)

            review_list.append(review_details)

        for amount in range(len(review_list)):

            review = review_list[amount]
            long = 30

            for detail in range(3):
                
                review[detail].place(x=400, y=280+long*detail+100*amount)
                 
            for detail in range(3,5):
                review[detail].place(x=500, y=280+long*(detail-3)+100*amount)

    def incresse_amoung(self):
        if self.tool_amoung > self.chosen_amoung:
            self.delete_amoung()
            self.chosen_amoung += 1
            self.show_amoung()
            #print("added")
        else:
            #print("Passed")
            pass

    def add_tool_to_cart(self):
        input_data = {"tool_name": self.tool_name, "quantity": self.chosen_amoung}
        r = requests.post(f'http://127.0.0.1:8000/system/shopping_cart/', json=input_data)
        self.delete_amoung()
        self.chosen_amoung = 1
        self.show_amoung()
        

    def decresse_amoung(self):
        if self.chosen_amoung > 1:
            self.delete_amoung()
            self.chosen_amoung -= 1
            self.show_amoung()
        else:
            pass
    
    def get_image(self,url,width,height) -> ImageTk.PhotoImage: 
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()  # read the image data from the URL

        im = Image.open(io.BytesIO(raw_data))  # create a PIL Image object from the image data
        im = im.resize((width,height))
        return ImageTk.PhotoImage(im)
    
    def Home(self):  
        self.master.show_home() 
        
    def show_make_review(self): 
        self.master.show_review()