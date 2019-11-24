def get_pls_work():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://csc207-tli.firebaseio.com/', None)
    result = firebase.get('/CocaCola', 'hcO40l8tnZVXkUVVYPq5QQJBoM92')
    return result
    print(result)
