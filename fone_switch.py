import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('test/F.jpg')
img = img.resize((200, 200))
img = np.asarray(img)
bg = Image.open('test/nothing1.jpg')
bg = np.asarray(bg)

sumR = 0
sumG = 0
sumB = 0
k = 0
for x in img[:, :90, :]:
    for y in x:
        sumR += y[0]
        sumG += y[1]
        sumB += y[2]
        k += 1
avgR = sumR / k
avgG = sumG / k
avgB = sumB / k
print("R - ", avgR, "G - ", avgG, "B - ", avgB)

#plt.imshow(img[90:, 100:130, :])
#plt.show()

sumR1 = 0
sumG1 = 0
sumB1 = 0
k1 = 0
for x in img[90:, 100:130, :]:
    for y in x:
        sumR1 += y[0]
        sumG1 += y[1]
        sumB1 += y[2]
        k1 += 1
print("R - ", sumR1 / k1, "G - ", sumG1 / k1, "B - ", sumB1 / k1)
coef = -20
alpha = 8
img = img.copy()
for x in img:
    for y in x:
        # print(y)
        if y[0] > avgR - coef and y[1] > avgG - coef and y[2] > avgB - coef:
            y[0] = 255
            y[1] = 255
            y[2] = 255
        if y[0] < y[1] + alpha:
            y[0] = 255
            y[1] = 255
            y[2] = 255
i = 0
for x in img:
    j = 0
    for y in x:
        if y[0] == 255 and y[1] == 255 and y[2] == 255:
            y[0] = bg[i, j, 0]
            y[1] = bg[i, j, 1]
            y[2] = bg[i, j, 2]
        j += 1
    i += 1
img = Image.fromarray(np.uint8(img)).convert('RGB')
img.save('C:\\Users\\969\\PycharmProjects\\letnii_proekt\\pj\\F.jpg')
# for x in img[112:, 80:92, :]:
#     for y in x:
#         if y[0] != 255 and y[1] != 255 and y[2] != 255:
#             print(y)
