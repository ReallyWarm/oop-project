import sys
sys.path.append('./oop-project/web_app/class_object/')
from system import System
from customerinfo import CustomerInfo
from address import Address
from order import Order
from review import Review

if __name__ == '__main__':
    # Set up the clss object
    Sys = System()
    
    customer = [CustomerInfo('Pornthep', 'Thammawong',
                             'firm@gmail.com', 'Kmitl')
                ,CustomerInfo('NorNor', 'Sawongnam',
                             'NorNor@gmail.com', 'Kmitl')
                ,CustomerInfo('พรี่โอมใจเกเร', 'สองศรี',
                             'Thanasak@gmail.com', 'Kmitl')]
    
    address = [ Address('Pornthep', 'Kmitl', 'Thailand',
                          '-', 'Phathumtani', '-', '0412320412', '12304')
   ,Address('NorNor', 'Kmitl', 'Thailand',
                          '-', 'Udontani', '-', '06341321321', '423423')
    ,Address('พรี่โอมใจเกเร', 'Kmitl', 'Thailand',
                          '-', 'Udontani', '-', '0512859258', '12000')]


    order1 = Order('ad12','34000','Pronthep','Success','12.00')
    review1 = Review('Pornthep','Good Product','-','12/11/2023')

    # add customer information to system
    for i in range (len(customer)):
        Sys.add_customerinfo(customer[i])
    

    # add address in customerinfo
    for i in range (len(address)):
        customer[i].add_address(address[i])
        
    
    print(Sys._customerinfo,end=' ')

    for i in range(len(customer)):
        print(customer[i]._addresses,end=' ')
    
    #edit address
    edit_add1 = address[0].edit_address('Pornthep', 'CU', 'Thailand',
                          '-', 'Phathumtani', '-', '0412320412', '12304')
    customer[0].update_edit_address(edit_add1)
    print(customer[0]._addresses[0])
    
    #delete address 3 in list of customer 
    del_add3 = customer[2].delete_address(address[2])
    print(customer[2]._addresses)
    
    #check order
    check_order1 =customer[0].store_order(order1)
    print(check_order1)
    
    #check review
    check_review1 = customer[0].store_review(review1)
    print(check_review1)
    
    for i in range(len(customer)):
        print(customer[i],end=' ')
 
  
    

    
   