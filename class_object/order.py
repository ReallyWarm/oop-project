from datetime import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from address import Address

class Order:
    def __init__(self, orders:list, payment_id:str, payment_date:datetime, total_price:float, shipping_price:float, discount_price:float, final_price:float, 
                 address:'Address', shipment:str='EMS', status:str='In the product management process.', delivery_time:datetime=None) -> None:
        self._orders = orders
        self._payment_id = payment_id
        self._payment_date = payment_date
        self._total_price = total_price
        self._shipping_price = shipping_price
        self._discount_price = discount_price
        self._final_price = final_price
        self._address = address
        self._shipment = shipment
        self._status = status
        self._delivery_time = delivery_time        

    @property
    def orders(self):
        return self._orders
    
    @property
    def payment_id(self):
        return self._payment_id
    
    @property
    def payment_date(self):
        return self._payment_date
    
    @property
    def total_price(self):
        return self._total_price
    
    @property
    def shipping_price(self):
        return self._shipping_price
    
    @property
    def discount_price(self):
        return self._discount_price
    
    @property
    def final_price(self):
        return self._final_price
    
    @property
    def address(self):
        return self._address
    
    @property
    def shipment(self):
        return self._shipment
    
    @property
    def status(self):
        return self._status
    
    @property
    def delivery_time(self):
        return self._delivery_time

    def update_order(self, status:str='In the delivery process', delivery_time:datetime=datetime.now()):
        self._status = status
        self._delivery_time = delivery_time

    def __repr__(self) -> str:
        return "{}" .format(str(self._orders) +','+self._payment_id+','+self._total_price +','+self._status +','+self._delivery_time)