from flask import Request, Flask
from firebase import firebase
from model import Invoice
import pyrebase
import json
from flask import *
app = Flask(__name__)

invoiceObject = Invoice.Invoice()
JSONversion = json.dumps(vars(invoiceObject))
#print(JSONversion)

DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)

listOfInvoiceIDs = ""
userDATA = DATABASE.get('/Business Owner', 'YwF7HkeUCkRUU6V00lkh2d0p5512')
userDATA = userDATA.get('Invoices', None)
#print(userDATA)

#print(userDATA)

#print(inventorydb)
# listOfInvoiceIDs = ""
# for key in userDATA:
#     #print(key)
#     # try and except block testing if there are multiple invoices
#     try:
#         #print(key)
#         int(key)
#     except:
#         # testing if there is only one invoice
#         try:
#             #print(json.loads(inventorydb).get("id"))
#             break
#         except:
#             pass
            # print("no")
    # listOfInvoiceIDs += key + ','
    #print(listOfInvoiceIDs)
#print(listOfInvoiceIDs[:-1])


# config = {
#         "apiKey": "AIzaSyCkjsbkDtmKUU_77XHDYfNnBZS1E3F82iw",
#         "authDomain": "csc207-tli.firebaseapp.com",
#         "databaseURL": "https://csc207-tli.firebaseio.com",
#         "projectId": "csc207-tli",
#         "storageBucket": "csc207-tli.appspot.com",
#         "messagingSenderId": "707734809591",
#         "appId": "1:707734809591:web:313eb97ac705e6ebb21cf2",
#         "measurementId": "G-VQCPWR41LV"
#     }
#
# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# user = auth.create_user_with_email_and_password("helloamy@gmail.com", "password")
# userID = user["localId"]
# DATABASE.put("Business Owner", userID,
#              {
#              "Address": "address",
#              "Email": "helloamy@gmail.com",
#              "Name": "name",
#              "Password": "password"
#              })

invoice_information = ""
inventorydb = DATABASE.get('Invoices', "FEkg7hBAVxPgbwHHp2VmNwVCCwK2")
inventorydb = inventorydb.get("invoice1", "total price")
print(inventorydb)
inventorydb = inventorydb.get("total price", None)
print(inventorydb)
try:
    inventorydb = DATABASE.get('Invoices', "FEkg7hBAVxPgbwHHp2VmNwVCCwK2")
    invoice_information += inventorydb.get("total price", None)
    invoice_information += inventorydb.get("invoice1", "delivered")
    invoice_information += inventorydb.get("invoice1", "issued")
    invoice_information += inventorydb.get("invoice1", "paid")
    for key in inventorydb:
        invoice_information += str(key) + ','
    print(invoice_information[:-1])
except:
    print("no")

