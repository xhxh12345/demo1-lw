import cv2
import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageTk
# 中文显示
def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype(
        "font/simhei.ttf", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)

# tk.canvas显示
def cv2img_to_tkimg(im,width,height):
    im = cv2.resize(im,(width,height))
    cvimage = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
    pilImage = PIL.Image.fromarray(cvimage)
    tkImage = PIL.ImageTk.PhotoImage(image=pilImage)
    return tkImage
