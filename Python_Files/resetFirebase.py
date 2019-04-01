import firebase, listReader

'''
Clears all names in firebase and
resets it the data to what is in
the secret file
'''

firebase.deleteAll()

for parent in listReader.getParentList():
    firebase.createParent(parent)
