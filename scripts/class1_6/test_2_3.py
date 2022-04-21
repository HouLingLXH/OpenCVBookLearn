"""通道测试"""

import cv2 as cv

image = cv.imread("./1.1.jpg")

bgra = cv.cvtColor(image, cv.COLOR_BGR2BGRA)

print(bgra.shape)
bgra[:, 20:50, 3] = 125

cv.imshow("image", image)
cv.imwrite("alpha.png", bgra)

cv.waitKey(0)
