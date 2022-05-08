"""绘制多边形"""

import cv2 as cv
import numpy as np

img = np.zeros((640, 960, 3), np.core.uint8)

points = [(200, 20), (400, 20), (600, 600), (100, 600)]
points = np.array(points, np.core.int32)  # 首先转换为一个numpy.ndarray
points = [points]  # 再包成一个ndarray的列表
img = cv.polylines(img, points, True, (100, 20, 200))
cv.imshow("polylines", img)
cv.waitKey(0)
