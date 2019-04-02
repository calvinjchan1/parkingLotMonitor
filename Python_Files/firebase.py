import pyrebase, getpass, listReader
import pprint

#https://github.com/thisbejim/Pyrebase for documentaion on pyrebase

#Get login info
email = listReader.email #input("Enter your email address: ")
password = listReader.password#getpass.getpass("Enter your password: ")

plateDict = {}

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

def deleteAll():
    '''
    Deletes all parents
    '''
    data = db.child("parents").get(user['idToken'])
    if not (data.val() == None):
        for child in data.val():
            db.child("parents").child(child).remove(user['idToken'])

def refreshPlateDict():
    global plateDict
    data = db.child("users").get(user['idToken']) #Ordered Dict
    data = data.val()
    plateDict = {}
    for key in data:
        thisUser = data[key]
        #Covert plate data into usable array
        plates = "".join(thisUser['plates'].split())#Remove all whitespace
        plates = plates.replace("-", "")#Remove dashes
        plates = plates.upper()#Make sure we are in uppercase
        plates = plates.split(',')#Seperate by comma
        for plate in plates:
            if plate in plateDict:
                plateDict[plate].append(key)
            else:
                plateDict[plate] = [key]

def setLot(plate, mode):
    '''
    Try to update the firebase via the given plate
    plate is the license plate as a string to try and match
    mode is a boolean of the mode the program is being run in
        True is entrance mode
        False is exit mode
    Returns true if it was able to update with the given plate,
    false otherwise
    '''
    if plate in plateDict:
        for person in plateDict[plate]:
            db.child("users").child(person).update({"inParkingLot":mode}, user['idToken'])
        return True
    else:
        return False

refreshPlateDict()

