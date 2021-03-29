import cv2 as cv
import numpy as np

# cap = cv.VideoCapture('vids/her.mp4')
cap = cv.VideoCapture(0)

bgfg = cv.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        print('the end')
        break

    frame = cv.flip(frame, 1)  #Horizontal Flip
    output = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.bilateralFilter(gray, 5, 50, 100)

    fgmask = bgfg.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv.erode(fgmask, kernel, iterations=1)
    res = cv.bitwise_and(gray, gray, mask=fgmask)

    contours, heirarchy = cv.findContours(res, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area < 500:
            continue
        hull = cv.convexHull(contour)
        # cv.drawContours(output, contour, -1, (0,0,255), 3)
        cv.drawContours(output, hull, -1, (0,255,0), 10)



    cv.imshow('vid', frame)
    cv.imshow('fg', fgmask)
    cv.imshow('res', res)
    cv.imshow('output', output)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()