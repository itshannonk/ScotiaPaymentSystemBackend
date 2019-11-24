from flask import Request, Flask
import pyrebase

from model import DataRetrieval
app = Flask(__name__)


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
user = auth.sign_in_with_email_and_password("email@gmail.com", "password")
firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)
print(user["localId"])
try:
    if(firebase.get('/Business Owner', user["localId"]) != None):
        print("Business Owner")
except:
    pass
try:
    if(firebase.get('/CocaCola', user["localId"]) != None):
        print("CocaCola")
except:
    pass
try:
    if(firebase.get('/Truck Driver', user["localId"]) != None):
        print("Truck Driver")
except:
    print("")
