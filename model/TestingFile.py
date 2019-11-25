from flask import Request, Flask
from firebase import firebase
from model import Invoice
import json

invoiceObject = Invoice.Invoice()
JSONversion = json.dumps(vars(invoiceObject))
#print(JSONversion)

DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)



listOfInvoiceIDs = ""
userDATA = DATABASE.get('/Business Owner', None)
userDATA = userDATA.get('FEkg7hBAVxPgbwHHp2VmNwVCCwK2', None)
userDATA = userDATA.get('Invoices', None)
#print(userDATA)


userDATA = DATABASE.get('/Business Owner', 'FEkg7hBAVxPgbwHHp2VmNwVCCwK2')
inventorydb = userDATA.get("Invoices")
print(inventorydb)
listOfInvoiceIDs = ""
for key in inventorydb:
    print(key)
    # try and except block testing if there are multiple invoices
    try:
        int(key)
    except:
        # testing if there is only one invoice
        try:
            print(json.loads(inventorydb).get("id"))
        except:
            pass
            # print("no")
    listOfInvoiceIDs += key + ','
print(listOfInvoiceIDs[:-2])
