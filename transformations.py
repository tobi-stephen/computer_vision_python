import cv2 as cv
import numpy as np

img_o = cv.imread('imgs/pre_tope.jpg')
img = cv.resize(img_o, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('img', img)

# translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # (width, height)

    # shifting values
    # x --> right
    # y --> down
    # -x --> left
    # -y --> up

    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 200)
cv.imshow('translated', translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    rotPoint = rotPoint or (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    print(rotMat)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -30, (100,100))
cv.imshow('rotated', rotated)

# r = rotate(rotated, -30)
# cv.imshow('rr', r)

# flip
flipped = cv.flip(img, 1)
cv.imshow('flipped', flipped)

cv.waitKey(0)