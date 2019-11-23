import pyrebase
from getpass import getpass

firebaseConfig = {
    "apiKey": "AIzaSyCkjsbkDtmKUU_77XHDYfNnBZS1E3F82iw",
    "authDomain": "csc207-tli.firebaseapp.com",
    "databaseURL": "https://csc207-tli.firebaseio.com",
    "projectId": "csc207-tli",
    "storageBucket": "csc207-tli.appspot.com",
    "messagingSenderId": "707734809591",
    "appId": "1:707734809591:web:313eb97ac705e6ebb21cf2",
    "measurementId": "G-VQCPWR41LV"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Please Enter Your Email Address : ")
password = input("Please Enter Your Password :  ")

# create users
user = auth.create_user_with_email_and_password(email, password)
print("Success .... ")

login = auth.sign_in_with_email_and_password(email, password)

print("Success ... ")