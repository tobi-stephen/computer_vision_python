import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('imgs/babe.jpg')
h, w = img.shape[:2]
img = cv.resize(img, (w//2, h//2))
cv.imshow('img', img)
# print(img.dtype)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype=img.dtype)
circle = cv.circle(blank.copy(), (w//4, h//6), 100, 255, -1)
cv.imshow('circle', circle)

mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('mask', mask)

# histogram ==> intensity distribution of an image
# grayscale histogram
gray_hit = cv.calcHist([gray], [0], None, [256], [0, 256])
#
#
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.hist(gray.ravel(), 256, [0,256])
# plt.plot(gray_hit)
# plt.xlim([0,256])
# plt.show()

# color histogram

b, g, r = cv.split(img)

# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
#
# plt.hist(b.ravel(), 256, [0,256])
# plt.hist(g.ravel(), 256, [0,256])
# plt.hist(r.ravel(), 256, [0,256])
# plt.show()


# plt.figure()
# plt.title('color histogram')
# plt.ylabel('# of pixels')
# plt.xlabel('bins')
# colors = ('b', 'g', 'r')
#
# for i, col in enumerate(colors):
#     hist = cv.calcHist([img], [i], circle, [256], [0,256])
#     plt.plot(hist, color=col)
#     plt.xlim([0,256])
#     # plt.show()
#
# plt.show()
#
# cv.waitKey(0)