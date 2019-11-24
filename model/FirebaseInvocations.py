"""
This module will be used to make calls to the real-time database.
"""
from flask import Request, Flask
from firebase import firebase
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

app = Flask(__name__)
@app.route('/get_name', methods=['GET'])
def get_name(request: Request):
    """ Get a user's data base on user_type and user_id.

    :param user_type: Business Owner, CocaCola, Truck Driver
    :param user_id: User's unique id in the database
    :return: a json object containing the user's information
    """
    try:
        if (DATABASE.get('/Business Owner', request.args.get("userID")) != None):
            userDATA = DATABASE.get('/Business Owner', request.args.get("userID"))
            return userDATA.get("Name", None)
    except:
        pass
    try:
        if (DATABASE.get('/CocaCola', request.args.get("userID")) != None):
            userDATA = DATABASE.get('/CocaCola', request.args.get("userID"))
            return userDATA.get("Name", None)
    except:
        pass
    try:
        if (DATABASE.get('/Truck Driver', request.args.get("userID")) != None):
            userDATA = DATABASE.get('/Truck Driver', request.args.get("userID"))
            return userDATA.get("Name", None)
    except:
        return ""
