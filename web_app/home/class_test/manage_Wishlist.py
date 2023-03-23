import sys
sys.path.append('./web_app/class_object/') 
from wishlish import Wishlist
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from customerinfo import CustomerInfo  
from shoppingcart import ShoppingCart
if __name__ == '__main__':  

    # ----------- manage wishlist by guest ----------- #
    system = System() 
    wishlist = Wishlist() 
    shoppingcart = ShoppingCart()
    category = system.category
    hand_tools_type = TypeOfTool(name='Hand tools')
    drills_type = SubtypeOfTool(name='Drills')
    nothing = SubtypeOfTool(name='None') 

    # Create test Tool objects in Catalog
    category.add_type_of_tool(hand_tools_type)
    hand_tools_type.add_subtype(drills_type)
    hand_tools_type.add_subtype(nothing)

    test_drill = Tool('01x', 'Testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    drills_type.add_tool(test_drill)

    # add to wishlist
    wishlist.add_item(test_drill)
    print(wishlist._wish_product) 

    # add to cart 
    shoppingcart.add_item(wishlist.get_items(test_drill)) 
    print(shoppingcart._cart)
    wishlist.delete_item(test_drill) 
    print(wishlist._wish_product)

    # remove product 
    wishlist.add_item(test_drill)
    print(wishlist._wish_product) 
    wishlist.delete_item(test_drill) 
    print(wishlist._wish_product)

    # ------------- manage wishlist by customer ------------- # 
    customer = CustomerInfo("kelvin","Lim","Kelvin1521@gmail.com","holly wood")
    # add to wishlist
    customer.my_wishlist.add_item(test_drill) 

    # add to cart
    customer.my_shoppingcart.add_item(customer.my_wishlist.get_items(test_drill))
    print(customer.my_shoppingcart._cart[0])
    customer.my_wishlist.delete_item(test_drill)
    print(customer.my_wishlist._wish_product)

    # remove product 
    customer.my_wishlist.add_item(test_drill) 
    print(customer.my_wishlist._wish_product) 
    customer.my_wishlist.delete_item(test_drill) 
    print(customer.my_wishlist._wish_product)
