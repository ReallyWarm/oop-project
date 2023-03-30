from tool import Tool, Item
from shoppingcart import ShoppingCart

class Wishlist:
    def __init__(self) -> None:
        self._wish_product = []
        self._quantity = 0
        self._price = 0.00

    @property
    def wish_product(self):
        return self._wish_product
    
    def find_item(self, tool:Tool):
        for wish_item in self.wish_product:
            if tool is wish_item.tool:
                return wish_item
        return None

    def add_item(self, tool:Tool, buy_amount:int):
        wish_item = self.find_item(tool)
        if wish_item is not None:
            wish_item.set_buy_amount(buy_amount)
        else:
            self._wish_product.append(Item(tool, buy_amount))

    def set_item_amount(self, tool:Tool, buy_amount:int):
        item = self.get_items(tool)
        item.set_buy_amount(buy_amount)

    def get_items(self, tool:Tool):
        for wish_item in self.wish_product:
            if tool == wish_item.tool:
                return wish_item 

    def delete_item(self, tool:Tool):
        item = self.get_items(tool)
        self._wish_product.remove(item)

    def send_to_cart(self, cart:ShoppingCart):
        for wish_item in self.wish_product:
            cart.add_by_item(wish_item)
        self._wish_product.clear()

    def calculate_price(self):
        pass