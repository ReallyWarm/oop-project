class CustomerInfo:
    def __init__(self, first_name, last_name, email, company_name,address,my_wishlist,my_shoppingcart,my_order,my_review,used_coupon) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._company_name = company_name
        self._addresses = [ ]
        self.my_wishlist = my_wishlist
        self.my_shoppingcart = my_shoppingcart
        self.my_order = my_order
        self.my_review = my_review
        self.used_coupon = used_coupon

