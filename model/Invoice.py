from model.Status import Status

from model.Item import Item

from typing import List

"""
This is the Invoice of a Customer
It contains a list of Items and the Status of the delivery
"""


class Invoice:
    id: int
    total_price: float
    status: Status
    items: List[Item.Item]

    def __init__(self):
        self.id = 3
        self.total_price = 12.99
        #self.status = Status.Status(True, True, False)
        #self.items = [Item.Item("cocacola", 12.33, 2), Item.Item("cocacola", 12.33, 2)]

    def getinvoice(self):
        return {
            "ID": self.id,
            "Total Price": self.total_price,
            "Status": self.status,
            "Items": self.items
        }
