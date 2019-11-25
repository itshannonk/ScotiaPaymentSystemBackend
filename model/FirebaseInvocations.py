"""
This module will be used to make calls to the real-time database.
"""
from flask import Request, Flask
from firebase import firebase
import json
import pyrebase
# Initialize database
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)


def get_current_user(email: str, password: str):
    """ Get the current user's information for authentication purposes.
    """
    pass
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
        invoice_information += inventorydb.get(invoiceID, "delivered")
        invoice_information += inventorydb.get(invoiceID, "issued")
        invoice_information += inventorydb.get(invoiceID, "paid")
        invoice_information += inventorydb.get("total price", None)
        for key in inventorydb:
            invoice_information += str(key) + ','
        return invoice_information[:-1]
    except:
        return ""


def create_user(address: str, email: str, name: str, password: str, role: str, userID: str):
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


def set_invoice_status(user_id: str, invoice_id: str, status_type: str, new_value: bool):
    """ Change invoice_id's status based on status_type and new_value.

    :param user_id: Unique id of the user to whom the invoice belongs.
    :param invoice_id: Unique id of the invoice to be changed.
    :param status_type: The status that will be changed.
    :param new_value: The new status' value (either True or False).
    :return:
    """
    invoice_path = '/Invoices/' + user_id + '/' + invoice_id + '/status'
    # firebase.put('/Invoices/FEkg7hBAVxPgbwHHp2VmNwVCCwK2/invoice 1/status', 'issued', False)
    DATABASE.put(invoice_path, status_type, new_value)
