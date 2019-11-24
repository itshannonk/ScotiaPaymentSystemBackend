from flask import Request, Flask
import pyrebase
from model import DataRetrieval
app = Flask(__name__)


@app.route('/shannons-testing-functionCOPY', methods=['GET'])
def loginPage(request: Request):
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

    try:
        user = auth.sign_in_with_email_and_password(request.args["email"], request.args["password"])
        token = user['idToken']
        return token.uID
    except:
        return False

#import pyrebase

#app = Flask(__name__)
#email = input("enter email ")
#password = input("enter password ")
#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
#try:
    #user = auth.sign_in_with_email_and_password(email, password)
    #authentication = firebase.Authentication('WhuM19qMjd7nY89xzzFhrkxCCIWEBGL2khm2y2UC', 'abc@gmail.com')
    #firebase.authentication = authentication
    #print(authentication.extra)
#except:
    #print("")
    #7iQ8fEpGvsSEQXXfOl3AJB5hFfu2