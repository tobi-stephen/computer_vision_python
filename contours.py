import cv2 as cv
import numpy as np


img = cv.imread('imgs/pre_tope.jpg')
w = img.shape[1]
h = img.shape[0]
img = cv.resize(img, (int(w*0.3), int(h*0.3)), interpolation=cv.INTER_CUBIC)
cv.imshow('img', img)

img_copy = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

blur = cv.blur(gray, (5,5))
# cv.imshow('blur', blur)

canny = cv.Canny(blur, 125, 125)
# cv.imshow('canny', canny)



ret, thresh = cv.threshold(blur, 100, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

contours, hierachies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("no of contours: {}".format(len(contours)))

blank = np.zeros(gray.shape, dtype='uint8')

# for cnt in contours:
#     area = cv.contourArea(cnt)
    # print(area)
    # if area > 10:
cv.drawContours(blank, contours, -1, (255,255,255), 1)
cv.drawContours(img_copy, contours, -1, (0,255,0), 3)

cv.imshow('blank', blank)
cv.imshow('img_copy', img_copy)
# tot = np.hstack((img, img_copy))
# tot_g = np.vstack((np.hstack((gray, blur, thresh)), np.hstack((canny, blank, blank))))
# cv.imshow('tot', tot)
# cv.imshow('tot_g', tot_g)

cv.waitKey(0)