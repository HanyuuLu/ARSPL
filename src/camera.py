import cv2.cv2 as cv2
import lpr
import time
cap = cv2.VideoCapture(1)
image = cv2.imread('demo.jpg')
while True:
    ret, frame = cap.read()
    cv2.imshow('capture', frame)
    res = lpr.recognition(frame)
    print(res, end='\r')
    if (cv2.waitKey(1) & 0xff) == ord('s'):
        break
