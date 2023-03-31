class Coupon:
    def __init__(self, code, discount_value,name) -> None:
        self._name = name
        self._code = code
        self._discount_value = discount_value
    @property
    def name(self): 
        return self._name
    
    @name.setter 
    def name(self, value):
        self._name = value

    @property
    def discount_value(self):
        return self._discount_value
    
    @discount_value.setter 
    def discount_value(self, value):
        self._discount_value = value
    
    def __str__(self):
        return str(self._code)

class Wholesale:
    def __init__(self, amount, discount_value) -> None:
        self._amount = amount
        self._discount_value = discount_value