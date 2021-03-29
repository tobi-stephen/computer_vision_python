import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('imgs/pre_tope.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print('check img file')
    exit(1)
_, mask = cv.threshold(img, 150, 250, cv.THRESH_BINARY_INV)

kernel = np.ones((7,7), np.uint8)

dilated = cv.dilate(mask, kernel, iterations=3)
# closed1 = cv.erode(dilated, kernel, iterations=3)

eroded = cv.erode(mask, kernel, iterations=3)
# opened1 = cv.dilate(eroded, kernel, iterations=3)

# erosion followed by dilation
opened = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=3)

# dilation followed by erosion
closed = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel, iterations=3)

# difference between dilation and erosion
morph_grad = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel, iterations=3)

# difference between image and opened image
top_hat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernel, iterations=3)

titles = ['orig', 'mask', 'dilated', 'eroded', 'opened', 'closed', 'morph_grad', 'top_hat']
images = [img, mask, dilated, eroded, opened, closed, morph_grad, top_hat]

for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()