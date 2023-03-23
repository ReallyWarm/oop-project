class Admin():
    def __init__(self, username, password, first_name, last_name, email,system) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._username = username
        self._password = password 
        self.system = system
    def request_system(self,information,coupon_search = None):

        if(information == "search_coupon" ) : 
            return (self.system).search_coupon() 
        if(information == "find_coupon" ) :
            return (self.system).find_coupon(coupon_search)
        