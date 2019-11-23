from firebase import firebase
firebase = firebase.FirebaseApplication("https://console.firebase.google.com/u/0/project/csc207-tli/database/csc207-tli/data/")
result = firebase.get("/CocaCola", "testing")
print(result)