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
success, image = camera.read() #Take a screenshot
if success:
    cv2.imshow("Test", image)
    cv2.imwrite("runtime/test.jpg", image)
else:
    print("Picture failed")

time.sleep(1);
print(cmdTest.scanPlate("runtime/test.jpg"))
