import cv2
cur_let = 'del'
vidcap = cv2.VideoCapture(f'C:\\Users\\969\\PycharmProjects\\letnii_proekt\\vid_for_train\\{cur_let}.avi')
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite(f"C:\\Users\\969\\PycharmProjects\\letnii_proekt\\train\\train\\{cur_let}\\{cur_let}{count}.jpg", image)  # save frame as JPEG file
    success, image = vidcap.read()

    print(f'[+] Read a new frame({cur_let, count}.jpg): ', success)
    count += 1
print(count)