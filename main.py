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
