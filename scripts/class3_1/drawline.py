"""绘制线段"""

import cv2 as cv
import numpy as np

img = np.ones((640, 960, 3), np.core.uint8)
img = cv.line(img, (0, 320), (960, 640), (0, 0, 125), 2)
img = cv.line(img, (0, 640), (480, 0), (0, 125, 0), 5)

cv.imshow("line", img)

cv.waitKey(0)
