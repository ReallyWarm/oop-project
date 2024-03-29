import sys
sys.path.append('./class_object/')
from wishlist import Wishlist
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from customerinfo import CustomerInfo  
from shoppingcart import ShoppingCart
if __name__ == '__main__':  

    # # ----------- manage wishlist by guest ----------- #
    system = System() 
    wishlist = Wishlist() 
    shoppingcart = ShoppingCart()
    category = system.category
    hand_tools_type = TypeOfTool(name='Hand tools')
    drills_type = SubtypeOfTool(name='Drills')
    nothing = SubtypeOfTool(name='None') 

    # Create test Tool objects in Catalog
    category.add_type(hand_tools_type)
    category.type_add_subtype(hand_tools_type, drills_type)
    category.type_add_subtype(hand_tools_type, nothing)

    # Create test Tool
    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    category.subtype_add_tool(drills_type, test_drill)

    # add to wishlist

    wishlist.add_item(test_drill, 10)
    print(wishlist)

    # add to cart 
    wishlist.set_item_amount(test_drill, 20) 
    print(wishlist)

     # remove product 
    wishlist.delete_item(test_drill) 
    print(wishlist)

    # ------------- manage wishlist by customer ------------- # 
    customer = CustomerInfo("unused","unused","kelvin","Lim","Kelvin1521@gmail.com","holly wood")

    # add to wishlist
    customer.my_wishlist.add_item(test_drill, 5) 
    # add same one
    customer.my_wishlist.add_item(customer.my_wishlist.get_item(test_drill).tool, 1)
    print(customer.my_wishlist)

    # remove product 
    customer.my_wishlist.delete_item(test_drill)
    print(customer.my_wishlist)

    customer.my_wishlist.add_item(test_drill, 10)
    print(customer.my_wishlist)

    customer.my_wishlist.send_to_cart(system.get_active_cart())
    print(customer.my_wishlist)
    print(system.get_active_cart())
