import cv2 as cv

cap = cv.VideoCapture(0)
# cap.set(3, 480)
# cap.set(4, 480)

ret, img = cap.read()
ret, img2 = cap.read()
img = cv.flip(img, 1)
img2 = cv.flip(img2, 1)

while cap.isOpened():
    diff = cv.absdiff(img, img2)
    # ret, diff = cap.read()
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 2)
    _, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
    dilated = cv.dilate(thresh, None, iterations=3)

    # canny = cv.Canny(blur, 100, 200)

    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(img, contours, -1, (0,255,0), 2, cv.FILLED)

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        area = cv.contourArea(contour)
        if area < 1500:
            continue

        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255,0), 2)
        cv.putText(img, "Status: {}".format("movement"), (10,20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv.imshow('gray', cv.flip(gray,1))
    cv.imshow('cap', img)
    img = img2
    ret, img2 = cap.read()
    img2 = cv.flip(img2, 1)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()