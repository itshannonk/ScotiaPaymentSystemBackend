from firebase import firebase
import json
from model import Invoice
from model import Status
from model import Item
firebase = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")

invoiceObject = Invoice.Invoice(3)
JSONversion = json.dumps(vars(invoiceObject))
print(JSONversion)
resultPut = firebase.put('Business Owner','this is where the authID goes', {'Name':'Grace', 'help':'me', 'invoice':JSONversion})
print(resultPut)