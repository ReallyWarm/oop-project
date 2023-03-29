class Coupon:
    def __init__(self, code, discount_value,name) -> None:
        self._name = name
        self._code = code
        self._discount_value = discount_value

class Wholesale:
    def __init__(self, amount, discount_value) -> None:
        self._amount = amount
        self._discount_value = discount_value