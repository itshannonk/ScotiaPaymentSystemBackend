from typing import List

from model.Invoice import Invoice

from model.Customer import Customer

"""
This is the Driver
They have a selected list of Invoices and Cus
"""


class Distributer:
    name: str
    id: str
    invoices: List[Invoice]
    customers: List[Customer]

    def __init__(self, name: str, id: str, invoices: List[Invoice], customers: List[Customer]):
        self.name = name
        self.id = id
        self.invoices = invoices
        self.customers = customers

    def getDistributer(self):
        return {
            "Name": self.name,
            "ID": self.id,
            "Invoices": self.invoices,
            "Customers": self.customers
        }
