import cv2 as cv
import numpy as np

img = cv.imread('imgs/lenna.png')
# img = cv.resize(img, (320,400))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 3)
print(len(faces))

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

cv.imshow('img', img)

cv.waitKey(0)