import pyrebase
# import requests
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
    user = auth.sign_in_with_email_and_password(request.args.get("email"), request.args.get("password"))
    # TODO: change the statement above to the commented one below:
    # user = FirebaseInvocations.get_current_user(request.args.get("email"), request.args.get("email"))
    try:
        if FirebaseInvocations.get_user_data('Business Owner', user["localId"]):
            return "Business Owner"+","+user["localId"]
    except:
        pass
    try:
        if FirebaseInvocations.get_user_data('CocaCola', user["localId"]):
            return "CocaCola"+","+user["localId"]
    except:
        pass
    try:
        if FirebaseInvocations.get_user_data('Truck Driver', user["localId"]):
            return "Truck Driver"+","+user["localId"]
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
    user = auth.create_user_with_email_and_password(request.args.get("email"), request.args.get("password"))
    userID = user["localId"]
    FirebaseInvocations.create_user(request.args.get("address"), request.args.get("email"), request.args.get("name"),
                                    request.args.get("password"), request.args.get("role"), userID)
    return userID

@app.route('/get_display_name', methods=['GET'])
def get_display_name(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    userID = request.args.get("userID")
    return FirebaseInvocations.get_login_name(userID)


@app.route('/get_list_of_invoice_ids', methods=['GET'])
def get_list_of_invoice_ids(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    userID = request.args['userID']
    return FirebaseInvocations.get_list_of_invoice_ids(userID)

@app.route('/get_current_invoiceID', methods=['GET'])
def get_current_invoiceID(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    return FirebaseInvocations.get_current_invoiceID()

@app.route('/get_list_of_invoice_ids', methods=['POST'])
def set_current_invoiceID(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    return FirebaseInvocations.set_current_invoiceID()

@app.route('/get_invoice_information', methods=['GET'])
def get_invoice_information(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    userID = request.args['userID']
    invoiceID = request.args['invoiceID']
    return FirebaseInvocations.get_invoice_information(userID, invoiceID)


def get_invoice_by_id(request: Request):
    """ Retrieve an invoice given the user's id and the invoice id. """
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    return FirebaseInvocations.get_invoice_json(user_id, invoice_id)


@app.route('/get_user_by_id', methods=['GET'])
def get_name(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


@app.route('/set_invoice_status', methods=['SET'])
def set_invoice_status(request: Request):
    """ Change an invoice's status. """
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    status_type = request.args['statustype']
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
    """ Retrieve a single user's information based on its unique id. """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


@app.route('/create_invoice', methods=['PUT'])
def create_invoice(request: Request):
    print("reached create invoice main")
    userID = request.args['userid']
    invoiceID = request.args['invoiceid']
    item_dict = {}
    item_dict[request.args.get("item")] = [request.args.get("quantity"), request.args.get("price")]
    FirebaseInvocations.create_invoice( item_dict, userID, invoiceID)

    return "returned!"
