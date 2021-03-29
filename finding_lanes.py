import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def makeCoord(image, line_params):
    try:
        slope, intercept = line_params
        y1 = img.shape[0]
        y2 = int(y1*(3/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
    except:
        return np.array([])
    return np.array([x1, y1, x2, y2])

def findSlopeIntercept(img, lines):
    right_fit = []
    mid_fit = []
    left_fit = []

    for line in lines:
        # print(line)
        if len(line[0]) < 4:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)

            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
        else:
            x1, y1, x2, y2 = line.reshape(4)
        params = np.polyfit((x1, x2), (y1, y2), 1)
        slope = params[0]
        intercept = params[1]
        # print(params)

        if slope > 0:
            mid_fit.append((slope, intercept))
        elif slope < -0.8:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))

    left_fit_avg = np.average(left_fit, axis=0)
    right_fit_avg = np.average(right_fit, axis=0)
    mid_fit_avg = np.average(mid_fit, axis=0)
    # print(left_fit_avg, 'left')
    # print(right_fit_avg, 'right')
    #
    left_line = np.array([])
    right_line = np.array([])
    mid_line = np.array([])
# if left_fit_avg :
    left_line = makeCoord(img, left_fit_avg)
# if right_fit_avg:
    right_line = makeCoord(img, right_fit_avg)
    mid_line = makeCoord(img, mid_fit_avg)

    return np.array([left_line, right_line, mid_line], dtype=object)


def cannyEdges(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    canny = cv.Canny(blur, 50, 150)
    return canny


def roi(img):
    height = img.shape[0]
    width = img.shape[1]
    # polygon = np.array([(500, height), (550,250), (0,500)])
    polygon = np.array([(200, height), (550,250), (1100, height)])
    # polygon = np.array([(2000, height), (1000,1233), (1350,1175), (width, height)]) for 'imgs/lanesmac,jpg'
    mask = np.zeros_like(img)
    cv.fillPoly(mask, [polygon], 255)
    masked_img = cv.bitwise_and(img, mask)
    return masked_img

def detectAndDisplayLines(img, lines):
    ret = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            # print(line)
            if not len(line):
                continue
            x1,y1,x2,y2 = line.reshape(4)
            cv.line(ret, (x1,y1), (x2,y2), (255,0,0), 5)


    return ret

# img = cv.imread('imgs/lanes.jpg')
# w, h = img.shape[1]//3, img.shape[0]//3
# img = cv.resize(img, (w, h))
# orig_img = img.copy()
# print(orig_img.shape[:2])

# canny = cannyEdges(orig_img)
# roiMask = roi(canny)
# lines = cv.HoughLinesP(roiMask, 2, np.pi / 180, 100, None, minLineLength=40, maxLineGap=5)
# # print(len(lines))
# avg_lines = findSlopeIntercept(orig_img, lines)
# print(len(avg_lines))
# line_image = detectAndDisplayLines(orig_img, avg_lines)
# combo_image = cv.addWeighted(orig_img, 0.8, line_image, 1, 1)

# cv.imshow('img', img)
# cv.imshow('gray', gray)
# cv.imshow('blur', blur)
# cv.imshow('canny', canny)
# cv.imshow('roiMask', roiMask)
# cv.imshow('line image', line_image)
# cv.imshow('result', line_image)
# cv.waitKey(0)
# cv.destroyAllWindows()

# plt.imshow(combo_image)
# plt.show()


cap = cv.VideoCapture('vids/lanes.mp4')

while True:
    ret, img = cap.read()

    if not ret:
        print('video done')
        exit(1)
    orig_img = img.copy()

    canny = cannyEdges(orig_img)
    roiMask = roi(canny)
    lines = cv.HoughLinesP(roiMask, 2, np.pi / 180, 100, None, minLineLength=40, maxLineGap=5)
    # lines = cv.HoughLines(roiMask, 2, np.pi/180, 100)
    # print(len(lines))
    avg_lines = findSlopeIntercept(orig_img, lines)
    # print(len(avg_lines))
    line_image = detectAndDisplayLines(orig_img, avg_lines)
    combo_image = cv.addWeighted(orig_img, 0.8, line_image, 1, 1)

    cv.imshow('result', combo_image)

    if cv.waitKey(33) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()