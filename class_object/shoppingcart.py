from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tool import Tool
from tool import Item

class ShoppingCart: 
    def __init__(self) -> None:
        self._cart = []
        self._total_price = 0.00
        self._shipping_price = 40.00
        self._final_price = 0.00

    @property 
    def total_price(self):
        return self._total_price
    
    @property 
    def shipping_price(self): 
        return self._shipping_price
    
    @property 
    def total_price(self): 
        return self._total_price
    
    @property
    def cart(self) -> list:
        return self._cart
    
    def get_item(self, tool:Tool) -> Item | None:
        for cart_item in self.cart:
            if tool is cart_item.tool:
                return cart_item
        return None

    def add_item(self, tool:Tool, buy_amount:int) -> None:
        cart_item = self.get_item(tool)
        if cart_item is not None:
            cart_item.set_buy_amount(buy_amount)
        else:
            self._cart.append(Item(tool, buy_amount))
        self.calculate_price()

    def add_by_item(self, item:Item) -> None:
        cart_item = self.get_item(item.tool)
        if cart_item is not None:
            cart_item.set_buy_amount(item.buy_amount)
        else:
            self._cart.append(item)
        self.calculate_price()
        
    def set_item_amount(self, tool:Tool, buy_amount:int) -> None:
        item = self.get_item(tool)
        item.set_buy_amount(buy_amount)
        self.calculate_price()

    def delete_item(self, tool:Tool) -> None:
        item = self.get_item(tool)
        self._cart.remove(item)
        self.calculate_price()

    def clear_cart(self) -> None:
        self._cart.clear()
        self.calculate_price()

    def calculate_price(self) -> None:
        self._total_price = sum([item.items_price for item in self._cart])
        self._final_price = self._total_price + self._shipping_price

    def update_cart_items(self) -> str:
        status = {}
        for item in reversed(self._cart):
            stock_amount = item.tool.amount
            if stock_amount <= 0:
                status[item.tool.name] = "Out of stock"
                self._cart.remove(item)
            elif item.buy_amount > stock_amount:
                status[item.tool.name] = "Stock updated"
                item._buy_amount = stock_amount
                item.update_item()
        self.calculate_price()
        return status

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())
