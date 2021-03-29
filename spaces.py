import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('imgs/dan.jpg')
img = cv.resize(img, (250,250))
# cv.imshow('img', img)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# BGR ro L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

ret = np.hstack((img, hsv, lab, rgb))
cv.imshow('out', ret)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('lab to BGR', lab_bgr)

# gray to BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray to BGR', gray_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)