from firebase import firebase
import json
from model.Invoice import Invoice
import random

invoiceObject = Invoice()
resultPut = firebase.put('Business Owner','this is where the authID goes', {'Name':'Grace', 'help':'me'})



def createuser(request):
    fireb = firebase.FirebaseApplication("https://csc207-tli.firebaseio.com/")
    if ('id' in request.args) and ('name' in request.args) and ('address' in request.args) \
            and ('email' in request.args) and ('password' in request.args) and (request.args.get('type') == 'Customer'):
        fireb.put('Business Owner', request.args.get('id'), {'Address': request.args.get('address'), 'Email': request.args.get('email'),
                                                             'Name': request.args.get('name'), 'Password': request.args.get('password')})
        listofinvoices = []
        for i in range(0, 4):
            invoiceObject = Invoice(random.randint(0, 5), random.randint(0, 50), Status(), [Item(), Item(), Item()]).getinvoice()
            jsonObject = json.loads(invoiceObject)
            listofinvoices.append(jsonObject)



    elif ('id' in request.args) and ('name' in request.args) and ('address' in request.args) \
            and ('email' in request.args) and ('password' in request.args) and ((request.args.get('type') == 'Truck Driver') | (request.args.get('type') == 'CocaCola')):
        fireb.put(request.args.get('type'), request.args.get('id'),
                  { 'Email': request.args.get('email'),'Name': request.args.get('name'), 'Password': request.args.get('password')})
    else:
         print("Error, fields are not filled out!")
