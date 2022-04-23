"""行人追踪"""
import sys

import cv2 as cv
import numpy as np

video_path = "./src/person.mp4"  # 视频地址
step = 3  # 间隔多少秒检测一次

# body_cascade = cv.CascadeClassifier("./haarcascade_fullbody.xml")  #
body_cascade = cv.CascadeClassifier("./haarcascade_eye.xml")

video = cv.VideoCapture(video_path)
frame_num = video.get(cv.CAP_PROP_FRAME_COUNT)
frame_fps = video.get(cv.CAP_PROP_FPS)
frame_index: np.core.uint64 = 0

while frame_index < frame_num:
    video.set(cv.CAP_PROP_POS_FRAMES, frame_index)
    result, img = video.read()

    # img = cv.imread("./src/monitoring.jpg")
    # img = cv.imread("./src/img.png")

    if result:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # gray = img[:, :, 0] + img[:, :, 1] + img[:, :, 2]
        # t1, dst1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        dst1 = img
        bodys = body_cascade.detectMultiScale(dst1, 1.1, 5)
        print(bodys)
        for (x, y, w, h) in bodys:
            cv.rectangle(dst1, (x, y), (x + w, y + h), (0, 0, 255), 5)

        win_name = "img"
        cv.imshow(win_name, dst1)
        key = cv.waitKey(0)
        if key == 27:
            frame_index = frame_num
            cv.destroyWindow(win_name)
            break

    frame_index += np.core.uint64(step * frame_fps)

video.release()
print("结束 ")
sys.exit()
