from typing import List

from model.Customer import Customer

from model.Invoice import Invoice

"""
CocaCola is our supreme overlord. 
"""


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


    def getsupplier(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "ID": self.id,
            "Invoices": self.invoices,
            "Customers": self.customers
        }