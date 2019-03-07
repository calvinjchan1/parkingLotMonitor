import pyrebase, getpass

#https://github.com/thisbejim/Pyrebase for documentaion on pyrebase

#Get login info
email = input("Enter your email address: ")
password = getpass.getpass("Enter your password: ")

#Setup pyrebase
config = {
  "apiKey": "AIzaSyBzraFT2d7I2XAfkpinjeAb-BOZB-kHetY",
  "authDomain": "parkinglotmonitor.firebaseapp.com",
  "databaseURL": "https://parkinglotmonitor.firebaseio.com",
  "storageBucket": "parkinglotmonitor.appspot.com"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
print(user)
db = firebase.database()

#Example Code
'''
#Send Data
db.child("parents").update({"test":True},user['idToken'])

#Get data
parents = db.child("parents").get(user['idToken'])
print(parents.val())
'''

def getParent(parent):
    '''
    Returns a bool of whether the given parent is in the parking lot,
    None if the parent doesn't exist
    '''
    data = db.child("parents").child(parent).get(user['idToken'])
    inParkingLot = data.val()
    if inParkingLot != None: #Make sure the parent is someone who exists
        return inParkingLot
    else:
        return None

def setParent(parent, value):
    '''
    Sets the given parent to the given value. Returns true if successful,
    false if the parent doesn't exist
    '''
    if getParent(parent) != None: #Make sure parent exists
        db.child("parents").update({parent: value}, user['idToken'])
        return True
    else:
        return False

def createParent(parent, value=False):
    '''
    Creates the given parent with given value. Returns true if successful,
    false if the parent already exists
    '''
    if getParent(parent) == None: #Make sure parent doesn't exist
        db.child("parents").update({parent: value}, user['idToken'])
        return True
    else:
        return False

