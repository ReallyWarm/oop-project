from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from customerinfo import CustomerInfo
from category import Category
from shoppingcart import ShoppingCart
from wishlist import Wishlist
from discount import Coupon, Wholesale
from tool import Tool
from admin import Admin
from payment import Payment
from auth import Authenticate
from typing import TYPE_CHECKING

class System():
    # Data of coupon and wholesale
    def __init__(self) -> None:
        self._authentication = Authenticate()
        self._category = Category()
        self._system_cart = ShoppingCart()
        self._server_coupons = []
        self._wholesales = []
        self._customerinfos = []
        self._admins = []

    @property
    def auth(self) -> Authenticate:
        return self._authentication

    @property
    def customerinfos(self) -> list:
        return self._customerinfos

    @property 
    def server_coupons(self) -> list : 
        return self._server_coupons
    
    @property 
    def wholesales(self) -> list:
        return self._wholesales
    
    @property
    def category(self) -> Category:
        return self._category
    
    @property
    def system_cart(self) -> ShoppingCart:
        return self._system_cart
    
    def get_active_cart(self) -> ShoppingCart:
        try:
            current_user = self.get_login()
            return current_user.my_shoppingcart
        except:
            return self._system_cart
        
    def get_wishlist(self) -> Wishlist | None:
        try:
            current_user = self.get_login()
            return current_user.my_wishlist
        except:
            return None
    
    def search_user(self, username:str) -> CustomerInfo | Admin:
        for user in self._customerinfos:
            if user.username == username:
                return user
        for admin_user in self._admins:
            if admin_user.username == username:
                return admin_user
    
    def search_wholesale(self, code:str) -> Wholesale:
        for wholesale in self._wholesales:
            if wholesale.code == code : 
                return wholesale

    def search_coupon(self, coupon_code:str) -> Coupon: 
        for coupon in self._server_coupons:
            if coupon.code == coupon_code: 
                return coupon
            
    def get_current_user(self) -> dict:
        return self._authentication.get_current_user()
            
    def get_login(self) -> CustomerInfo | Admin:
        login_user = self.get_current_user()
        user_name = login_user.get('user')
        current_user = self.search_user(user_name)
        return current_user
    
    def check_admin(self) -> bool:
        user = self.get_current_user()
        admin_username = user.get('user')
        for admin in self._admins:
            if admin.username == admin_username and isinstance(admin, Admin):
                return True
        return False

    def add_to_cart(self, tool:Tool, buy_amount:int) -> str:
        active_cart = self.get_active_cart()
        if tool.amount < buy_amount:
            return "Item amount exceeds the available tool in stock"
        else:
            active_cart.add_item(tool, buy_amount)

    def add_to_wishlist(self, tool:Tool, buy_amount:int) -> str:
        customer_wishlist = self.get_wishlist()
        if customer_wishlist is None:
            return "Can not get wishlist"
        elif tool.amount < buy_amount:
            return "Item amount exceeds the available tool in stock"
        else:
            customer_wishlist.add_item(tool, buy_amount)

    def wishlist_to_cart(self, wishlist:Wishlist, cart:ShoppingCart) -> bool:
        if wishlist is not None and cart is not None:
            wishlist.send_to_cart(cart)
            return True
        return False

    def add_admin(self, admin:Admin) -> None:
        self._admins.append(admin)

    def add_customerinfo(self, customer:CustomerInfo) -> None:
        self._customerinfos.append(customer)

    def add_wholesale(self, wholesale_code:str, amount:int, discount_value:int) -> None: 
        wholesale = Wholesale(wholesale_code,amount,discount_value)
        self._wholesales.append(wholesale)

    def modify_wholesale(self, wholesale_code:str, new_amount:int = None, new_discount_value:int = None) -> None:
        for wholesale in self.wholesales : 
            if wholesale.code == wholesale_code: 
                if new_amount is not None : 
                    wholesale.amount = new_amount 
                if new_discount_value is not None : 
                    wholesale.discount_value = new_discount_value
                return

    def delete_wholesale(self, wholesale_code:str) -> None:
        tools = self._category.search_by_name('')
        for key,value in tools.items(): 
            for wholesale in value.wholesales : 
                if wholesale.code == wholesale_code: 
                    value.wholesales.remove(wholesale)
        for wholesale in self.wholesales : 
            if wholesale.code == wholesale_code :
                self.wholesales.remove(wholesale)
                del wholesale 
                return

    def add_coupon(self, coupon_code:str, discount_value:int, name:str) -> None:  
        new_coupon = Coupon(coupon_code,discount_value,name)
        self._server_coupons.append(new_coupon)

    def modify_coupon(self, coupon_code:str, new_discount_value:int = None, new_name:int = None) -> None:
        for coupon in self._server_coupons :
            if coupon.code == coupon_code:  
                if coupon.name is not None : 
                    coupon.name = new_name
                if coupon.discount_value is not None :
                    coupon.discount_value= new_discount_value
                return 

    def delete_coupon(self, coupon_code:str) -> None:
        for coupon in self._server_coupons: 
            if coupon.code == coupon_code:
                self._server_coupons.remove(coupon) 
                return
            
    def create_tool(self, product_code:str, tool_name:str, tool_description:str, tool_brand:str, tool_amount:int, tool_image:str, tool_price:float, type_of_tool:str) -> None:
        new_tool = Tool(product_code, tool_name, tool_description, tool_brand, tool_amount, tool_image, tool_price, type_of_tool)
        self._category.subtype_name_add_tool(type_of_tool, new_tool)
        
    def delete_tool(self, tool:Tool) -> None:
        for tool_in_list in self._category._all_tools: 
            if tool_in_list.name == tool.name:
                self._category._all_tools.remove(tool_in_list)
                
        for subtype in self._category._all_subtypes:
            if subtype.subtypename == tool.type_of_tool:
                for tool_in_subtype in subtype.tools_list:
                    if tool_in_subtype.name == tool.name:
                        subtype.tools_list.remove(tool_in_subtype)

    def modify_tool(self, tool:Tool, name:str=None, description:str=None, brand:str=None, price:float=None, code:str=None ,type_of_tool:str=None) -> None:
        if name is not None :
            tool.change_name(name)
        if description is not None :
            tool.change_description(description)
        if brand is not None :
            tool.change_brand(brand)
        if price is not None :
            tool.change_price(price)
        if code is not None :
            tool.change_code(code)
        if type_of_tool is not None :
            tool.change_type_of_tool(type_of_tool)
            search_type = self._category.search_by_subtype(type_of_tool)
            selected_type = search_type[type_of_tool]
            self.delete_tool(tool)
            self._category.subtype_add_tool(selected_type, tool)

    def make_payment(self, card:str, current_user:CustomerInfo, address_name:str, coupon_code:str = None) -> str:
        shoppingcart = current_user.my_shoppingcart
        total_price = shoppingcart.total_price
        if total_price <= 0:
            return "You must add items to your shopping cart before paying"
        
        coupon = None
        discount_value = 0
        if coupon_code is not None:
            coupon = self.search_coupon(coupon_code) 
            if(coupon is None): 
                return "Coupon not found"
            if current_user.check_used_coupon(coupon_code):
                return "You have already used the coupon"
            discount_value = coupon.discount_value

        shoppingcart.update_cart_items()
        payment = Payment(total_price, shoppingcart.shipping_price, card, discount_value)
        status = payment.make_payment()
        if status == "Payment success":
            # store used coupon
            if coupon is not None:
                current_user.store_used_coupon(coupon)
            # store new order
            address = current_user.get_address(address_name)
            order_items = [item for item in shoppingcart.cart]
            new_order = payment.create_order(order_items, address)
            current_user.store_order(new_order)
            # clear cart
            current_user.my_shoppingcart.clear_cart()
            # update tool amount in shop
            for item in order_items:
                item.tool.amount = item.tool.amount - item.buy_amount
        del payment

        return status
