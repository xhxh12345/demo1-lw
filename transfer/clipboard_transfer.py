# coding=utf-8

import win32clipboard as wc
import win32con
import pyautogui as pg
import time
import win32api


def getText():
    # 开始剪切板操作
    wc.OpenClipboard()
    # 读取剪切板
    txt_get = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    if 'this_is_mouse_opt' in txt_get:  # 如果是鼠标操作
        txt_list = txt_get.split(' ')
        xy = txt_list[1].split(',')  # 鼠标操作坐标
        x = int(xy[0])
        y = int(xy[1])
        if txt_list[2] == 'left':
            print('左键:', x, y)
            pg.click(x, y)
        elif txt_list[2] == 'right':
            print('右键:', x, y)
            pg.rightClick(x, y)
        elif txt_list[2] == 'double':
            print('双击:', x, y)
            pg.doubleClick(x, y)
    wc.CloseClipboard()
    # return txt_get


def setText(aString):  # 写入剪切板t
    # print('str:', aString)

    # 开始剪切板操作
    wc.OpenClipboard()
    # 清空剪切板
    wc.EmptyClipboard()

    # 尝试将处理完的字符放入剪切板，注意这里用的是win32con.CF_UNICODETEXT，
    # 如果使用win32con.CF_TEXT则需要对txt进行编码，否则会出现乱码。
    wc.SetClipboardData(win32con.CF_UNICODETEXT, aString)

    # 关闭剪切板
    wc.CloseClipboard()



if __name__ == '__main__':
    string = "this_is_mouse_opt 100,15 double"
    setText(string)  # 将“test”写入剪切板
    time.sleep(3)
    getText()
    # 自动粘贴剪切板中的内容
    # win32api.keybd_event(17, 0, 0, 0)  # ctrl的键位码是17
    # win32api.keybd_event(86, 0, 0, 0)  # v的键位码是86
    # win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    # win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(13, 0, 0, 0)  # Enter的键位码是13
    # win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)