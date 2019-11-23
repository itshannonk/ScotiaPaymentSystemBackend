from model import Invoice
from typing import List


class Customer:
    name: str
    address: str
    id: str
    invoices: List[Invoice]

    def __init__(self, name : str, address : str, id : str, invoices : List[Invoice]):
        self.name = name
        self.address = address
        self.id = id
        self.invoices = invoices



