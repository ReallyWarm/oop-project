import datetime
import random
import string
from order import Order

class Payment: 
    def __init__(self, total_price:float, shipping_price:float, card:str, discount_price:int = 0) -> None:
        self.__total_price = total_price
        self.__shipping_price = shipping_price
        self.__date_create = datetime.datetime.now()
        self.__id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.__card = card 
        self.__discount_price = discount_price * self.__total_price/100
        self.__final_price = self.__total_price + shipping_price - self.__discount_price

    @property
    def total_price(self):
        return self.__total_price
    
    @property
    def shipping_price(self):
        return self.__shipping_price
    
    @property
    def discount_price(self):
        return self.__discount_price
    
    @property
    def final_price(self):
        return self.__final_price
    
    @property
    def date_create(self):
        return self.__date_create
    
    @property
    def payment_id(self):
        return self.__id
        
    def make_payment(self):
        if( not self.check_valid_card(self.__card)): 
            return "Invalid card" 
        status = self.perform_payment() 
        if status == True: 
            return "Payment success" 
        else : 
            return "Payment fail"

    def check_valid_card(self, card) -> bool: 
        #  and card.isdigit()
        if(len(card) == 16): 
            return True 
        return False 

    def perform_payment(self) -> bool:
        ''' do payment stuff here but we this is just for demo purposes'''
        return True
        
    def create_order(self, order_items, address):
        return Order(order_items, self.__id, self.__date_create, self.__total_price, self.__shipping_price, self.__discount_price, self.__final_price, address)