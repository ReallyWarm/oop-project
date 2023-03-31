class Tool:
    def __init__(self, code, name, description, brand, \
                 amount, image, price, type_of_tool) -> None:
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

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    
    def get_attributes(self, attr):
        return self.__dict__[attr]

    def modify_tool(self):
        pass

    def add_review(self):
        pass

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())

class Item:
    def __init__(self, tool, buy_amount) -> None: 
        self._tool = tool
        self._buy_amount = buy_amount
        self._items_price = tool.price * buy_amount

    @property
    def tool(self):
        return self._tool
    
    @property
    def amount(self):
        pass 

    @amount.setter
    def amount(self,value):
        self.buy_amount = value

    def update_item(self):
        pass