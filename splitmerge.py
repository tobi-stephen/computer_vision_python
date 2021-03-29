import cv2 as cv
import numpy as np


img = cv.imread('imgs/pre_tope.jpg')
w, h = img.shape[1], img.shape[0]

img = cv.resize(img, (int(w*0.5), int(w*0.5)))
cv.imshow('img', img)

blank = np.zeros((int(w*0.5), int(w*0.5)), dtype='uint8')

b, g, r = cv.split(img)

# displays each channel in grayscale
cv.imshow('blue', b)
cv.imshow('red', r)
cv.imshow('green', g)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge color channels
merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# displays the actual colors of each channels
cv.imshow('bluec', cv.merge([b, blank, blank]))
cv.imshow('redc', cv.merge([blank, blank, r]))
cv.imshow('greenc', cv.merge([blank, g, blank]))

cv.waitKey(0)