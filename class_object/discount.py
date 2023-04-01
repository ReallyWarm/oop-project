class Coupon:
    def __init__(self, code:str, discount_value:int, name:str) -> None:
        self._name = name
        self._code = code
        self._discount_value = discount_value
    
    @property
    def code(self) -> str:
        return self._code
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter 
    def name(self, value:str) -> None:
        self._name = value

    @property
    def discount_value(self) -> int:
        return self._discount_value
    
    @discount_value.setter 
    def discount_value(self, value:int) -> None:
        self._discount_value = value
    
    def __str__(self) -> str:
        return str(self._code)

class Wholesale:
    def __init__(self, code:str, amount:int, discount_value:int) -> None:
        self._code = code
        self._amount = amount
        self._discount_value = discount_value 

    @property
    def code(self) -> str: 
        return self._code
    
    @property
    def amount(self) -> int:
        return self._amount
    
    @amount.setter
    def amount(self, value:int) -> None: 
        self._amount = value

    @property 
    def discount_value(self) -> int: 
        return self._discount_value
    
    @discount_value.setter
    def discount_value(self, value:int) -> None:
        self._discount_value = value
    
        