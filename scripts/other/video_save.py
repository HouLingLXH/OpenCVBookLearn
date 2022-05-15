"""保存摄像头数据为视频"""

import cv2

# 获取视频流
cap = cv2.VideoCapture(0)

# 设置视频编解码器，关乎保存文件的格式
# DIVX对应avi格式文件， MP4V对应mp4格式文件，输出时要对应好
# 其他编码格式可以去官网查看
forcc = cv2.VideoWriter_fourcc(*"DIVX")  # 参数其实是4个，用星号将字符串逐一分开
fps = 24  # 帧率，一般根据相机性能来
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 取相机自身的宽度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取相机自身的高度
writer = cv2.VideoWriter('scripts/other/video.avi', forcc, fps, (width, height))

while True:
    rel, frame = cap.read()
    frame = cv2.flip(frame, 1)  # 画面镜像，因为不镜像，画面是左右对称的
    writer.write(frame)

    cv2.imshow("video", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

writer.release()
cap.release()
