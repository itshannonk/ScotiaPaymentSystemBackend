"""
This module will be used to make calls to the real-time database.
"""
from flask import Request, Flask
from firebase import firebase
import json
import pyrebase
# Initialize database
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


def get_current_user(email: str, password: str):
    """ Get the current user's information for authentication purposes.
    """
    config = {
        "apiKey": "AIzaSyCkjsbkDtmKUU_77XHDYfNnBZS1E3F82iw",
        "authDomain": "csc207-tli.firebaseapp.com",
        "databaseURL": "https://csc207-tli.firebaseio.com",
        "projectId": "csc207-tli",
        "storageBucket": "csc207-tli.appspot.com",
        "messagingSenderId": "707734809591",
        "appId": "1:707734809591:web:313eb97ac705e6ebb21cf2",
        "measurementId": "G-VQCPWR41LV"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    return auth.sign_in_with_email_and_password(email, password)


def get_user_data(user_type: str, user_id: str):
    """ Get a user's data base on user_type and user_id.

    :param user_type: Business Owner, CocaCola, Truck Driver
    :param user_id: User's unique id in the database
    :return: a json object containing the user's information
    """
    return DATABASE.get('/' + user_type, user_id)


def get_login_name(userID):
    """ Get a user's data base on user_type and user_id.

    :param user_type: Business Owner, CocaCola, Truck Driver
    :param user_id: User's unique id in the database
    :return: a json object containing the user's information
    """
    try:
        if (DATABASE.get('/Business Owner', userID) != None):
            userDATA = DATABASE.get('/Business Owner', userID)
            return userDATA.get("Name", None)
    except:
        pass
    try:
        if (DATABASE.get('/CocaCola', userID) != None):
            userDATA = DATABASE.get('/CocaCola', userID)
            return userDATA.get("Name", None)
    except:
        pass
    try:
        if (DATABASE.get('/Truck Driver', userID) != None):
            userDATA = DATABASE.get('/Truck Driver', userID)
            return userDATA.get("Name", None)
    except:
        return ""


def get_list_of_invoice_ids(userID):
    """
    :param userID: the userId
    :return: a string of invoiceIDs under the userID, where it is separated by commas
    """
    listOfInvoiceIDs = ""
    try:
        inventorydb = DATABASE.get('Invoices', userID)
        for key in inventorydb:
            listOfInvoiceIDs += str(key) + ','
        return listOfInvoiceIDs[:-1]
    except:
        return ""

def get_invoice_information(userID, invoiceID):
    """
    :param userID: the userId
    :return: "delivered, issued, paid, price"
    """
    invoice_information = ""
    try:
        inventorydb = DATABASE.get('Invoices', userID)
        inventorydb = inventorydb.get(invoiceID, None)
        statusdb = inventorydb.get("status", None)
        invoice_information += str(statusdb.get("delivered")) +","
        invoice_information += str(statusdb.get("issued"))+","
        invoice_information += str(statusdb.get("paid"))+","
        invoice_information += str(inventorydb.get("total price", None))
        return invoice_information
    except:
        return ""


def get_invoice_json(user_id: str, invoice_id: str):
    """ Return the invoice with id invoice_id as a json object.

    :param user_id: User's unique id.
    :param invoice_id: The invoice's unique id.
    :return: A json object containing the invoice.
    """
    invoice_path = '/Invoices/' + user_id
    return DATABASE.get(invoice_path, invoice_id)


def create_user(address: str, email: str, name: str, password: str, role: str, userID: str):
    "reached create user firebase"
    if role == "a Business Owner":
        DATABASE.put("Business Owner", userID,
                     {
                         "Address": address,
                         "Email": email,
                         "Name": name,
                         "Password": password
                     })
    elif role == "a Truck Driver":
        DATABASE.put("Truck Driver", userID,
                     {
                         "Email": email,
                         "Name": name,
                         "Password": password
                     })
    else:
        DATABASE.put(role, userID,
                     {
                         "Email": email,
                         "Name": name,
                         "Password": password
                     })


def set_invoice_status(user_id: str, invoice_id: str, status_type: str,
                       new_value: bool) -> bool:
    """ Change invoice_id's status based on status_type and new_value.

    :param user_id: Unique id of the user to whom the invoice belongs.
    :param invoice_id: Unique id of the invoice to be changed.
    :param status_type: The status that will be changed.
    :param new_value: The new status' value (either True or False).
    :return: Return True iff the invoice path is in the database.
    """
    invoice_path = '/Invoices/' + user_id + '/' + invoice_id
    if DATABASE.get(invoice_path, '/status'):
        DATABASE.put(invoice_path + '/status', status_type, new_value)
        return True
    return False


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
    DATABASE.put("Invoices/" + userID, invoiceID,
                 {
                     "orders": order_list,
                     'total price': str(price),
                     'status': {
                         'issued': True,
                         'paid': False,
                         'delivered': False
                     }
                 })
def get_customers():
    """ Change invoice_id's status based on status_type and new_value.

    :param user_id: Unique id of the user to whom the invoice belongs.
    :param invoice_id: Unique id of the invoice to be changed.
    :param status_type: The status that will be changed.
    :param new_value: The new status' value (either True or False).
    :return: Return True iff the invoice path is in the database.
    """
    listOfCustomerIDs = ""
    try:
        inventorydb = DATABASE.get('Business Owner', None)
        for key in inventorydb:
            listOfCustomerIDs += str(key) + ','
        return listOfCustomerIDs[:-1]
    except:
        return ""

