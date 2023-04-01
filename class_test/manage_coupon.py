import sys
sys.path.append('./class_object/')
from category import TypeOfTool, SubtypeOfTool
from tool import Tool
from system import System 
from admin import Admin
    # ----------- manage coupon -----------------# 
if __name__ == '__main__':
    system = System()
    namning = Admin("Admin","1234","Pithakpong","Sawongnam","pithakpong0862@gmail.com")
    
    # add coupon
    coupon_list = system.add_coupon("1234","20","สว่านใหม่ เจาะทะลุทะลวง ดุดันไม่เกรงใจใคร")

    # modify coupon 
    
    search_coupon = system.search_coupon("1234")
    print(search_coupon._name)
    system.modify_coupon("1234","40","สว่านใหม่ ลดด่วนลดแรง!!")
    print(search_coupon._name) 

    # delete coupon  
    system.delete_coupon("1234") 
    print(system._server_coupon)