from tool import Item
class Wishlist:
    def __init__(self) -> None:
        self._wish_product = [ ]
        self._quantity = 0
        self._price = 0.00

    def add_item(self, item_tool,buy_amount = 1): 
        for item in self._wish_product: 
            if item._tool == item_tool : 
                if item._buy_amount is not buy_amount: 
                    item.buy_amount = buy_amount
                return 
        new_item = Item(item_tool,buy_amount)
        self._wish_product.append(new_item)

    def set_item(self):
        pass

    def get_items(self,item_search):
        pass

    def delete_item(self,tool_delete):
        for item in self._wish_product:
            if item._tool == tool_delete:
                self._wish_product.remove(item)
                return
    def send_to_cart(self):
        pass

