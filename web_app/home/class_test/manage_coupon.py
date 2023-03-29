import sys
sys.path.append('./web_app/class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from admin import Admin
    # ----------- manage coupon -----------------# 
if __name__ == '__main__':
    system = System()
    namning = Admin("Admin","1234","Pithakpong","Sawongnam","pithakpong0862@gmail.com")
    # Inspect coupon
    coupon_list = namning.request_system("search_coupons",system) 
    print(coupon_list) 

    # create coupon and add coupon
    coupon = namning.manage_coupons("create_coupon",system,code = "1587",discount_value = 15,name = "ลดสนั่น ไก่จ้อราคาพิเศษ 15เปอร์เซ็น")
    system.update_coupon("add",coupon) 
    coupon_list = system.search_coupon()
    print(coupon_list[0]._name) 

    # modify coupon 
    search_coupon = namning.request_system("find_coupon",system,"ลดสนั่น ไก่จ้อราคาพิเศษ 15เปอร์เซ็น") 
    print(search_coupon._name)
    modify_coupon = namning.manage_coupons("modify_coupon",system,modify_coupon = search_coupon,code = "5642",discount_value = 20,name = "ไขควงใหม่ หมุนทีเดียวเข้าเกลียวเลย")
    print(modify_coupon._name) 
    system.update_coupon("modify",search_coupon,modify_coupon) 
    print(system.search_coupon()[0]._name)

    # delete coupon 
    search_coupon = namning.request_system("find_coupon",system,"ไขควงใหม่ หมุนทีเดียวเข้าเกลียวเลย") 
    print(search_coupon._name) 
    delete_coupon = namning.manage_coupons("delete_coupon",system,coupon = search_coupon)
    print(delete_coupon._name) 
    system.update_coupon("delete",search_coupon) 
    print(system.search_coupon())