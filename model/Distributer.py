from typing import List
from model import Invoice, Customer


class Distributer:
    name: str
    id: str
    invoices: List[Invoice]
    customers: List[Customer]

    def __init__(self, name: str, id : str, invoices : List[Invoice], customers : List[Customer]):
        self.name = name
        self.id = id
        self.invoices = invoices
        self.customers = customers
