from .shipping import Shipping
from .review import Review
from .category import SubtypeOfTool
from .wholesale import Wholesale

class Tool:
    def __init__(self, code, name, description, brand, amount, image, price, /
                 subtype_of_tool, shipping_status, shipping_price, shipping_time, /
                 wholesale_amount, wholesale_discount) -> None:
          self._code = code
          self._name = name
          self._description = description
          self._brand = brand
          self._amount = amount
          self._image =  image
          self._price = price
          self._category = subtype_of_tool
          self._shipping = Shipping(shipping_status, shipping_price, shipping_time)
          self._reviews = []
          self._wholesale = Wholesale()
