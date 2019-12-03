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
# userDATA = DATABASE.get('/Business Owner', 'YwF7HkeUCkRUU6V00lkh2d0p5512')
# userDATA = userDATA.get('Invoices', None)
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


def create_invoice(item_dict: dict, userID: str, invoiceID: str):
    """

    :param item_dict:key is "item name", value is list like ["5", "4.5"], "5"
    is quatity and "4.5" is price
    {"apple": ["5", "4.5"], "banana": ["10", "3.5"]}
    :return: None
    """
    # calculate the total price
    price = 0
    # arrange the order list
    order_list = []
    for item in item_dict:
        # arrange each item info to a small dict
        item_dict_new = {}
        price += int(item_dict[item][0]) * float(item_dict[item][1])
        item_dict_new["item"] = item
        item_dict_new["quantity"] = item_dict[item][0]
        item_dict_new["price"] = item_dict[item][1]
        # append the small dict to the order list
        order_list.append(item_dict_new)
    DATABASE.put("Invoices/"+userID, invoiceID,
                 {
                     "orders": order_list,
                     'total price': str(price),
                     'status': {
                         'issued': True,
                         'paid': False,
                         'delivered': False
                    }
                 })
# item_dict = {}
# print([request.args.get("quantity"), request.args.get("price")])
# item_dict[request.args.get("item")] = [request.args.get("quantity"),
#                                        request.args.get("price")]
create_invoice({"hi":["5","4.5"]}, "FEkg7hBAVxPgbwHHp2VmNwVCCwK2", "invoice2")

# customer_path = '/Truck Driver/' + "nSTFFgWdZvYpenarvvTmpXxJIYA3" + '/Assigned Invoices'
#
# listOfCustomerIDs = ""
# try:
#
#     inventorydb = DATABASE.get(customer_path, None)
#     for key in inventorydb:
#         listOfCustomerIDs += key + ":" + DATABASE.get(customer_path, key) + ","
#
#     print(listOfCustomerIDs[:-1])
# except:
#     print("nothing")
#
