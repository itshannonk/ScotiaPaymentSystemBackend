from flask import Request, Flask
from firebase import firebase
DATABASE = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/',
                                        None)
userDATA = DATABASE.get('/Business Owner', "3T8yP4J8IaaLKV0cueQjsSK07aX2")
userDATA.get("Name", None)
