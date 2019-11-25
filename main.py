import pyrebase

# """
# from the website:
# your function's entrypoint must be defined in a Python source file
# at the root of your project named main.py
# """
# import requests
# import json
#
#
# def get_customer(request):
#     r = request.get("https://us-central1-csc207-tli.cloudfunctions.net/testing")
#     # a Python object (dict) is pretty much a JSON file:
#     x = {
#         "name": "John",
#         "age": 30,
#         "city": "New York"
#     }
#     #idk what it looks like yet but we have to convert it into JSON by
#     jsonStr = json.dumps(r.toDict())
#
#
#     # the result is a JSON string:
#     print(jsonStr)

# from firebase.firebase import FirebaseApplication, FirebaseAuthentication

# create user, get user, get invoice, pay invoice, confirm payment,

"""
from firebase import firebase
firebase = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")
data = {
    "Address": "Toronto",
    "Email": "testin@testing.com",
    "Invoices": "{\"id\":6,\"price\":0,\"status\":{\"delivered\":true,\"issued\":true,\"paid\":true}}",
    "Name": "Amy Testing",
    "Password": "password"
}

result = firebase.post("/Business Owner/", data)
print(result)
"""
"""
from the website:
your function's entrypoint must be defined in a Python source file
at the root of your project named main.py
"""
# import requests
from flask import Request, Flask
from model import DataRetrieval, FirebaseInvocations
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
        if (FirebaseInvocations.get_user_data('Business Owner', user["localId"]) != None):
            return "Business Owner"+","+user["localId"]
    except:
        pass
    try:
        if (FirebaseInvocations.get_user_data('CocaCola', user["localId"])  != None):
            return "CocaCola"+","+user["localId"]
    except:
        pass
    try:
        if (FirebaseInvocations.get_user_data('Truck Driver', user["localId"])  != None):
            return "Truck Driver"+","+user["localId"]
    except:
        return ","


@app.route('/create_user', methods=['PUT'])
def create_user(request: Request):

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
    auth.create_user_with_email_and_password(request.args.get("email"), request.args.get("password"))
    print(auth.create_user_with_email_and_password(request.args.get("email"), request.args.get("password")))
    userID = auth.getInstance().getCurrentUser().getUid()
    FirebaseInvocations.create_user(request.args.get("address"), request.args.get("email"), request.args.get("name"),
                                    request.args.get("password"), request.args.get("role"), userID)
    return

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


@app.route('/get_user_by_id', methods=['GET'])
def get_name(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


@app.route('/set_invoice_status', methods=['SET'])
def set_invoice_status(request: Request):
    """ Change an invoices status. """
    user_id = request.args['userid']
    invoice_id = request.args['invoiceid']
    status_type = request.args['statustype']
    new_value = bool(request.args['newvalue'])
    FirebaseInvocations.set_invoice_status(user_id, invoice_id, status_type,
                                           new_value)
    return 'New values was recorded'


@app.route('/shannons-testing-functionCOPY', methods=['GET'])
def hello_get(request: Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    result = DataRetrieval.get_pls_work()
    # return result
    return result
    # return info
    # return 'return from hello_get function in main.py ' + request.url


@app.route('/get_user_by_id', methods=['GET'])
def get_user_by_id(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    user_type = request.args['usertype']
    user_id = request.args['userid']
    return FirebaseInvocations.get_user_data(user_type, user_id)


# TRYING TO RUN A LOCAL SERVER USING FLASK
@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/testing')
def local_testing(request: Request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    result = DataRetrieval.get_pls_work()
    return result


# def get_customer(request):
#     r = request.get("https://us-central1-csc207-tli.cloudfunctions.net/testing")

