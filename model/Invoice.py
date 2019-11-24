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
    items: List[Item]

    def __init__(self, id: int, total_price: float, status: Status, items: List[Item]):
        self.id = id
        self.total_price = total_price
        self.status = status
        self.items = items

    def getinvoice(self):
        return {
            "ID": self.id,
            "Total Price": self.total_price,
            "Status": self.status,
            "Items": self.items
        }
