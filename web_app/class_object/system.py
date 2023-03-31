from category import Category
from shoppingcart import ShoppingCart
from tool import Item
from discount import Coupon

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
    
    def search_coupon(self,coupon_code): 
        for coupon in self._server_coupon:
            if coupon._code == coupon_code: 
                return coupon
            
    def add_to_cart(self, tool, amount):
        item = Item(tool, amount)
        self._system_cart.add_item(item)

    def vertify_user(self):
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

    def add_coupon(self,code,discount_value,name):  
        new_coupon = Coupon(code,discount_value,name)
        self._server_coupon.append(new_coupon)

    def modify_coupon(self,coupon_code,new_discount_value = None,new_name = None):
        for coupon in self._server_coupon :
            if coupon._code == coupon_code:  
                if coupon.name is not None : 
                    coupon.name = new_name
                if coupon.discount_value is not None :
                    coupon.discount_value= new_discount_value
                return 

    def delete_coupon(self,coupon_code):
        for coupon in self._server_coupon: 
            if coupon._code == coupon_code:
                self._server_coupon.remove(coupon) 
                return
    def add_tool(self):
        pass

    def delete_tool(self):
        pass 