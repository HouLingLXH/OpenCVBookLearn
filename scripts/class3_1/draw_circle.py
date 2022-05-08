"""画圆"""
import random

import cv2 as cv
import numpy as np

img = np.ones((640, 960, 3), np.core.uint8)
img = cv.circle(img, (480, 320), 200, (68, 123, 98), 2)
img = cv.circle(img, (200, 320), 50, (156, 64, 112), -1)

for index in range(0, 50):
    center_x = int(random.random() * 960)
    center_y = int(random.random() * 640)
    radius = int(random.randint(1, 200))
    color = np.random.randint(0, 255, size=(3,)).tolist()
    img = cv.circle(img, (center_x, center_y), radius, color, -1)

cv.imshow("circle", img)
cv.waitKey(0)
