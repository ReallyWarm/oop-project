class Admin():
    def __init__(self, username, password, first_name, last_name, email) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._username = username
        self._password = password 
    def request_system(self,information,system,coupon_search = None):
        if information == "search_coupon" : 
            return system.search_coupon() 
        if information == "find_coupon"  :
            return system.find_coupon(coupon_search) 
    def manage_coupons(self,event,system,code = None,discount_value = None,name = None,modify_coupon = None,coupon = None): 
        if event == "create_coupon" : 
            return system.create_coupon(code,discount_value,name)
        if event == "modify_coupon" :  
            return system.modify_coupon(modify_coupon,code,discount_value,name)
        if event == "delete_coupon" : 
            return system.delete_coupon(coupon)
