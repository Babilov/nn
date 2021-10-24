import cv2
from PIL import Image
import matplotlib.pyplot as plt
for i in range(1, 6):
    im = Image.open("opencv_frame_" + str(i) + ".png")
    size = (128, 128)
    out = im.resize(size)
    out.save('resize-output{}.png'.format(i))
