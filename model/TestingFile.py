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
userDATA = DATABASE.get('/Business Owner', 'YwF7HkeUCkRUU6V00lkh2d0p5512')
print(userDATA)
userDATA = userDATA.get('Invoices', None)
print(userDATA)
#print(userDATA)

#print(userDATA)

#print(inventorydb)
listOfInvoiceIDs = ""
for key in userDATA:
    #print(key)
    # try and except block testing if there are multiple invoices
    try:
        #print(key)
        int(key)
    except:
        # testing if there is only one invoice
        try:
            #print(json.loads(inventorydb).get("id"))
            break
        except:
            pass
            # print("no")
    listOfInvoiceIDs += key + ','
    #print(listOfInvoiceIDs)
#print(listOfInvoiceIDs[:-1])
