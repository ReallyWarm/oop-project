
from wishlish import Wishlist
from shoppingcart import ShoppingCart
from address import Address
from order import Order
# manage addresss

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
        self.my_review = []
        self.used_coupon = []

    def check_coupon(self, coupon):
        pass

    def store_use_coupon(self, coupon):
        pass

    def store_order(self,order):
        for i in self.my_order:
            if self.my_order[i] == order:
                return self.my_order[i]

    def store_review(self, review):
        for i in self.my_review:
            if self.my_review[i] == review:
                return self.my_review[i]

    def add_addresse(self,address):
        if address._name not in self._addresses:
            self._addresses.append(address)
        else:
            for i in self._addresses:
                if i.name == address.name:
                    i = address
                break

    def get_addresse(self, address):
        for i in range(len(self._addresses)):
            if self._addresses[i]._name == address._name:
                return self._addresses[i]
                break

    def update_edit_addresse(self, address):
        for i in range(len(self._addresses)):
            if self._addresses[i]._name == address._name:
                self._addresses[i] = address
                break
            
    def delete_addresse(self, address):
        self._addresses.remove(address)


    def get_ShoppingCart(self):
        return self.my_shoppingcart
    
    def find_user(self, username):
        pass

    def create_review(self):
        pass
    
    def __str__(self):
        return "{}".format(self._addresses)
    
    def __repr__(self) -> str:
        return "{}".format(self._addresses)
