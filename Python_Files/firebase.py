import pyrebase

#https://github.com/thisbejim/Pyrebase for documentaion on pyrebase

#Get login info
email = input("Enter your email address: ")
password = input("Enter your password: ")

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

#Send Data
db.child("parents").update({"test":True},user['idToken'])

#Get data
parents = db.child("parents").get(user['idToken'])
print(parents.val())
