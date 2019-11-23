from firebase import firebase
import json
from model import Invoice
firebase = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")

invoiceObject = Invoice()
resultPut = firebase.put('Business Owner','this is where the authID goes', {'Name':'Grace', 'help':'me'})
print(resultPut)