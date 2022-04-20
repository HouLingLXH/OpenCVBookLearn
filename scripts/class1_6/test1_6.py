"""测试"""
import cv2 as cv

print("hello world")

filename = "./class1_6/1.1.jpg"
image = cv.imread(filename, cv.IMREAD_COLOR)
cv.imshow("image", image)

cv.waitKey(0)
