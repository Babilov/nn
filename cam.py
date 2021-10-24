import cv2
import numpy as np
import os
import time

cap = cv2.VideoCapture(0)
fps = 40.0
image_size = (640, 480)
cur_let = 'del'
video_file = f'C:\\Users\\969\\PycharmProjects\\letnii_proekt\\vid_for_train\\{cur_let}.avi'

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size)

i = 0
while True:
    ret, frame = cap.read()
    out.write(frame)
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cap.release()
cv2.destroyAllWindows()

print("Successfully saved")


# vidcap = cv2.VideoCapture(f'C:\\Users\\969\\PycharmProjects\\letnii_proekt\\vid_for_train\\{cur_let}.avi')
# success, image = vidcap.read()
# count = 0
# while success:
#     cv2.imwrite(f"C:\\Users\\969\\PycharmProjects\\letnii_proekt\\train\\train\\{cur_let}\\{cur_let}{count}.jpg", image)  # save frame as JPEG file
#     success, image = vidcap.read()
#
#     print('Read a new frame: ', success)
#     count += 1
# print(count)