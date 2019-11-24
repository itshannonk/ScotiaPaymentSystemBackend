"""
This module will be used to make calls to the real-time database.
"""
from firebase import firebase
# Initialize database
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


def get_user_data(user_type: str, user_id: str):
    """ Get a user's data base on user_type and user_id.

    :param user_type: BusinessOwner, CocaCola, Driver
    :param user_id: User's unique id in the database
    :return: a json object containing the user's information
    """
    return DATABASE.get('/' + user_type, user_id)
