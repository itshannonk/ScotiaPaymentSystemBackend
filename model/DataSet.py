import firebase_admin
from firebase import firebase
import json
from model import Invoice
from model import Status
from model import Item
firebase = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")

invoiceObject = Invoice.Invoice()
JSONversion = json.dumps(invoiceObject.__dict__)
# print(JSONversion)
# resultPut = firebase.put('Invoices','FEkg7hBAVxPgbwHHp2VmNwVCCwK2', {0:{"price":12.99, "status": "True"}, 1:{"price":12.99, "status": "True"}})
resultPut = firebase.put('Invoices','FEkg7hBAVxPgbwHHp2VmNwVCCwK2',
                         {'invoice1': {
                             'order': {
                                 'item name': 'new item',
                                 'quantity': 'quantity',
                                 'price': 'price'
                             },
                             'total price': 9.99,
                             'status': {
                                 'issued': True,
                                 'paid': False,
                                 'delivered': False
                             }
                         }})

#this is how you delete something. comment out the line below and see what it in firebase before uncommenting it out
result = firebase.delete("Business Owner/this is where the authID goes", "Name")
#this shows how you can update and add more children. Comment out the line below to see it
newresult = firebase.put("Business Owner","this is where the authID goes/Invoice", {3:JSONversion, 1:"gracececece"})
result = firebase.get('/Invoices', 'FEkg7hBAVxPgbwHHp2VmNwVCCwK2')
print(result)
