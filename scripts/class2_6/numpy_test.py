"""Numpy 测试"""
import numpy

# a = np.int8(3.14)
#
# print(a)

# b = np.float64(8)
# print(b)

# c = np.float(True)
# print(c)

# n1 = np.array([1, 2, 3])
# print(n1)

# n2 = np.array([[1.2, 2.3], [5.6, 7.7]])
# print(n2)

# n3 = numpy.array([1, 2, 3], numpy.core.float64)
# print(type(n3))

# n4 = numpy.array([1, 2, 3], ndmin=3)
# print(n4)

# n1 = numpy.empty([2, 3])
# print(n1)

# n2 = numpy.ones([3, 4])
# print(n2)

# n3 = numpy.zeros([3, 2], numpy.core.uint)
# print(n3)

# n4 = numpy.random.randint(1, 5, 3)
# print(n4)

# n5 = numpy.random.randint(1, 6, [2, 3])
# print(n5)

#
# n1 = numpy.array([1, 2])
# n2 = numpy.array([3, 4])
# print(n1 + n2)
# print(n1 * n2)
# print(n1 / n2)
# print(n1 ** n2)
# print(n1 > n2)


# n1 = numpy.array([1, 3, 5])
# n2 = n1.copy()
# n2[0] = 6
#
# print(n1)
# print(n2)

# n1 = numpy.array([[1, 2, 3], [4, 5, 6]])
# print(n1)
# print(n1[0, 0])
# print(n1[0][1])

# img1 = numpy.zeros([640, 960], numpy.core.uint8)
# img1[::40, 100:400] = 255
# cv2.imshow("图像", img1)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


# img2 = numpy.zeros([640, 960, 3], numpy.core.uint8)
# img2[:, :, 0] = 255
# cv2.imshow("img", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img3 = numpy.random.randint(0, 256, [640, 960, 3], numpy.core.uint8)
# cv2.imshow("img", img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


a = numpy.array([1, 2, 3])
b = numpy.array([4, 5, 6])

c = numpy.vstack((a, b))
print(c)
