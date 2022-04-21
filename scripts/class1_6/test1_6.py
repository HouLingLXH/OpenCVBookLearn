"""测试"""
import cv2 as cv

print("hello world")

filename = "./class1_6/1.1.jpg"
image = cv.imread(filename, cv.IMREAD_COLOR)
# px = image[:10, :100, :] = [0, 0, 0]

# gray = cv.cvtColor(image, cv.COLOR_HSV2BGR)

b, g, r = cv.split(image)

print(b.shape)

merged = cv.merge([b, g, r])
merged2 = cv.merge([b, b, r])

cv.imshow("merged", merged2)

# cv.imshow("image", image)

# gray = cv.imread(filename, cv.IMREAD_GRAYSCALE)
# cv.imshow("gray", gray)

cv.waitKey(0)
