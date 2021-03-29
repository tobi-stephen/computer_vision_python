import cv2 as cv
import sys
import math

point_list = list()

def clickEvent(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        size = len(point_list)
        print (size)
        if size != 0 and size % 3 != 0:
            cv.line(img, tuple(point_list[round((size-1)/3)*3]), (x, y), (0, 255, 0), 4)
        cv.circle(img, (x, y), 5, (0, 0, 255), cv.FILLED)
        # cv.imshow('img', img)
        point_list.append([x, y])
        print(point_list)


def gradient(pt1, pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def get_angle():
    pt1, pt2, pt3 = point_list[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angle_rad = math.atan((m2-m1)/(1 - (m2*m1)))
    angle_deg = round(math.degrees(angle_rad))
    # print(angle_deg)
    cv.putText(img, str(abs(angle_deg)), (pt1[0]-40, pt1[1]-20), cv.FONT_HERSHEY_COMPLEX, 1.5, (0,0,255), 2)

img = cv.imread("./imgs/pre_tope.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

while True:

    if len(point_list) % 3 == 0 and len(point_list) != 0:
        get_angle()

    cv.imshow('img', img)
    cv.setMouseCallback('img',clickEvent)
    if cv.waitKey(1) == ord('d'):
        break

    if cv.waitKey(1) & 0xff == ord('c'):
        point_list = list()
        img = cv.imread("./imgs/pre_tope.jpg")
