from model.Status import Status

from model.Item import Item

from typing import List

"""
This is the Invoice of a Customer
It contains a list of Items and the Status of the delivery
"""
import json


class Invoice:
    id: int
    total_price: float

    # status: Status
    # items: List[Item]

    def __init__(self):
        self.id = 3
        self.total_price = 12.99
        self.delivered = True
        self.issued = True
        self.paid = False

        # right now, it is storing the items in a list where the item objects in the list are in a JSON string format"
        # because the issue with converting an object like Invoice into a string
        # is that the inner objects are not 'serializable'
        item = Item("cocacola", 12.33, 2)
        item2 = Item("cocacoladiet", 12.66, 5)
        self.items = [json.dumps(vars(item)), json.dumps(vars(item2))]

        # self.status = Status(True, True, False)
        # self.items = [Item("cocacola", 12.33, 2), Item("cocacola", 12.33, 2)]

    def change_delivered(self, delivered):
        self.delivered = delivered
        return self.delivered

    # must input an item
    def input_item(self, item):
        self.items.append(json.dumps(vars(item)))
