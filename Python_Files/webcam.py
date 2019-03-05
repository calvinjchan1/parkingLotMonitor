import cmdTest
import cv2

camera = cv2.VideoCapture(0)
success, image = camera.read()
if success:
    cv2.imshow("Test", image)
    cv2.imwrite("test.jpg", image)
