import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# smoothing ==> blur ==> filter

img = cv.imread('imgs/lenna.png')
w, h = int(img.shape[1] * 0.5), int(img.shape[0]*0.5)
img = cv.resize(img, (w, h))
# cv.imshow('img', img)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.uint8)/25

# homogenous 2D convolution using custom kernel
conv2D = cv.filter2D(rgb, -1, kernel)
# cv.imshow('2D conv', cv.cvtColor(conv2D, cv.COLOR_RGB2BGR))

# NB: boxFilter ==> blur ==> filter2D can be used interchangeabl
# average smoothing
avg = cv.blur(rgb, (5,5))
# cv.imshow('avg smoothing', avg)

# gaussian smoothing
gaussian_img = cv.GaussianBlur(rgb, (3,3), 0)
# cv.imshow('Gaussian blur', gaussian_img)

# median smoothing -- for removing salt/pepper noise
median_img = cv.medianBlur(rgb, 3)
# cv.imshow('median blur', median_img)

# bilateral smoothing -- preserve edges and borders while removing noises
bilateral = cv.bilateralFilter(rgb, 20, 30, 40)
# cv.imshow('bilateral', bilateral)

titles = ['orig', '2D Conv', 'blur', 'gaussian', 'median', 'bilateral']
images = [rgb, conv2D, avg, gaussian_img, median_img, bilateral]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
# cv.waitKey(0)