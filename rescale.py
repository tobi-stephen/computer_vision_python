import cv2 as cv
import sys

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# reading images
# img = cv.imread('imgs/dan.jpg')
#
# cv.imshow('Cat', img)
# img_scaled = rescaleFrame(img, 0.3)
# cv.imshow('img_scaled', img_scaled)
#
# cv.waitKey(0)

# def changeRes(capture, width, height):
#     # work on live videos only
#     capture.set(3, width)
#     capture.set(4, height)

# reading videos
capture = cv.VideoCapture('vids/her.mp4')

while True:
    ret, frame = capture.read()
    frame_scaled = rescaleFrame(frame, scale=0.74)

    cv.imshow('Video', frame)
    cv.imshow('Framed', frame_scaled)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
