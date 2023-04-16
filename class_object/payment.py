import datetime
import random
import string
class Payment : 
    def __init__(self, total_amount:float,card:str,discount_amount : int = 0) -> None:
        self.__total_amount = total_amount
        self.__date_create = datetime.datetime.now()
        # self.__id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) 
        self.__id = None
        self.__card = card 
        self.__final_price = (100 - discount_amount) * self.__total_amount/100 
    def make_payment(self):
        if( not self.check_valid_card(self.__card)): 
            return "Invalid card" 
        self.__id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) 
        status = self.perform_payment() 
        if status == True: 
            return "payment success" 
        else : 
            return "payment fail"

    def check_valid_card(self,card) -> bool: 
        if(len(card) == 16 and card.isdigit()): 
            return True 
        return False 


    def perform_payment(self) -> bool:
        return True
# payment = Payment(231.21,"mnasdxx",21,"sdf5","ON") 
# print(payment.date_create)