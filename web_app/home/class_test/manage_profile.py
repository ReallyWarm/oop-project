import sys
sys.path.append('./web_app/class_object/')
from tool import Tool
from order import Order
from address import Address
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

    address = [Address('Pornthep', 'Kmitl', 'Thailand',
                       '-', 'Phathumtani', '-', '0412320412', '12304'), Address('NorNor', 'Kmitl', 'Thailand',
                                                                                '-', 'Udontani', '-', '06341321321', '423423'), Address('พรี่โอมใจเกเร', 'Kmitl', 'Thailand',
                                                                                                                                        '-', 'Udontani', '-', '0512859258', '12000')]

    # create the example review and order
    order1 = Order('ad12', '34000', 'Pronthep', 'Success', '12.00')
    test_drill = Tool('01x', 'Testing drill', 'POWER',
                      'idk', 10, None, 1000.00, 'Drills')
    customer[3].create_review(test_drill)
    customer_review = customer[3].store_review('Prakrittipon')

    # add customer information to system
    for i in range(len(customer)):
        Sys.add_customerinfo(customer[i])

    # add address in customerinfo
    for i in range(len(address)):
        customer[i].add_address(address[i])

    print(Sys._customerinfo, end='\n')

    print()

    for i in range(len(customer)):
        print(customer[i]._addresses, end='\n')

    print()

    # edit address
    address[0].edit_address('Pornthep', 'CU', 'Thailand',
                            '-', 'Phathumtani', '-', '0412320412', '12304')
    print(customer[0]._addresses[0])

    print()
    # delete address 3 in list of customer
    print(customer[2].delete_address(address[2]))
    print()

    # check order
    print(customer[0].store_order(order1))
    print('--------------------------------------')

    # check review
    print(customer_review)
