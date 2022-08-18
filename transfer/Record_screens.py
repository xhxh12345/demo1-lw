
from flask import Flask, render_template, Response
import io
# import cv2
# from opencv-python
import uuid, socket
import pandas as pd
from desktopmagic.screengrab_win32 \
    import (getDisplayRects, getRectAsImage)

from PIL import ImageGrab

# from openpyxl import load_workbook

# 获取本机ip
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)




#开始主程序
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:

        screens = getDisplayRects()

        documents = io.BytesIO()

        image = ImageGrab.grab(bbox=screens[int(0)], all_screens=True)  # 高速截屏，且内存占用较小

        # image.save("D:\AGITEST\AGIshow\data\\jieping.png", format="JPEG")  # 将画面保存到一个实体文件夹，这种方式就是可以对文件进行加工和处理

        # img = cv2.imread("D:\AGITEST\AGIshow\data\\jieping.png")
        #
        # frame = cv2.imencode('.jpg', img)[1].tobytes()
        #

        image.save(documents, format="JPEG")  # 将画面保存到内存，不进行实体保存，这样就不需要进行独立的文件夹来进行支持

        frame = documents.getvalue()


        yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + frame)

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    # df1 = pd.read_excel("D:\pythonProject\AGIwebtest\AGIback.xlsx") #存放信息的EXCEL表格

    port1 = 5001

    ip = myaddr

    app.run(host=ip, port=port1, threaded=True)