import cv2 as cv
import datetime


def clickEvent(event, x, y, flags, params):
    global frame
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        xy = str(x) + ' ' + str(y)
        cv.putText(frame, xy, (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv.LINE_AA)
        cv.imshow('Video', frame)

# reading videos
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1020)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv.CAP_PROP_BRIGHTNESS, 1000)

fourcc = cv.VideoWriter_fourcc('X','V','I','D')
writer = cv.VideoWriter('vids/out.avi', fourcc, 33, (640,480))
ret, frame = capture.read()

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        writer.write(cv.flip(frame, 1))

    txt = 'Height: ' + str(capture.get(4)) + ' Width: ' + str(capture.get(3))
    cv.putText(frame, txt, (20, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2, cv.LINE_AA)
    cv.putText(frame, str(datetime.datetime.now()), (10, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),2, cv.LINE_AA)
    cv.imshow('Video', frame)
    cv.setMouseCallback('Video', clickEvent)

    if cv.waitKey(33) & 0xFF == ord('d'):
        break

writer.release()
capture.release()
cv.destroyAllWindows()
