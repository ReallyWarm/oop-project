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
    customer1 = CustomerInfo('Pornthep', 'Thammawong',
                             'firm@gmail.com', 'Kmitl')
    customer2 = CustomerInfo('NorNor', 'Sawongnam',
                             'NorNor@gmail.com', 'Kmitl')
    customer3 = CustomerInfo('พรี่โอมใจเกเร', 'สองศรี',
                             'Thanasak@gmail.com', 'Kmitl')
    
    adderess1 = Address('Pornthep', 'Kmitl', 'Thailand',
                          '-', 'Phathumtani', '-', '0412320412', '12304')
    adderess2 = Address('NorNor', 'Kmitl', 'Thailand',
                          '-', 'Udontani', '-', '06341321321', '423423')
    adderess3 = Address('พรี่โอมใจเกเร', 'Kmitl', 'Thailand',
                          '-', 'Udontani', '-', '0512859258', '12000')

    order1 = Order('ad12','34000','Pronthep','Success','12.00')
    review1 = Review('Pornthep','Good Product','-','12/11/2023')

    # add customer information to system
    Sys.add_customerinfo(customer1)
    Sys.add_customerinfo(customer2)
    Sys.add_customerinfo(customer3)

    # add address in customerinfo
    adderess1_adderess = customer1.add_addresse(adderess1)
    adderess2_adderess = customer2.add_addresse(adderess2)
    adderess3_adderess = customer3.add_addresse(adderess3)
    
    print(Sys._customerinfo)
    print(customer1._addresses[0])
    print(customer2._addresses[0])
    print(customer3._addresses[0])
    
    #edit address
    edit_add1 = adderess1.edit_addresse('Pornthep', 'CU', 'Thailand',
                          '-', 'Phathumtani', '-', '0412320412', '12304')
    customer1.update_edit_addresse(edit_add1)
    print(customer1._addresses[0])
    
    #delete address
    del_add3 = customer3.delete_addresse(adderess3)
    print(customer3._addresses)
    
    #check order
    check_order1 =customer1.store_order(order1)
    print(check_order1)
    
    #check review
    check_review1 = customer1.store_review(review1)
    print(check_review1)
    
    print(customer1)
    print(customer2)
    print(customer3)
  
 
  
    

    
   