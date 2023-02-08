class Coupon:
    def __init__(self) -> None:
        self._discount_codes = []

    def add_coupon(self, code, discount_value) -> None:
        self._discount_codes.append(Discount(code, discount_value))

class Discount:
    def __init__(self, code, discount_value) -> None:
        self._code = code
        self._discount_value = discount_value
