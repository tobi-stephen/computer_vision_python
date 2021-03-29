import cv2 as cv
import numpy as np


img = cv.imread('imgs/pre_tope.jpg')
h, w = img.shape[:2]
img = cv.resize(img, (w//3, h//3))
cv.imshow('img', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# laplacian operator
laplace_image = cv.Laplacian(gray, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(laplace_image))

# sobel operators
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)
sobx = np.uint8(np.absolute(sobelx))

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)
soby = np.uint8(np.absolute(sobelx))
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('ret image', np.hstack((gray, lap)))
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined sobel', combined_sobel)

# edge detect
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)