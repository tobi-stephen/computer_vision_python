import cv2 as cv


def clickEvent(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        xy = str(x) + ', ' + str(y)
        cv.putText(img, xy, (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (255, 255, 0), 2, cv.LINE_AA)
        cv.imshow('img', img)
    if event == cv.EVENT_RBUTTONDOWN:
        print('button down')
        b, g, r = img[x,y]
        print(b, g, r)

img = cv.imread('imgs/pre_tope.jpg')

cv.imshow('img', img)
cv.setMouseCallback('img', clickEvent)

cv.waitKey(0)
cv.destroyAllWindows()
