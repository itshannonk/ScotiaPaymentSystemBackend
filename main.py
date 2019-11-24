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
from model import DataRetrieval

app = Flask(__name__)
@app.route('/login_page_get', methods=['GET'])
def login_page_get(request: Request):
    """HTTP Cloud Function.
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
    return True
    #firebase = pyrebase.initialize_app(config)

    #auth = firebase.auth()

    #try:
        #user = auth.sign_in_with_email_and_password(request.args["email"], request.args["password"])
        #return True
    #except:
        #return False

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


def get_user_by_id(request: Request):
    """ Retrieve a single user's information based on its unique id. """
    pass


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

app = Flask(__name__)
@app.route('/login_page_get', methods=['GET'])
def login_page_get(request: Request):
    """HTTP Cloud Function.
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
    from firebase import firebase
    user = auth.sign_in_with_email_and_password(request["email"], request["password"])
    firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)
    print(user["localId"])
    try:
        if (firebase.get('/Business Owner', user["localId"]) != None):
            return "Business Owner"
    except:
        pass
    try:
        if (firebase.get('/CocaCola', user["localId"]) != None):
            return "CocaCola"
    except:
        pass
    try:
        if (firebase.get('/Truck Driver', user["localId"]) != None):
            return "Truck Driver"
    except:
        return ""