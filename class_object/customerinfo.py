from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tool import Tool
    from order import Order
    from discount import Coupon
from user import User
from wishlist import Wishlist
from shoppingcart import ShoppingCart
from address import Address
from review import Review

class CustomerInfo(User):
    def __init__(self, username:str, hashed_password:str, first_name:str, last_name:str, email:str, company_name:str) -> None:
        User.__init__(self, username, hashed_password, first_name, last_name, email)
        self._company_name = company_name
        self._addresses = []
        self._my_wishlist = Wishlist()
        self._my_shoppingcart = ShoppingCart()
        self._my_order = []
        self._my_review = []
        self._used_coupon = []

    def check_used_coupon(self, coupon_code:str) -> bool:
        for coupon in self._used_coupon:
            if coupon.code == coupon_code: 
                return True
        return False

    def store_used_coupon(self, coupon:Coupon):
        self._used_coupon.append(coupon)

    def store_order(self, order:Order) -> None:
        self._my_order.append(order)

    def create_address(self, name:str, company:str, country:str, state:str, city:str, address:str, phone_number:str, postal_code:str) -> None:
        new_address = Address(name,company,country,state,city,address,phone_number,postal_code)
        for address in self.address:
            if address.name == new_address.name:
                return print('Unvailable to create a new address. Please check your name isn\'t duplicate.')
        self.address.append(new_address)        
            
            
    def get_address(self, name) -> Address:
        for i in self.address:
            if i.name == name:
                return i        

    def delete_address(self, name) -> None:
        address = self.get_address(name)
        self.address.remove(address)

    def get_ShoppingCart(self) -> ShoppingCart:
        return self.my_shoppingcart

    def create_review(self, tool:Tool, head_of_review:str, comment:str, rating:float, date_of_review:str) -> None:
        review = Review(self._first_name, head_of_review, comment, date_of_review, rating)
        self._my_review.append(review)
        tool.add_review(review)

    @property
    def my_reviewed(self) -> list:
        return self._my_review
    
    @property
    def my_order(self) -> list:
        return self._my_order
    
    @property
    def my_wishlist(self) -> Wishlist:
        return self._my_wishlist
    
    @property
    def my_shoppingcart(self) -> ShoppingCart:
        return self._my_shoppingcart
    
    @property
    def used_coupon(self) -> list:
        return self._used_coupon

    @property
    def address(self) -> list:
        return self._addresses
        
    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
        
    def __repr__(self) -> str: 
        return "{}".format(self._addresses)
