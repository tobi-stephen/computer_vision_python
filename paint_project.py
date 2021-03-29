import cv2 as cv
import numpy as np


# myColors = [[5,107,0,19,255,255],[0, 94,0,179,255, 43], [133,56,0,159,156,255], [57,76,0,100,255,255]]
myColors = [[0, 0,255,0,255, 255]]
myPoints = []

def findColor(img, myColor):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    for i,color in enumerate(myColor):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(hsv, lower, upper)
        x,y = getContours(mask)
        if x == 0 and y == 0:
            continue
        myPoints.append((x,y))
        cv.circle(imgContour, (x,y), 10, (0,0,255), thickness=cv.FILLED)

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    # print("no of contours: {}".format(len(contours)))
    x,y,w,h = 0,0,0,0
    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        if area < 2000:
            continue

        # cv.drawContours(imgContour, cnt, -1, (255,0,0), thickness=3)
        perimeter = cv.arcLength(cnt, True)
        approxCurve = cv.approxPolyDP(cnt, 0.02*perimeter, True)
        x, y, w, h = cv.boundingRect(approxCurve)
        cv.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 3)

    return x+w//2, y+h//2

def clear(_, __):
    global myPoints
    myPoints = []

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 480)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 320)
capture.set(cv.CAP_PROP_BRIGHTNESS, 1000)

cv.namedWindow('contours')
cv.createButton('clear', clear, myPoints, cv.QT_NEW_BUTTONBAR)

while True:
    ret, frame = capture.read()
    img = cv.resize(cv.flip(frame, 1), (400, 320))
    imgContour = img.copy()
    findColor(img, myColors)

    if len(myPoints) != 0:
        for point in myPoints:
            cv.circle(imgContour, point, 10, (0, 0, 255), thickness=cv.FILLED)

    # cv.imshow('Video', img)
    cv.imshow('contours', imgContour)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()