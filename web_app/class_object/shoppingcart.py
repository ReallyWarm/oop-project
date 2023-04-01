from tool import Tool, Item

class ShoppingCart: 
    def __init__(self) -> None:
        self._cart = []
        self._subtotal_price = 0.00
        self._shipping_price = 0.00
        self._discount_value = 0.00
        self._total_price = 0.00

    @property
    def cart(self):
        return self._cart
    
    def find_item(self, tool:Tool):
        for cart_item in self.cart:
            if tool is cart_item.tool:
                return cart_item
        return None

    def add_item(self, tool:Tool, buy_amount:int):
        cart_item = self.find_item(tool)
        if cart_item is not None:
            cart_item.set_buy_amount(buy_amount)
        else:
            self._cart.append(Item(tool, buy_amount))

    def add_by_item(self, item:Item):
        cart_item = self.find_item(item.tool)
        if cart_item is not None:
            cart_item.set_buy_amount(item.buy_amount)
        else:
            self._cart.append(item)
        
    def set_item_amount(self, tool:Tool, buy_amount:int):
        item = self.get_items(tool)
        item.set_buy_amount(buy_amount)

    def get_items(self, tool:Tool):
        for cart_item in self.cart:
            if tool == cart_item.tool:
                return cart_item 

    def delete_item(self, tool:Tool):
        item = self.get_items(tool)
        self._cart.remove(item)

    def clear_cart(self):
        self._cart.clear()

    def calculate_price(self):
        pass

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
