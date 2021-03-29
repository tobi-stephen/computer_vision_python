import cv2 as cv
import numpy as np

pts = []
counter = 0


def mouseEvent(event, x, y, flags, params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)

        pts.append([x,y])
        counter = counter + 1
        # cv.circle(img, (x,y), 5, (0,255,0), thickness=cv.FILLED)


img = cv.resize(cv.imread('imgs/book3.jpg'), (320,480))
imgCopy = img.copy()

# matrix = cv.getPerspectiveTransform(np.float32(pts), np.float32(pts2))
# ret = cv.warpPerspective(img, matrix, (width, height))
# cv.imshow('ret', ret)

# for x in pts:
#     cv.circle(img,tuple(x), 5, (0,255,0), thickness=cv.FILLED)


def clear(_, __):
    print('clear')
    global pts, img, imgCopy
    pts = []
    cv.destroyWindow('ret')
    img = cv.resize(cv.imread('imgs/book3.jpg'), (320,480))

cv.namedWindow('img')
cv.createButton('clear', clear, None, cv.QT_NEW_BUTTONBAR)
cv.setMouseCallback('img', mouseEvent)

while True:

    if len(pts) == 4:
        width, height = (208, 350)
        # width, height = pts[1][0] - pts[0][0], pts[2][1] - pts[0][1]
        pts = [[29, 85], [237, 84], [24, 434], [243, 445]]
        pts2 = [[0, 0], [width, 0], [0, height], [width, height]]
        matrix = cv.getPerspectiveTransform(np.float32(pts), np.float32(pts2))
        ret = cv.warpPerspective(imgCopy, matrix, (width, height))
        cv.imshow('ret', ret)

    for x in pts:
        cv.circle(img, tuple(x), 5, (0,255,0), thickness=cv.FILLED)

    cv.imshow('img', img)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
