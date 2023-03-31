import sys
sys.path.append('./oop-project/web_app/class_object/')
from tool import Tool
from order import Order
from customerinfo import CustomerInfo
from system import System

if __name__ == '__main__':
    # Set up the clss object
    Sys = System()

    customer = [CustomerInfo('Pornthep', 'Thammawong',
                             'firm@gmail.com', 'Kmitl'), CustomerInfo('NorNor', 'Sawongnam',
                                                                      'NorNor@gmail.com', 'Kmitl'), CustomerInfo('พรี่โอมใจเกเร', 'สองศรี',
                                                                                                                 'Thanasak@gmail.com', 'Kmitl'),
                CustomerInfo("Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")]


    # create the example review and order
    order1 = Order('ad12', '34000', 'Pronthep', 'Success', '12.00')
    test_drill = Tool('01x', 'Testing drill', 'POWER',
                      'idk', 10, None, 1000.00, 'Drills')
    customer[3].create_review(test_drill)
    customer_review = customer[3].store_review('Prakrittipon')

    # add customer information to system
    for i in range(len(customer)):
        Sys.add_customerinfo(customer[i])

    # create address in customerinfo
    customer[0].create_address('Pornthep','สำรวยกล้วย','Thailand','Phathumtani','Bangkuwat','sol.9/3 100/72','0982845321','12000')
    customer[1].create_address('NorNor','จารย์แดง จำกัด','Thailand','Udon Thani','-','-','0210567473','10010')

    customer[2].create_address('พรี่โอมใจเกเร','ใจเกเร จำกัด','Thailand','Udon Thani','-','-','0810567473','10010')
    customer[3].create_address('Prakrittipon','KMIL','Thailand','Bangkok','Pha ya tai','sol.12 24/89','0901276842','11120')


    print(Sys._customerinfo, end='\n')

    print()

    for i in range(len(customer)):
        print(customer[i]._addresses, end='\n')

    print()

    #edit address
    customer[0]._addresses[0].edit_address(country='England',phone_number='0900563573')
    print(customer[0]._addresses)

    print()
    
    # # delete address 3 in list of customer
    customer[2].delete_address(customer[2]._addresses[0])
    print(customer[2]._addresses)
    print()

    # # check order
    print(customer[0].store_order(order1))
    print('--------------------------------------')

    # check review
    print(customer_review)
