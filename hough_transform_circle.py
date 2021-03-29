import cv2 as cv
import numpy as np

img = cv.imread('imgs/shape4.jpeg')
output = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)
edges = cv.medianBlur(blur, 5)

circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 50, param1=100, param2=50, minRadius=10, maxRadius=0)

circles_ = np.uint16(np.around(circles))

for circle in circles_[0, :]:
    x, y, r = circle.ravel()
    print(x,y,r)
    cv.circle(output, (x,y), r, (0,255,0), 3)
    cv.circle(output, (x,y), 2, (0,255, 255), 3)

cv.imshow('img', output)

cv.waitKey(0)
cv.destroyAllWindows()