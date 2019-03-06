import cmdTest
import cv2
import os

try:
    os.mkdir("runtime")
except:
    print("Failed to create runtime directory")

camera = cv2.VideoCapture(0)
success, image = camera.read()
if success:
    cv2.imshow("Test", image)
    cv2.imwrite("runtime/test.jpg", image)
