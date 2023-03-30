class Wishlist:
    def __init__(self) -> None:
        self._wish_product = [ ]
        self._quantity = 0
        self._price = 0.00

    def add_item(self,item):
        if item not in self._wish_product:
            self._wish_product.append(item)
        else : 
            for i in self._wish_product: 
                if i._name == item._name : 
                    i = item 
                break

    def set_item(self):
        pass

    def get_items(self,item_search):
        for item in self._wish_product:
            if item._name == item_search._name: 
                return item 
            break

    def delete_item(self,item):
        self._wish_product.remove(item)

    def send_to_cart(self):
        pass

