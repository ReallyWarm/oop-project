class Tool:
    def __init__(self, code, name, description, brand, /
                 amount, image, price, type_of_tool) -> None:
          self._code = code
          self._name = name
          self._description = description
          self._brand = brand
          self._amount = amount
          self._price = price
          self._category = type_of_tool
          self._reviews = [ ]
          self._image = [image]
          self._wholesale = [ ]
