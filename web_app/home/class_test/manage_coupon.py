import sys
sys.path.append('./web_app/class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from admin import Admin
    # ----------- manage coupon -----------------# 
if __name__ == '__main__':
    system = System()
    namning = Admin("Admin","1234","Pithakpong","Sawongnam","pithakpong0862@gmail.com",system)
    # Inspect coupon
    coupon_list = namning.request_system("search_coupons") 
    print(coupon_list) 

    # create coupon and add coupon
    coupon = (namning.system).create_coupon("1587","15","ลดสนั่น ไก่จ้อราคาพิเศษ 15เปอร์เซ็น")
    system.update_coupon("add",coupon) 
    coupon_list = system.search_coupon()
    print(coupon_list[0]._name) 

    # modify coupon 
    search_coupon = namning.request_system("find_coupon","ลดสนั่น ไก่จ้อราคาพิเศษ 15เปอร์เซ็น") 
    print(search_coupon._name)
    modify_coupon = namning.system.modify_coupon(search_coupon,"5642","20","เครื่องเจาะใหม่ ดุดันไม่เกรงใจใคร")
    print(modify_coupon._name) 
    system.update_coupon("modify",search_coupon,modify_coupon) 
    print(system.search_coupon()[0]._name)

    # delete coupon 
    search_coupon = namning.request_system("find_coupon","เครื่องเจาะใหม่ ดุดันไม่เกรงใจใคร") 
    print(search_coupon._name) 
    delete_coupon = namning.system.delete_coupon(search_coupon)
    print(delete_coupon._name) 
    system.update_coupon("delete",search_coupon) 
    print(system.search_coupon())

