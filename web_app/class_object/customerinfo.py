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
        for i in self.get_my_reviewed:
            if i._user_name == first_name  :
                return i

    def create_address(self,name,company,country,state,city,address,phone_number,postal_code):
        new_address = Address(name,company,country,state,city,address,phone_number,postal_code)
        for address in self.address:
            if address.name == new_address.name:
                return print('Unvailable to create a new address. Please check your name isn\'t duplicate.')
            
        self.address.append(new_address)        
            
    def get_address(self, name):
        for i in self.address:
            if i.name == name:
                return i
         

    def delete_address(self, address):
        self.address.remove(address)

    def get_ShoppingCart(self):
        return self.my_shoppingcart
    
    def find_user(self, username):
        pass

    def create_review(self, tool, head_of_review, comment, rating, date_of_review):
        review = Review(self._first_name, head_of_review, comment, date_of_review, rating)
        self._my_review.append(review)
        tool.add_review(review)

    @property
    def my_reviewed(self):
        return self._my_review

    @property
    def address(self):
        return self._addresses
        
    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
        
    def __repr__(self) -> str: 
        return "{}".format(self._addresses)
