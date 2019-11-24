"""
This module will be used to make calls to the real-time database.
"""
from firebase import firebase
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)


# firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
#                                         None)
# result = firebase.get('/CocaCola', 'hcO40l8tnZVXkUVVYPq5QQJBoM92')
def get_user_data(user_type: str, user_id: str):
    return DATABASE.get('/' + user_type, user_id)
