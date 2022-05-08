"""画矩形"""

import cv2 as cv
import numpy as np

img = np.zeros((640, 960, 3), np.core.uint8)
img = cv.rectangle(img, (480, 320), (500, 400), (125, 0, 0), 2)
img = cv.rectangle(img, (200, 200), (400, 300), (111, 222, 0), -1)

cv.imshow("rectangle", img)
cv.waitKey(0)
