from typing import List

from model import Customer

from model import Invoice


class Supplier:
    name: str
    address: str
    id: str
    invoices: List[Invoice]
    customers: List[Customer]

    def __init__(self, name: str, address: str, id: str, invoices: List[Invoice], customers: List[Customer]):
        self.name = name
        self.address = address
        self.id = id
        self.invoices = invoices
        self.customers = customers
