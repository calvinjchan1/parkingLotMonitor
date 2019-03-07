import pyrebase

#https://github.com/thisbejim/Pyrebase for documentaion on pyrebase

#Get login info
email = input("Enter your email address: ")
password = input("Enter your password: ")
APIKey = input("Enter the API Key: ")

#Setup pyrebase
config = {
  "apiKey": APIKey,
  "authDomain": "parkinglotmonitor.firebaseapp.com",
  "databaseURL": "https://parkinglotmonitor.firebaseio.com",
  "storageBucket": "parkinglotmonitor.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
print(user)
