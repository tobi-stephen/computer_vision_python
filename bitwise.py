import cv2 as cv
import numpy as np


blank = np.zeros((400, 400), dtype='uint8')

rect = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, thickness=cv.FILLED, lineType=cv.LINE_AA)

cv.imshow('ret', np.hstack((rect, circle)))

# bitwise AND ==> intersecting regions
bitwise_and = cv.bitwise_and(rect, circle)

# bitwise OR ==> intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rect, circle)

# bitwise NOT ==> inverts pixels
bitwise_not = cv.bitwise_not(rect)

# bitwise XOR ==> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rect, circle)

cv.imshow('bitwise', np.hstack((bitwise_and, bitwise_or, bitwise_xor)))

bitwise_not_circle = cv.bitwise_not(circle)
cv.imshow('bitwise not', np.hstack((bitwise_not, bitwise_not_circle)))

cv.waitKey(0)