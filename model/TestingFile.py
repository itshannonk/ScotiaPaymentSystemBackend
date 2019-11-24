from flask import Request, Flask
from firebase import firebase
from model import Invoice
import json

invoiceObject = Invoice.Invoice()
JSONversion = json.dumps(vars(invoiceObject))
print(JSONversion)

DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


listOfInvoiceIDs = ""
userDATA = DATABASE.get('/Business Owner', "FEkg7hBAVxPgbwHHp2VmNwVCCwK2")
inventorydb = userDATA.get("Invoices")
totalInvoices = 0
for key in inventorydb:
    listOfInvoiceIDs += key + ','
    totalInvoices += 1
print(listOfInvoiceIDs + str(totalInvoices))
