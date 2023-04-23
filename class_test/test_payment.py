import sys
sys.path.append('./class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System
from customerinfo import CustomerInfo

if __name__ == '__main__':  
    system = System()
    category = system.category
    hand_tools_type = TypeOfTool(name='Hand tools')
    drills_type = SubtypeOfTool(name='Drills')

    # Create test Tool objects in Catalog
    category.add_type(hand_tools_type)
    category.type_add_subtype(hand_tools_type, drills_type)
    test_drill = Tool('01x', 'testing drill', 'POWER', 'idk', 10, None, 1000.00, 'Drills')
    faifa_drill = Tool('02x', 'faifa drill', 'POWER', 'idk', 12, None, 800.00, 'Drills')
    sawaan = Tool('03x', 'sawaan', 'go to hell', 'HEAVEN', 15, None, 2000.00, 'Drills')
    category.subtype_add_tool(drills_type, test_drill)
    category.subtype_add_tool(drills_type, faifa_drill)
    category.subtype_add_tool(drills_type, sawaan)

    customer = CustomerInfo("unused","unused",'Pornthep', 'Thammawong', 'firm@gmail.com', 'Kmitl')
    system.add_customerinfo(customer)
    customer.create_address('Pornthep','สำรวยกล้วย','Thailand','Phathumtani','Bangkuwat','sol.9/3 100/72','0982845321','12000')

    # assume logged in already -> same as using system.add_to_cart(...)
    customer.my_shoppingcart.add_item(test_drill, 5)
    customer.my_shoppingcart.add_item(faifa_drill, 10)

    print(customer.my_shoppingcart.cart)
    print('--------------------------------')

    # PAYMENT SUCCESS
    status = system.make_payment('1234567890123456', customer, 'Pornthep')
    print(status)
    print(customer.my_shoppingcart.cart)

    print('--------------------------------')
    print(customer.my_order)
    print('--------------------------------')

    # PAYMENT NO ITEM
    status = system.make_payment('1234567890123456', customer, 'Pornthep')
    print(status)
    print('--------------------------------')

    customer.my_shoppingcart.add_item(test_drill, 3)

    # INVALID CARD
    status = system.make_payment('not_numberwith16', customer, 'Pornthep')
    print(status)
    status = system.make_payment('12345', customer, 'Pornthep')
    print(status)

    print('--------------------------------')
    print(customer.my_shoppingcart.cart)
    print('--------------------------------')

    # PAYMENT WITH COUPON
    system.add_coupon("1234",10,"สว่านใหม่ เจาะทะลุทะลวง ดุดันไม่เกรงใจใคร")
    status = system.make_payment('1234567890123456', customer, 'Pornthep', '1234')
    print(status)

    print('--------------------------------')
    print(customer.my_order)
    print('--------------------------------')

    customer.my_shoppingcart.add_item(test_drill, 10)

    # You have already used the coupon
    status = system.make_payment('1234567890123456', customer, 'Pornthep', '1234')
    print(status)
    print('--------------------------------')

    # "Coupon not found"
    status = system.make_payment('1234567890123456', customer, 'Pornthep', 'No')
    print(status)






