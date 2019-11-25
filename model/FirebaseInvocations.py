"""
This module will be used to make calls to the real-time database.
"""
from flask import Request, Flask
from firebase import firebase
import json
# Initialize database
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


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
    userDATA = DATABASE.get('/Business Owner', userID)
    inventorydb = userDATA.get("Invoices")
    for key in inventorydb:
        # try and except block testing if there are multiple invoices
        try:
            int(key)
        except:
            # testing if there is only one invoice
            try:
                return json.loads(inventorydb).get("id")
            except:
                pass
        listOfInvoiceIDs += str(key) + ','
    return listOfInvoiceIDs[:-2]
