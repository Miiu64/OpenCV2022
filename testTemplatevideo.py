import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import Constants

capture = cv.VideoCapture(Constants.port)
lower_green = np.array([200, 200, 200])
upper_green = np.array([255, 255, 255])

template = cv.imread('Photos/templatezoomedout.png',0)

while True:
    isTrue, original = capture.read()
    mask = cv.inRange(original, lower_green, upper_green)
    cv.imwrite('Photos\mask.png', original)  

    img_rgb = cv.imread('Photos\mask.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
    
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.72
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(mask , pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
    cv.imshow('Final Result', mask)
    cv.imshow('gray', img_gray)
    if cv.waitKey(20) & 0xFF==ord('d'):
            break
capture.release()

cv.destroyAllWindows()
cv.waitKey(0)