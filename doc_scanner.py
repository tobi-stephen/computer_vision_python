import cv2 as cv
import numpy as np

frameWidth = 640
frameHeigth = 480

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeigth)
cap.set(cv.CAP_PROP_BRIGHTNESS, 150)


def reorder(points):
    # print(points)
    points = points.reshape((4,2))
    pointsNew = np.zeros((4,1,2), np.int32)
    add = points.sum(axis=1)
    # print("add ", add)

    pointsNew[0] = points[np.argmin(add)]
    pointsNew[3] = points[np.argmax(add)]
    # print("new points ", pointsNew)

    diff = np.diff(points, axis=1)
    # print("diff ", diff)

    pointsNew[1] = points[np.argmin(diff)]
    pointsNew[2] = points[np.argmax(diff)]
    # print("final point order", pointsNew)

    return pointsNew


def getWarp(img, biggest):
    biggest = reorder(biggest)

    # pts = [[29, 85], [237, 84], [24, 434], [243, 445]]
    pts2 = [[0, 0], [frameWidth, 0], [0, frameHeigth], [frameWidth, frameHeigth]]
    matrix = cv.getPerspectiveTransform(np.float32(biggest), np.float32(pts2))
    ret = cv.warpPerspective(img, matrix, (frameWidth, frameHeigth))

    ret = ret[20: frameWidth-20, 20: frameHeigth-20]
    ret = cv.resize(ret, (frameHeigth, frameWidth))

    return ret


def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    maxArea = -1
    biggestContourApprox = np.array([])

    for contour in contours:
        area = cv.contourArea(contour)
        if area < 2000:
            continue
        # cv.drawContours(out, contour, -1, (0,255,255), 4)
        perimeter = cv.arcLength(contour, True)
        approxPoints = cv.approxPolyDP(contour, 0.03*perimeter, True)
        objPoints = len(approxPoints)
        # print(objPoints)
        if area > maxArea and objPoints == 4:
            biggestContourApprox = approxPoints
            maxArea = area
        # x, y, w, h = cv.boundingRect(contour)
    cv.drawContours(imgContour, biggestContourApprox, -1, (255, 0, 0), 20)

    return biggestContourApprox

def preProcess(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 1)
    canny = cv.Canny(blur, 150, 250)
    kernel = np.ones((5,5), dtype=np.uint8)
    dilated = cv.dilate(canny, kernel, iterations=2)
    eroded = cv.erode(dilated, kernel, iterations=1)

    return eroded

while cap.isOpened():
    _, frame = cap.read()
    if not _:
        print("as e dey hot")
        exit(1)
    frame = cv.flip(cv.resize(frame, (frameWidth, frameHeigth)), 1)
    out = frame.copy()
    imgContour = frame.copy()

    thresh = preProcess(frame)
    contour = getContours(thresh)
    # print(len(contour))

    if len(contour) == 4:
        out = getWarp(frame, contour)

#     cv.imshow('ret', warped_image)
# else:
    cv.imshow('ret', out)
    cv.imshow('res', imgContour)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()