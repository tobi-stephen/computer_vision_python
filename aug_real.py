import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
imgTarget = cv.imread('./imgs/switch.jpg')
vid = cv.VideoCapture('./vids/lanes.mp4')

ret, img = vid.read()
h, w, c = imgTarget.shape
print(h, w, c)
img = cv.resize(img, (w, h))

orb = cv.ORB_create(nfeatures=1000)
kp1, des1 = orb.detectAndCompute(imgTarget, None)
# imgTarget = cv.drawKeypoints(imgTarget, kp1, None)
print(len(des1))

while cap.isOpened():
    ret, img = vid.read()
    img = cv.resize(img, (w, h))
    ret, cam = cap.read()
    cam = cv.resize(cam, (w, h))


    kp2, des2 = orb.detectAndCompute(cam, None)
    # cam = cv.drawKeypoints(cam, kp2, None)
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    
    imgF = cv.drawMatches(imgTarget, kp1, cam, kp2, good, None)
    img2 = np.zeros_like(cam)
    
    if len(good) > 8:
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

        matrix, mask = cv.findHomography(srcPts, dstPts, cv.RANSAC, 5)
        print(matrix)

        pts = np.float32([[0,0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
        dst = cv.perspectiveTransform(pts, matrix)
        img2 = cv.polylines(cam, [np.int32(dst)], True, (255, 0, 255), 3)
        imgWarp = cv.warpPerspective(cam, matrix, (w, h))
    
    # cv.imshow('imgwarp', imgWarp)

    cv.imshow('cam', cam)
    cv.imshow('imgTarget', imgTarget)
    cv.imshow('img', img)
    cv.imshow('imgF', imgF)
    cv.imshow('img2', img2)
    
    if cv.waitKey(0) & 0xFF == ord('d'):
        break
    # if cv.waitKey(1) & 0xFF == ord('d'):
    #     break

cap.release()
cv.destroyAllWindows()