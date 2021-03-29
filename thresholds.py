import cv2 as cv
import numpy as np


img = cv.imread('imgs/dan.jpg')
h, w = img.shape[:2]
img = cv.resize(img, (w//3, h//3))
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# simple threshold
threshold, thresh = cv.threshold(gray, 120, 250, cv.THRESH_BINARY)
# cv.imshow('simple threshold', thresh)
print(threshold)

# inverse simple threshold
ret, inverse_thresh = cv.threshold(gray, 120, 250, cv.THRESH_BINARY_INV)
# cv.imshow('inverse simple thresh', inverse_thresh)

cv.imshow('ret', np.hstack((gray, thresh, inverse_thresh)))

# adaptive threshold
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 1)
cv.imshow('adapted thresh', adapt_thresh)

cv.waitKey(0)