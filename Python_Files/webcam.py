import cmdTest
import cv2
import os
import time

#Make a runtime directory if there isn't one
try:
    os.mkdir("runtime")
    print("Created runtime directory")
except:
    print("Failed to create runtime directory")

#Take a picture and save it to the runtime directoy
camera = cv2.VideoCapture(0)
time.sleep(1); #Let windows get camera ready

def takePicture():
    '''
    Takes a picture, scans for license plates, and
    returns how long it took to do sos
    '''
    start = time.time()
    success, image = camera.read() #Take a screenshot
    if success:
        #cv2.imshow("Test", image)
        cv2.imwrite("runtime/test.jpg", image)
    else:
        print("Picture failed")
    print(cmdTest.scanPlate("runtime/test.jpg"))
    timeTaken = time.time()-start
    print("Time Taken: " + str(timeTaken))
    return timeTaken

#Print out average time it takes to take each picture
avgTime = 0
total = 0
count = 0
while True:
    total += takePicture()
    count +=1
    avgTime = total/count
    print("Average time: " + str(avgTime))
