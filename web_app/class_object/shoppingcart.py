from tool import Item
class ShoppingCart: 
    def __init__(self) -> None:
        self._cart = [ ]
        self._subtotal_price = 0.00
        self._shipping_price = 0.00
        self._discount_value = 0.00
        self._total_price = 0.00

    @property
    def carts(self):
        return self._cart

    def add_item(self, item_tool,buy_amount = 1): 
        for item in self._cart: 
            if item._tool == item_tool : 
                if item._buy_amount is not buy_amount: 
                    item.buy_amount = buy_amount
                return 
        new_item = Item(item_tool,buy_amount)
        self._cart.append(new_item)

    def set_item(self):
        pass

    def get_item(self):
        pass

    def delete_item(self,item_tool):
        for item in self._cart: 
            if item._tool == item_tool : 
                self._cart.remove(item) 
                return

    def clear_cart(self):
        pass

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
