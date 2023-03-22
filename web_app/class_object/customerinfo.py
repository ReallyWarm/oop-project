from tool import Item
from wishlish import Wishlist
from shoppingcart import ShoppingCart

class CustomerInfo:
    def __init__(self, first_name, last_name, email, company_name) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._company_name = company_name
        self._addresses = [ ]
        self.my_wishlist = Wishlist()
        self.my_shoppingcart = ShoppingCart()
        self.my_order = [ ]
        self.my_review = [ ]
        self.used_coupon = [ ]

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

    def create_review(self):
        pass
        


