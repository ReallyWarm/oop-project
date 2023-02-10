class Item:
    def __init__(self, tool, amount, price) -> None: 
        self._item = tool
        self._amount = amount
        self._items_price = price * amount