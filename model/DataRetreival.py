from firebase import firebase
firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)
result = firebase.get('/CocaCola', 'testing')
print(result)