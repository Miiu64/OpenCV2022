import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import Constants

original = cv.imread(Constants.MPRPhoto)
img = original[0:1080, 0:1920]
blank = np.zeros(img.shape, dtype = 'uint8')
# dst = cv.fastNlMeansDenoisingColored(img ,None, 20, 20, 11,29)
lower_green = np.array([230, 230, 230])
upper_green = np.array([255, 255, 255])

mask = cv.inRange(img , lower_green, upper_green)
cv.imwrite('Photos\mask.png', mask)  

img_rgb = cv.imread('Photos\mask.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Photos/templatezoomedout.png',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imshow('Final Result',img_rgb)
cv.waitKey(0)