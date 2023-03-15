import shoppingcart

class Order:
    def __init__(self, orders, price, shipping, status, delivery_time) -> None:
          self._orders = orders
          self._price = price
          self._shipping = shipping
          self._status = status
          self._delivery_time = delivery_time
          