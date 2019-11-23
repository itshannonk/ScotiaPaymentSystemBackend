from firebase import firebase
import json
firebase = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")
resultPut = firebase.put('Business Owner','this is where the authID goes', {'Name':'Grace', 'help':'me'})
print(resultPut)