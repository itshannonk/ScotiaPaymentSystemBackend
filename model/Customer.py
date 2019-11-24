from model.Invoice import Invoice

from typing import List

"""
This is a Customer who has a list of Invoices
"""


class Customer:
    name: str
    address: str
    id: str
    invoices: List[Invoice]
    type: str

    def __init__(self, name: str, address: str, id: str, invoices: List[Invoice], type: str) -> None:
        self.name = name
        self.address = address
        self.id = id
        self.invoices = invoices
        self.type = type

    def getcustomer(self) -> dict:
        temp = ''
        for invoice in self.invoices:
            temp += ' ' + invoice.getinvoice()
        print(temp)
        return {
            "Name": self.name,
            "Address": self.address,
            "ID": self.id,
            "Invoices": temp
        }
