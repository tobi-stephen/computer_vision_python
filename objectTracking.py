import cv2 as cv
import numpy as np

# TODO: install opencv_contrib for Tracker modules

cap = cv.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 720)

while True:
    timer = cv.getTickCount()
    ret, img = cap.read()

    fps = cv.getTickFrequency()/(cv.getTickCount() -timer)
    cv.putText(img, 'FPS: ' + str(int(fps)), (75,50), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2)
    cv.imshow('img', img)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break