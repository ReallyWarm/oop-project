import sys
sys.path.append('./class_object/')
from tool import Tool
from order import Order
from customerinfo import CustomerInfo
from system import System

if __name__ == '__main__':
    # Set up the clss object
    Sys = System()

    customer = [CustomerInfo("unused","unused",'Pornthep', 'Thammawong', 'firm@gmail.com', 'Kmitl'), 
                CustomerInfo('NorNor007', '$2b$12$DmZVZhN.hpSa.QbeXWfUzO5Nh8b5Csh7AvqYFZsTR6i8KfdWlg6Am','NorNor', 'Sawongnam', 'NorNor@gmail.com', 'Kmitl'), 
                CustomerInfo('PreeOhm','$2b$12$w4yNVfOcN36ylngAaAmW1etV8pD9H9ju0pbbeYFdbUaYof60CjA72','พรี่โอมใจเกเร', 'สองศรี', 'Thanasak@gmail.com', 'Kmitl'),
                CustomerInfo('KorphaiSK','$2b$12$3XJZVS.xPIG5NE46RspWZOsdQEbq3EFtKxMl7zB9.9XY9cf8283ny',"Prakrittipon", "Sommool", "korphaisk@gmail.com", "KMITL")]

    # add customer information to system
    for i in range(len(customer)):
        Sys.add_customerinfo(customer[i])

    # create address in customerinfo
    customer[0].create_address('Pornthep','สำรวยกล้วย','Thailand','Phathumtani','Bangkuwat','sol.9/3 100/72','0982845321','12000')
    customer[1].create_address('NorNor007','จารย์แดง จำกัด','Thailand','Udon Thani','-','-','0210567473','10010')
    customer[2].create_address('PreeOhm','ใจเกเร จำกัด','Thailand','Udon Thani','-','-','0810567473','10010')
    customer[3].create_address('KorphaiSK','KMIL','Thailand','Bangkok','Pha ya tai','sol.12 24/89','0901276842','11120')
    
    # create the example review and order
    order1 = Order([], 'x', '0', '34000', '0', '0', '34000', customer[0].get_address('Pornthep'))
    test_drill = Tool('01x', 'Testing drill', 'POWER',
                      'idk', 10, None, 1000.00, 'Drills')
    customer[3].create_review(test_drill, "test_review1", "good_tool", 4.5, "4/1/2023")

    #test result name is duplicate
    print()
    customer[3].create_address('KorphaiSK','KU','Thailand','Bangkok','Sapan','sol.12 24/89','02012389089','10000')

    print()
    
    print(Sys.customerinfos, end='\n')

    print()

    #get the addres in customerinfo
    print(customer[3].get_address('KorphaiSK'))
    
    for i in range(len(customer)):
        print(customer[i].address, end='\n')

    print()

    #edit address
    customer[1].get_address('NorNor007').edit_address(country='England',phone_number='0900563573')
    print(customer[1].address)

    print()
    
    # delete address 3 in list of customer
    customer[2].delete_address('PreeOhm')
    print(customer[2].address)
    print()

    #  check order
    customer[0].store_order(order1)
    print(customer[0].my_order[0])
    print('--------------------------------------')

    # # check review
    print(customer[3].my_reviewed[0])
