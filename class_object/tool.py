from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from discount import Wholesale
    from review import Review

class Tool:
    def __init__(self, code:str, name:str, description:str, brand:str, \
                 amount:int, image, price:float, type_of_tool:str) -> None:
          self._code = code
          self._name = name
          self._description = description
          self._brand = brand
          self._amount = amount
          self._price = price
          self._category = type_of_tool
          self._reviews = [ ]
          self._image = [image]
          self._wholesale = [ ]
          self._rating = 0.00
          self.__n_review = 0.00
          self.__rated_review = 0.00

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def wholesales(self) -> list:
        return self._wholesale
    
    def add_wholesale(self, wholesale:'Wholesale') -> None:
        self._wholesale.append(wholesale)

    @property
    def price(self) -> float:
        return self._price
    
    @property
    def review_list(self) -> list:
        return self._reviews
    
    def add_review(self, review:'Review') -> None:
        self._reviews.append(review)
        self.__n_review += 1
        self.__rated_review += review._rating
        self._rating = self.__rated_review / self.__n_review

    @property
    def rating(self) -> float:
        return self._rating

    def modify_tool(self) -> None:
        print(self)
        a = input('Choose modify infomation: \n 1 = name \n 2 = description \n 3 = brand \n 4 = price \n your input:::')

        def modify_name(new_name:str):
            self._name = new_name
            
        def modify_description(new_description:str):
            self._description = new_description
            
        def modify_brand(new_brand:str):
            self._brand = new_brand
            
        def modify_price(new_price:float):
            self._price = new_price
            
        # print(a)  
        if (int(a) == 1):
            new_name = input('Enter new name:')
            modify_name(new_name)
            print('changing success')
        elif ( int(a) == 2 ):
            new_description = input('Enter new description:')
            modify_description(new_description)
            print('changing success')
        elif (int(a) == 3 ):
            new_brand = input('Enter new brand:')
            modify_brand(new_brand)
            print('changing success')
        elif (int(a) == 4):
            new_price = input('Enter new price:')
            modify_price(new_price)
            print('changing success')
            
        print(self)

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())

class Item:
    def __init__(self, tool:'Tool', buy_amount:int) -> None: 
        self._tool = tool
        self._buy_amount = buy_amount
        self._items_price = tool.price * buy_amount

    @property
    def tool(self) -> 'Tool':
        return self._tool
    
    @property
    def buy_amount(self) -> int:
        return self._buy_amount
    
    @property
    def items_price(self) -> float:
        return self._items_price
    
    def set_buy_amount(self, amount:int) -> None:
        self._buy_amount = amount
        self.update_item()

    def update_item(self) -> None:
        self._items_price = self.tool.price * self.buy_amount

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())

    def __repr__(self) -> str:
        return f'\"{self.__str__()}\"'