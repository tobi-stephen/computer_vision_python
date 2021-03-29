import cv2 as cv
import numpy as np

img = cv.imread('imgs/babe.jpg')
output = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), 0)

# blur = np.float32(blur)
# corners = cv.cornerHarris(blur, 2, 3, 0.04)
# corners = cv.dilate(corners, None)
#
# output[corners > 0.001*corners.max()] = [0,0,255]

corners = cv.goodFeaturesToTrack(blur, 0, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv.circle(output, (x,y), 5, (0,0,255), -1, lineType=cv.LINE_AA)

cv.imshow('ret', output)

cv.waitKey(0)
cv.destroyAllWindows()