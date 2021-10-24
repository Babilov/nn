import cv2
import pyautogui
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
cam = cv2.VideoCapture(0)


img_counter = 0
model = load_model('C:\\Users\\969\\PycharmProjects\\letnii_proekt\\model')
while True:

    ret, frame = cam.read()
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("window", frame)
    # rect = cv2.rectangle(frame, (0, 100), (250, 400), (0, 255, 0), 1)
    # cv2.imshow("window", rect)
    if not ret:
        print("failed to grab frame")
        break

    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        im = pyautogui.screenshot()
        labels = {0: 'A',
                  1: 'B',
                  2: 'C',
                  3: 'D',
                  4: 'E',
                  5: 'F',
                  6: 'G',
                  7: 'H',
                  8: 'I',
                  9: 'J',
                  10: 'K',
                  11: 'L',
                  12: 'M',
                  13: 'N',
                  14: 'O',
                  15: 'P',
                  16: 'Q',
                  17: 'R',
                  18: 'S',
                  19: 'T',
                  20: 'U',
                  21: 'V',
                  22: 'W',
                  23: 'X',
                  24: 'Y',
                  25: 'Z',
                  26: 'del',
                  27: 'space'}
        im.save('C:\\Users\\969\\PycharmProjects\\letnii_proekt\\current\\current\\cur.jpg')
        # im = im.resize((224,224))
        # im = np.asarray(im)
        # im = im[None, :, :, :]
        test_generator = ImageDataGenerator(
            preprocessing_function=preprocess_input
        )
        test_images = test_generator.flow_from_directory(
            directory='C:\\Users\\969\\PycharmProjects\\letnii_proekt\\current',
            target_size=(224, 224),
            color_mode='rgb',
            class_mode='categorical',
            batch_size=1,
            shuffle=False
        )
        pred = model.predict(test_images)



cam.release()
cv2.destroyAllWindows()
