def get_pls_work():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)
    result = firebase.get('/CocaCola', 'testing')
    return result
    print(result)
