import shoppingcart

class Order:
    def __init__(self, orders:list, price:float, shipping:str, status:str, delivery_time:str) -> None:
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

    @property
    def get_value(self):
        return self._orders

    def update_order(self):
        pass

    def __repr__(self) -> str:
        return "{}" .format(str(self._orders) +','+self._price +','+self._shipping +','+self._status +','+self._delivery_time)