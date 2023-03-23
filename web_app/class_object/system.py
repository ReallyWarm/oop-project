from category import Category
from shoppingcart import ShoppingCart
from tool import Item 
from customerinfo import CustomerInfo

class System():
    #Data of coupon and wholesale
    def __init__(self):
        self._category = Category()
        self._system_cart = ShoppingCart()
        self._server_coupon = []
        self._wholesale = []
        self._customerinfo = []

    @property
    def category(self):
        return self._category
    
    @property
    def system_cart(self):
        return self._system_cart
    
    def add_to_cart(self, tool, amount):
        item = Item(tool, amount)
        self._system_cart.add_item(item)

    def vertify_user(self):
        pass

    def find_coupon (self):
        pass  

    def login(self,username,password):
        pass

    def create_wholesale(self):
        pass

    def modify_wholesale(self):
        pass

    def delete_wholesale(self):
        pass

    def update_wholesale(self):
        pass

    def create_coupon(self):
        pass

    def modify_coupon(self):
        pass

    def delete_coupon(self):
        pass

    def update_coupon(self):
        pass

    def add_tool(self):
        pass

    def delete_tool(self):
        pass 
    


