from flask import Request, Flask
from firebase import firebase
from model import Invoice
import json

invoiceObject = Invoice.Invoice()
JSONversion = json.dumps(vars(invoiceObject))
print(JSONversion)

DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


userDATA = DATABASE.get('/Business Owner', "FEkg7hBAVxPgbwHHp2VmNwVCCwK2")
print(userDATA)
inventorydb = userDATA.get("Invoices")
totalInvoices = 0
for key in inventorydb:
    print(key)
    print(inventorydb[key])
    totalInvoices += 1
