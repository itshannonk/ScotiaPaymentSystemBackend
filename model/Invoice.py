from model import Status, Item
from typing import List


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

