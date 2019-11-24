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

