import cv2 as cv
import numpy as np

def empty(_):
    pass
    # print(_)

def emptya():
    print('press press')

# cv.namedWindow('TrackBars')
cv.namedWindow('ret')
cv.resizeWindow('ret', 640, 240)
cv.createTrackbar('Hue Min', 'ret', 0, 179, empty)
cv.createTrackbar('Hue Max', 'ret', 179, 179, empty)
cv.createTrackbar('Sat Min', 'ret', 0, 255, empty)
cv.createTrackbar('Sat Max', 'ret', 255, 255, empty)
cv.createTrackbar('Val Min', 'ret', 0, 255, empty)
cv.createTrackbar('Val Max', 'ret', 255, 255, empty)

# img = cv.imread('imgs/babe.jpg')
# h, w = img.shape[:2]
# img = cv.resize(img, (w//2, h//2))
# cv.imshow('img', img)

# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cap = cv.VideoCapture('vids/her.mp4')
# cap = cv.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
cap.set(cv.CAP_PROP_BRIGHTNESS, 1000)

while 1:
    ret, img = cap.read()
    img = cv.flip(cv.resize(img, (320,320)), 1)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos('Hue Min', 'ret')
    h_max = cv.getTrackbarPos('Hue Max', 'ret')
    s_min = cv.getTrackbarPos('Sat Min', 'ret')
    s_max = cv.getTrackbarPos('Sat Max', 'ret')
    v_min = cv.getTrackbarPos('Val Min', 'ret')
    v_max = cv.getTrackbarPos('Val Max', 'ret')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv.inRange(hsv, lower, upper)

    color_mask = cv.bitwise_and(img, img, mask=mask)


    cv.imshow('ret2', np.hstack((img, hsv, color_mask)))
    cv.imshow('mask', mask)


    if cv.waitKey(33) & 0xFF == ord('d'):
        print(lower)
        print(upper)
        break