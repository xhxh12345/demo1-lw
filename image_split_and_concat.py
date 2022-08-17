#pictures9.py
import glob
import pandas as pd
import numpy as np
import cv2 as cv
from PIL import Image, ImageDraw, ImageFont


# 画布尺寸
ori_w = 1536
ori_h = 864

size = 1
scale = int(size ** 0.5)
new_w = int(ori_w / scale)
new_h = int(ori_h / scale)

data_frameA=pd.read_excel(r'E:\test_video\path_all.xlsx',usecols='D', header=None, keep_default_na=False)
path_list = data_frameA.values.tolist()

while [''] in path_list:
    path_list.remove([''])


def creat_no_signal(new_w, new_h):
    # 创建无信号图像
    no_signal_img = Image.new('RGB', (new_w, new_h), (0, 0, 0))
    font = ImageFont.truetype(font='font/simhei.ttf', size=25)
    draw = ImageDraw.Draw(no_signal_img)  # 绘图声明
    label = '未添加视频'
    label_size = draw.textsize(label, font)
    label = label.encode('utf-8')

    left = int((new_w - label_size[0]) / 2)
    top = int((new_h - label_size[1]) / 2)
    location = (left, top)
    draw.text(location, str(label,'UTF-8'), fill=(255, 255, 255), font=font)
    del draw

    no_signal_img = np.array(no_signal_img)
    no_signal_img= cv.rectangle(no_signal_img, (0, 0), (new_w-1, new_h-1), (0, 0, 255), 1)

    return no_signal_img


def concat(path_list, new_w, new_h):
    # 读取图像
    imgs = []
    for f in path_list:
        img = cv.imread(f[0], -1)
        img = cv.resize(img, (new_w, new_h), cv.INTER_CUBIC)
        img = cv.rectangle(img, (0, 0), (new_w - 1, new_h - 1), (0, 0, 255), 1)
        imgs.append(img)

    # 添加无信号图
    for j in range(size - len(path_list)):
        imgs.append(creat_no_signal(new_w, new_h))

    # 宫格排列
    if size == 1:  # 1宫格
        img_concat = imgs[0]
    elif size == 4:  # 4宫格
        img0 = np.concatenate(imgs[0:2], 1)  # 沿1轴横向拼接
        img1 = np.concatenate(imgs[2:4], 1)
        img_concat = np.concatenate([img0, img1], 0)  # 沿0轴纵向拼接
    elif size == 9:  # 9宫格
        img0 = np.concatenate(imgs[0:3], 1)  # 沿1轴横向拼接
        img1 = np.concatenate(imgs[3:6], 1)
        img2 = np.concatenate(imgs[6:], 1)
        img_concat = np.concatenate([img0, img1, img2], 0)  # 沿0轴纵向拼接
    elif size == 16:  # 16宫格
        img0 = np.concatenate(imgs[0:4], 1)  # 沿1轴横向拼接
        img1 = np.concatenate(imgs[4:8], 1)
        img2 = np.concatenate(imgs[8:12], 1)
        img3 = np.concatenate(imgs[12:16], 1)
        img_concat = np.concatenate([img0, img1, img2, img3], 0)  # 沿0轴纵向拼接

    return img_concat


image = concat(path_list, new_w, new_h)

cv.imshow("concat.jpg",image)
cv.waitKey(0)  # 无限期显示窗口
