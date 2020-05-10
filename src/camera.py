import cv2.cv2 as cv2
import lpr
import time
timeStamp = time.time()
cap = cv2.VideoCapture(1)
image = cv2.imread('demo.jpg')
while True:
    ret, frame = cap.read()
    cv2.imshow('capture', frame)
    res = lpr.recognition(frame)
    print("\r%s %f ms             " %
          (res, (time.time() - timeStamp)*1000), end='')
    timeStamp = time.time()
    if (cv2.waitKey(1) & 0xff) == ord('s'):
        break
