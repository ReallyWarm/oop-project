from category import Category,SubtypeOfTool,TypeOfTool
from shoppingcart import ShoppingCart
from tool import Item, Tool
from discount import Coupon


class System():
    # Data of coupon and wholesale
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

    def search_coupon(self): 
        return self._server_coupon

    def add_to_cart(self, tool, amount):
        item = Item(tool, amount)
        self._system_cart.add_item(item)

    def add_customerinfo(self, customer):
        self._customerinfo.append(customer)

    def vertify_user(self):
        pass

    def find_coupon (self,search_coupon):
        for coupon in self._server_coupon: 
            if coupon._name == search_coupon : 
                return coupon 

    def login(self, username, password):
        pass

    def create_wholesale(self):
        pass

    def modify_wholesale(self):
        pass

    def delete_wholesale(self):
        pass

    def update_wholesale(self):
        pass
    @staticmethod
    def create_coupon(code,discount_value,name):
        return Coupon(code,discount_value,name)

    def modify_coupon(self,modify_coupon,code,discount_value,name):
        for i in range(len(self._server_coupon)):  
            if (self._server_coupon[i])._name == modify_coupon._name : 
                return Coupon(code,discount_value,name)
            break

    def delete_coupon(self,coupon):
        for i in self._server_coupon: 
            if i._name == coupon._name:  
                return i
                #self._server_coupon.remove(i)
            break

    def update_coupon(self,task,coupon,modify_coupon = None):
        if task == "modify": 
            for i in range(len(self._server_coupon)):
                if (self._server_coupon[i])._name == coupon._name : 
                    self._server_coupon[i] = modify_coupon
                break
        elif task == "add": 
            self._server_coupon.append(coupon)

        elif task == "delete":
            self._server_coupon.remove(coupon)

    def add_tool(self):
        tool_name = input('Enter tool name:')
        self._tool_description = input('Enter tool_description:')
        self._tool_brand = input('Enter tool_brane:')
        self._tool_price = input('Enter tool price:')
        self._tool_category = input('Enter tool_category:')
        self._tool_review = []
        self._tool_image = []
        self._tool_wholesale = []
        #type_of_tool = TypeOfTool(name=input('Enter type of tool:'))
        #subtype_of_tool = SubtypeOfTool(name=input('Enter subtype of tool:'))
        tool_name = Tool(tool_name, self._tool_description, self._tool_brand, self._tool_price, self._tool_category, self._tool_review,\
                          self._tool_image,self._tool_wholesale)
        #self.category.add_type_of_tool(type_of_tool)
        #TypeOfTool.add_subtype(subtype_of_tool)
        #SubtypeOfTool.add_tool(tool_name)
        #print(SubtypeOfTool.tools_list)

    def delete_tool(self, will_delete_tool):
        del will_delete_tool
        #search by name or category
        #self._will_delete_tool = A
