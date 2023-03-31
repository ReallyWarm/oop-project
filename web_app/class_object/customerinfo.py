from wishlish import Wishlist
from shoppingcart import ShoppingCart
from address import Address
from tool import Item,Tool
from review import Review

class CustomerInfo:
    def __init__(self, first_name, last_name, email, company_name) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._company_name = company_name
        self._addresses = []
        self.my_wishlist = Wishlist()
        self.my_shoppingcart = ShoppingCart()
        self.my_order = []
        self._my_review = []
        self.used_coupon = []

    def check_coupon(self, coupon):
        pass

    def store_use_coupon(self, coupon):
        pass

    def store_order(self,order):
        for i in self.my_order:
            if i == order:
                return i

    def store_review(self,first_name) :
        for i in self._my_review:
            if i._user_name == first_name  :
                return i

    def create_address(self,name,company,country,state,city,address,phone_number,postal_code):
        address = Address(name,company,country,state,city,address,phone_number,postal_code)
        if address._name not in self._addresses:
            self._addresses.append(address)
        else:
            for i in self._addresses:
                if i.name == address.name:
                    i = address
                break

    def get_address(self, address):
        for i in self._addresses:
            if i._name == address._name:
                return i
                break

            
    def delete_address(self, address):
        self._addresses.remove(address)


    def get_ShoppingCart(self):
        return self.my_shoppingcart
    
    def find_user(self, username):
        pass

    def create_review(self, tool):
        head_of_review = input('Enter head of review:')
        comment = input('Enter comment: ')
        rating = float(input('Enter rating: '))
        date_of_review = str(input('Enter date of review: '))
        review = Review(self.get_username, head_of_review, comment, date_of_review, rating)
        print("--------------------------------------------")
        print("creat review success")
        print("'id of review is ")
        print(id(review))
        print(review)
        print("--------------------------------------")
        print("review information is \n reviewed user:{} \n head of review: {} \n comment review: {} \n date of review: {} \n rating: {}".\
              format(review._user_name, review._head_of_review, review._comment, review._date_of_review, review._rating))
        self.get_my_reviewed.append(review)
        print("---------------------------------------------")
        print("My reviewed: {}".format(self.get_my_reviewed))
        tool.add_review(review)

    @property
    def get_username(self):
        return self._first_name
        
    @property
    def get_my_reviewed(self):
        return self._my_review
        
    def __repr__(self) -> str: 
        return "{}".format(self._addresses)
