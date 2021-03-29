import cv2 as cv
import numpy as np

img = cv.imread('imgs/pre_tope.jpg')
w, h = int(img.shape[1] * 0.5), int(img.shape[0]*0.5)
img = cv.resize(img, (w, h))
cv.imshow('img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

mask = cv.circle(blank.copy(), (w//3, h//3), 50, 255, -1)
cv.imshow('Mask', mask)

rect = cv.rectangle(blank.copy(), (w//3 - 40, h//3 -40), (w//3 +40, h//3+40), 255, -1)

sh = cv.bitwise_and(mask, rect)
cv.imshow('mask_and', sh)

masked = cv.bitwise_and(img, img, mask=sh)
cv.imshow('masked', masked)

cv.waitKey(0)