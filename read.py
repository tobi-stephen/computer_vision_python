import cv2 as cv


# reading images
# img = cv.imread('imgs/dan.jpg')
#
# cv.imshow('Cat', img)
#
# k = cv.waitKey(0)
#
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('imgs/dan2.jpg', img)
#     cv.destroyAllWindows()

# reading videos
# capture = cv.VideoCapture('vids/her.mp4')
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1020)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv.CAP_PROP_BRIGHTNESS, 1000)

fourcc = cv.VideoWriter_fourcc('X','V','I','D')
writer = cv.VideoWriter('vids/out.avi', fourcc, 20, (640,480))

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        writer.write(cv.flip(frame, 1))

    cv.imshow('Video', frame)

    if cv.waitKey(33) & 0xFF == ord('d'):
        break

writer.release()
capture.release()
cv.destroyAllWindows()
