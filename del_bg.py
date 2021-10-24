import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#image = cv2.imread('C:\\Users\\969\\PycharmProjects\\letnii_proekt\\test\\a_help.jpg')
# image = cv2.imread('C:\\Users\\969\\jupyter\\data\\asl_alphabet_train\\asl_alphabet_train\\A\\A2000.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY_INV)[1]
# thresh = 255 - thresh
#
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# result = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
#
# cv2.imshow('result', result)
# cv2.imwrite('result.png', result)
# cv2.waitKey()

img = Image.open('C:\\Users\\969\\jupyter\\data\\asl_alphabet_train\\asl_alphabet_train\\A\\A1.jpg')
img = np.asarray(img)
img = np.copy(img)

# plt.imshow(img[:12, :, :])
# plt.show()

sumR = 0
sumG = 0
sumB = 0
k = 0
for x in img[:12, :, :]:
    for y in x:
        sumR += y[0]
        sumG += y[1]
        sumB += y[2]
        k += 1
print("R - ", sumR / k, "G - ", sumG / k, "B - ", sumB / k)

coef = 50
for x in img:
    for y in x:
        # print(y)
        if 95 + coef > y[0] > 95 - coef and \
                77 + coef > y[1] > 77 - coef and \
                40 + coef > y[2] > 40 - coef:
            y[0] = 255
            y[1] = 255
            y[2] = 255

plt.imshow(img[:, :, :])
plt.show()