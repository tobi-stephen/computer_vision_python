import cv2 as cv


cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        print("the end")
        exit(1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    # print(len(faces))

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

    cv.imshow('img', img)
    if cv.waitKey(33) & 0xff == ord('d'):
        break

cap.release()
cv.destroyAllWindows()