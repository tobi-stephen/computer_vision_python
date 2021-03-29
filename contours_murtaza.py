import cv2 as cv
import numpy as np
import pprint


def get_contours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print("no of contours: {}".format(len(contours)))
    for i, cnt in enumerate(contours):
        area = cv.contourArea(cnt)
        # pprint.pprint(cnt)
        if area < 2000: continue
        # print(area)
        # cv.drawContours(imgContour, cnt, -1, (255,0,0), thickness=cv.FILLED)

        perimeter = cv.arcLength(cnt, True)
        # print(perimeter)
        approxCurve = cv.approxPolyDP(cnt, 0.02*perimeter, True) #this is done for estimating the type of shape
        # print(len(approxCurve))
        cv.drawContours(hello, [approxCurve], 0, (0,0,0), 5)
        noOfObjectCorners = len(approxCurve)
        x, y, w, h = cv.boundingRect(cnt)
        # print(x, y, w, h)

        cv.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)

        if noOfObjectCorners == 3:
            objectType = 'triangle'
        elif noOfObjectCorners == 4:
            aspectRatio = h/float(w)
            # print(aspectRatio)
            if aspectRatio > 0.91 and aspectRatio < 1.09:
                objectType = 'square'
            else:
                objectType = 'rectangle'
        else:
            objectType = 'other'

        print('Area: {}, perimeter: {}, objectCorners: {}, object type: {}'.format(area, perimeter, noOfObjectCorners, objectType))

        cv.putText(imgContour, objectType, (x+(w//2)-30, y+(h//2)-30), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,0, 0), 3)
        cv.waitKey(0)



img = cv.resize(cv.imread('imgs/shape.jpeg'), (480,480))
# cv.imshow('img', img)
hello = img.copy()

imgContour = img.copy()

# gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# gaussian blur
blur = cv.GaussianBlur(gray, (7,7), 1)
# cv.imshow('blur', blur)

# canny
canny = cv.Canny(gray, 50, 50)
# cv.imshow('canny', canny)

# contours
get_contours(canny)


cv.imshow('ret', np.hstack((hello, img, imgContour)))
# cv.imshow('ret1', np.hstack((gray, blur, canny)))


cv.waitKey(0)