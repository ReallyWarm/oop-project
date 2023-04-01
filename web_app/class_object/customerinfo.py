from tool import Item,Tool
from wishlish import Wishlist
from shoppingcart import ShoppingCart
from review import Review

class CustomerInfo:
    def __init__(self, first_name, last_name, email, company_name) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._company_name = company_name
        self._addresses = [ ]
        self._my_wishlist = Wishlist()
        self._my_shoppingcart = ShoppingCart()
        self._my_order = [ ]
        self._my_review = [ ]
        self._used_coupon = [ ]

    def check_coupon(self,coupon):
        pass

    def store_use_coupon(self,coupon):
        pass

    def store_order(self,order):
        pass

    def store_review(self,review):
        pass

    def add_addresse(self):    
        pass

    def get_address(self):
        pass

    def delete_address(self):
        pass

    def find_user(self,username):
        pass

    def create_review(self, tool, head_of_review, comment, rating, date_of_review):
        review = Review(self._first_name, head_of_review, comment, date_of_review, rating)
        self._my_review.append(review)
        tool.add_review(review)
    
    @property
    def my_reviewed(self):
        return self._my_review
    
    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
        


