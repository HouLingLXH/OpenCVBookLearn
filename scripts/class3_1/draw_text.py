"""绘制文字"""

import cv2 as cv
import numpy as np
# from PIL import ImageFont, ImageDraw, Image
import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw

img = np.zeros((640, 960, 3), np.core.uint8)
img = cv.putText(img, "Hello World!", (0, 60), cv.FONT_HERSHEY_SIMPLEX, 1, (125, 62, 89), 1, None, True)

img = cv.putText(img, "Hello World!", (0, 160), cv.FONT_HERSHEY_SIMPLEX, 1, (125, 62, 89), 1, None, False)

img_RGB = PIL.Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))  # 转换为RGB编码，然后从np数组转换为image对象
tex_draw = PIL.ImageDraw.Draw(img_RGB)  # 转换为简单的2D绘图界面PIL图像
fontStyle = PIL.ImageFont.truetype("scripts/class3_1/Deng.ttf", 30, encoding="utf-8")  # 加载字体与字号
tex_draw.text((0, 260), "你好", (230, 0, 0), fontStyle)  # 绘制文字，颜色为RGB格式
img = cv.cvtColor(np.asarray(img_RGB), cv.COLOR_RGB2BGR)  # 将image转换为np数组，然后从RGB转换为BGR

cv.imshow("text", img)
cv.waitKey(0)
