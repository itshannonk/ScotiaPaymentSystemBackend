from model import Status, Item
from typing import List


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

