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

def takePicture(confidence):
    '''
    Takes a picture, scans for license plates, and
    returns a tuple of (data, time taken), getting rid of all guesses below
    the confidence threshold given
    '''
    start = time.time()
    success, image = camera.read() #Take a screenshot
    if success:
        #cv2.imshow("Test", image)
        cv2.imwrite("runtime/test.jpg", image)
    else:
        print("Picture failed")
    data = cmdTest.scanPlate("runtime/test.jpg")
    timeTaken = time.time()-start
    print("Time Taken: " + str(timeTaken))

    #Remove low confidence guesses
    tempData = []
    for plate in data:
        tempPlate = []
        for guess in plate:
            if guess[1] >= confidence:
                tempPlate.append(guess)
        if(len(tempPlate) != 0):
            tempData.append(tempPlate)
    return (tempData, timeTaken)

#Print out average time it takes to take each picture
avgTime = 0
total = 0
count = 0
while True:
    data, timeTaken = takePicture(85)
    print(data)
    total += timeTaken
    count +=1
    avgTime = total/count
    print("Average time: " + str(avgTime))
