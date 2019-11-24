"""
This is an Item that appears on an Invoice.
"""


class Item:
    name: str
    price: float
    id: int

    def __init__(self, name: str, price: float, id: int):
        self.name = name
        self.price = price
        self.id = id

    def getitem(self):
        return {
            "Name": self.name,
            "Price": self.price,
            "ID": self.id
        }
