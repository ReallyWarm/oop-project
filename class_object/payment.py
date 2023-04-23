import datetime
import random
import string
class Payment: 
    def __init__(self, total_amount:float, card:str, discount_amount:int = 0) -> None:
        self.__total_amount = total_amount
        self.__date_create = datetime.datetime.now()
        self.__id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.__card = card 
        self.__discount_amount = discount_amount * self.__total_amount/100
        self.__final_price = self.__total_amount - self.__discount_amount

    @property
    def total_amount(self):
        return self.__total_amount
    
    @property
    def discount_amount(self):
        return self.__discount_amount
    
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
        if(len(card) == 16 and card.isdigit()): 
            return True 
        return False 

    def perform_payment(self) -> bool:
        ''' do payment stuff here but we this is just for demo purposes'''
        return True