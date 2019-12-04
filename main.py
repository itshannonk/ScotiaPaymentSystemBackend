"""
This module has been hosted using Google Cloud Platform. Every function has an
http endpoint that has been deployed with GCP.
"""
import pyrebase
from flask import Request, Flask
from model import FirebaseInvocations

app = Flask(__name__)


@app.route('/login_page_get', methods=['GET'])
def login_page_get(request: Request):
    """HTTP Cloud Function.
        This deals check the authentication of the user and also the retrieval of the userID
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
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
    user = auth.sign_in_with_email_and_password(request.args.get("email"),
                                                request.args.get("password"))
    # TODO: change the statement above to the commented one below:
    # user = FirebaseInvocations.get_current_user(request.args.get("email"), request.args.get("email"))
    try:
        if FirebaseInvocations.get_user_data('Business Owner', user["localId"]):
            return "Business Owner" + "," + user["localId"]
    except:
        pass
    try:
        if FirebaseInvocations.get_user_data('CocaCola', user["localId"]):
            return "CocaCola" + "," + user["localId"]
    except:
        pass
    try:
        if FirebaseInvocations.get_user_data('Truck Driver', user["localId"]):
            return "Truck Driver" + "," + user["localId"]
    except:
        return ","


@app.route('/get_customers', methods=['GET'])
def get_customers(request: Request):
    """ Return all the business owners' unique ids.

    :param request: flask.Request object.
    :return: Comma separated string of unique ids.
    """
    return FirebaseInvocations.get_customers()


@app.route('/get_assigned_invoices', methods=['GET'])
def get_assigned_invoices(request: Request):
    """ Return the invoices assigned to a given user.

    :param request: flask.Request object.
    :return: Comma separated string of invoice ids.
    """
    user_id = request.args.get("userID")
    return FirebaseInvocations.get_assigned_invoices(user_id)


@app.route('/create_user', methods=['PUT'])
def create_user(request: Request):
    """ Add a new user to the database.

    :param request: flask.Request object.
    :return: The new user's unique id.
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
    user = auth.create_user_with_email_and_password(request.args.get("email"),
                                                    request.args.get(
                                                        "password"))
    userID = user["localId"]
    FirebaseInvocations.create_user(request.args.get("address"),
                                    request.args.get("email"),
                                    request.args.get("name"),
                                    request.args.get("password"),
                                    request.args.get("role"), userID)
    return userID


@app.route('/get_display_name', methods=['GET'])
def get_display_name(request: Request):
    """ Return a given user's name.

    :param request: flask.Request object.
    :return: A string containing the user's name.
    """
    user_id = request.args.get("userID")
    return FirebaseInvocations.get_login_name(user_id)


@app.route('/get_list_of_invoice_ids', methods=['GET'])
def get_list_of_invoice_ids(request: Request):
    """ Return a list of a given user's assigned invoices.

    :param request: flask.Request object.
    :return: A string containing comma-separated invoice ids.
    """
    user_id = request.args['userID']
    return FirebaseInvocations.get_list_of_invoice_ids(user_id)


@app.route('/get_current_invoiceID', methods=['GET'])
def get_current_invoiceID(request: Request):
    """ Get the most recent invoice's id.

    :param request: flask.Request object.
    :return: A string containing an invoice's id.
    """
    return FirebaseInvocations.get_current_invoiceID()


@app.route('/get_list_of_invoice_ids', methods=['POST'])
def increment_current_invoiceID(request: Request):
    """ Increment the current invoice's id by 1.

    :param request: flask.Request object.
    :return: None.
    """
    return FirebaseInvocations.increment_current_invoiceID()


@app.route('/get_invoice_information', methods=['GET'])
def get_invoice_information(request: Request):
    """ Get information about a given invoice.

    :param request: flask.Request object.
    :return: A comma separated string containing the "delivered, issued, paid, price" information about an invoice.
    """
    user_id = request.args['userID']
    invoice_id = request.args['invoiceID']
    return FirebaseInvocations.get_invoice_information(user_id, invoice_id)


@app.route('/get_invoice_by_id', methods=['GET'])
def get_invoice_by_id(request: Request):
    """ Get an information about a given invoice.

    :param request: flask.Request object.
    :return: A json object containing an invoice's information.
    """
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    return FirebaseInvocations.get_invoice_json(user_id, invoice_id)


@app.route('/get_user_by_id', methods=['GET'])
def get_name(request: Request):
    """ Return a given user's data.

    :param request: flask.Request object.
    :return: A json object containing a user's data.
    """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


@app.route('/set_invoice_status', methods=['SET'])
def set_invoice_status(request: Request):
    """ Change a given invoice's status.

    :param request: flask.Request object.
    :return: A string containing the request's status.
    """
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    status_type = request.args['statustype']  # 'issued', 'paid', 'delivered'
    if request.args['newvalue'].lower() == 'true':
        new_value = True
    else:
        new_value = False
    if FirebaseInvocations.set_invoice_status(user_id, invoice_id, status_type,
                                              new_value):
        return 'The invoice was found in the database'
    return 'The invoice was not found in the database'


@app.route('/get_user_by_id', methods=['GET'])
def get_user_by_id(request: Request):
    """ Return a given user's data.

    :param request: flask.Request object.
    :return: A json object containing a user's data.
    """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


@app.route('/create_invoice', methods=['PUT'])
def create_invoice(request: Request):
    """ Creates an invoice using the given data (item, quantity, and price).

    :param request: flask.Request object.
    :return: None.
    """
    print("reached create invoice main")
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    item_dict = {request.args.get("item"): [request.args.get("quantity"),
                                            request.args.get("price")]}
    FirebaseInvocations.create_invoice(item_dict, user_id, invoice_id)
