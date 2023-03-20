import shoppingcart

class Order:
    def __init__(self, orders, price, shipping, status, delivery_time) -> None:
# order is list of the tool that customer bought combine with the price of that tool
# price of shipping and total
# shipping shipping by who
# status status of shipping stage , update to the date somehow
# delivery_time, rely on the shipping company.
          self._orders = orders
          self._price = price
          self._shipping = shipping
          self._status = status
          self._delivery_time = delivery_time

    def get_value(self):
         pass

    def  set_value(self):
         pass

    def update_order(self):
         pass   
