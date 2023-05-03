from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from tool import Tool
    from shoppingcart import ShoppingCart
from tool import Item

class Wishlist:
    def __init__(self) -> None:
        self._wish_product = []
        self._total_price = 0.00

    @property
    def total_price(self) -> float: 
        return self._total_price
    
    @property
    def wish_product(self) -> list:
        return self._wish_product
    
    def get_item(self, tool:'Tool') -> 'Item' or None:
        for wish_item in self.wish_product:
            if tool is wish_item.tool:
                return wish_item
        return None

    def add_item(self, tool:'Tool', buy_amount:int) -> None:
        wish_item = self.get_item(tool)
        if wish_item is not None:
            wish_item.set_buy_amount(buy_amount)
        else:
            self._wish_product.append(Item(tool, buy_amount))
        self.calculate_price()

    def set_item_amount(self, tool:'Tool', buy_amount:int) -> None:
        item = self.get_item(tool)
        item.set_buy_amount(buy_amount)
        self.calculate_price()

    def delete_item(self, tool:'Tool') -> None:
        item = self.get_item(tool)
        self._wish_product.remove(item)
        self.calculate_price()

    def clear_wishlist(self) -> None:
        self._wish_product.clear()
        self.calculate_price()

    def update_wish_items(self) -> None:
        for item in self._wish_product:
            item.update_item()

    def send_to_cart(self, cart:'ShoppingCart') -> None:
        self.update_wish_items()
        for wish_item in self.wish_product:
            cart.add_by_item(wish_item)
        self.clear_wishlist()

    def calculate_price(self) -> None:
        self._total_price = sum([item.items_price for item in self._wish_product])

    def __str__(self) -> str:
        return str(self.__class__)+'\n'+', '.join(f'{key} : {value}' for key, value in self.__dict__.items())