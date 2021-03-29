import cv2 as cv
import numpy as np

img_orig = cv.imread('imgs/pre_tope.jpg')
img = cv.resize(img_orig, (500, 500))
cv.imshow('img', img)

# convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(blur, 100, 100)
cv.imshow('canny edge', canny)

# dilate image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilated)

kernel = np.ones((7,7), dtype='uint8')
dilatedNP = cv.dilate(canny, kernel, iterations=3)
cv.imshow('dilatedNP', dilatedNP)

# erode image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('eroded', eroded)

# resize image
resized = cv.resize(img_orig, (400, 400), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# crop image using array slicing
cropped = img[50:200, 100:250]
cv.imshow('cropped', cropped)

cv.waitKey(0)