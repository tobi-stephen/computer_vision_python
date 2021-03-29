import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint a certain color
blank[200:300, 300:400] = 0, 0, 255
blank[0:100, 100:200] = 255, 0, 0
cv.imshow('colors', blank)

# 2. draw a rectangle
cv.rectangle(blank, (100,100), (250,250), (0,255, 0), thickness=cv.FILLED, lineType=cv.LINE_AA)
cv.imshow('rect', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 255, 0), thickness=cv.FILLED)
cv.imshow('circle', blank)

# 4. draw a line
cv.line(blank, (100,0), (300,300), (255,255, 255), thickness=4, lineType=cv.LINE_AA)
cv.imshow('line', blank)

# 5. draw a text
cv.putText(blank, 'BaBa Hello', (100,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100, 100, 100), 2, cv.LINE_AA, False)
cv.imshow('text', blank)

cv.arrowedLine(blank, (499,499), (0,0), (125,125,125), 4)
cv.imshow('arrowedLne', blank)
cv.waitKey(0)