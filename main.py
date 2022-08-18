import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk
import tkinter.messagebox
import cv2
from tkinter import filedialog
import image_split_and_concat


# 打开系统文件路径方法
# adpjfpoisshago
# afgagdjalksdf
# adslkfgjalkgj

# 主窗口
class master:
    def __init__(self, root):
        self.root = root
        self.root.geometry('%dx%d' % (1920, 1080))
        self.root.title('视频标记工具--10')
        frame1(self.root)


# 第一个页面 登录
class frame1:
    def __init__(self, root):
        self.root = root
        self.frame1 = tk.Frame(root)
        self.frame1.pack()
        self.username = tk.StringVar()
        self.username.set('skyagi')

        self.password = tk.StringVar()
        self.password.set('98743210')
        # 控件

        # 字体
        fontStyle = tkFont.Font(family="Lucida Grande", size=30)

        fontStyle2 = tkFont.Font(family="Lucida Grande", size=40)
        # 标题
        title = tk.Label(self.frame1, text='登 录Sky_AGI ', font=fontStyle2)
        # 用户名输入
        label1 = tk.Label(self.frame1, text='账号: ', font=fontStyle)

        entry1 = tk.Entry(self.frame1, textvariable=self.username, font=fontStyle)
        # 密码输入
        label2 = tk.Label(self.frame1, text='密码: ', font=fontStyle)
        entry2 = tk.Entry(self.frame1, show='*', textvariable=self.password, font=fontStyle)
        # 功能按钮
        button1 = tk.Button(self.frame1, text='登录', font=fontStyle, command=self.login)
        button2 = tk.Button(self.frame1, text='退出', font=fontStyle, command=self.quit)

        # 布局
        title.grid(column=2, row=0, pady=100, )
        label1.grid(column=1, row=1, pady=50)
        entry1.grid(column=2, row=1, pady=50)

        label2.grid(column=1, row=2, pady=20)
        entry2.grid(column=2, row=2, pady=20)

        button1.grid(column=1, row=3, pady=60)
        button2.grid(column=2, row=3, pady=60, sticky='e')

    def login(self):
        if self.username.get() == 'skyagi' and self.password.get() == '98743210':
            self.frame1.destroy()
            frame2(self.root)
        else:
            tk.messagebox.showwarning(title='错误', message='账号或密码有误，请重新输入！')

    def quit(self):
        root.destroy()


# 第二个页面 选择
class frame2:

    # 第二个页面2:
    def __init__(self, root):
        self.root = root
        self.frame2 = tk.Frame(root)
        self.frame2.pack()
        # 所有控件
        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        fontStyle2 = tkFont.Font(family="Lucida Grande", size=40)
        title = tk.Label(self.frame2, text='Ai视频分析系统', font=fontStyle2)
        button1 = tk.Button(self.frame2, text='常规', font=fontStyle, command=self.login_frame3)
        button2 = tk.Button(self.frame2, text='高密', font=fontStyle, command=self.login_frame4)
        button3 = tk.Button(self.frame2, text='退出', font=fontStyle, command=self.login_frame1)

        # 布局
        title.grid(column=2, row=0, pady=100)
        button1.grid(column=1, row=1, sticky='n')
        button2.grid(column=3, row=1, sticky='s')
        button3.grid(column=2, row=3, ipadx=50, pady=200)

    def login_frame3(self):
        self.frame2.destroy()
        frame3(self.root)

    def login_frame4(self):
        self.frame2.destroy()
        frame3(self.root)

    def login_frame1(self):
        self.frame2.destroy()
        frame1(self.root)


# 第三个页面 常规
class frame3:
    def __init__(self, root):
        self.root = root
        self.frame3 = tk.Frame(root)
        self.frame3.pack()
        # 所有控件

        fontStyle = tkFont.Font(family="Lucida Grande", size=14)
        event_str = tk.StringVar()
        cap_str = tk.StringVar()
        cap_str.set('请输入单路视频或者图像地址')
        fontStyle2 = tkFont.Font(family="Lucida Grande", size=20)

        title = tk.Label(self.frame3, text='Ai视频识别分析系统', font=fontStyle2)
        # 画布
        canvas1 = tk.Canvas(self.frame3, width=1536, height=864, bg='white')
        # notebook1
        frameOne = tkinter.Frame()
        frameTwo = tkinter.Frame()
        frame3 = tkinter.Frame()
        frame4 = tkinter.Frame()
        frame5 = tkinter.Frame()

        notebook1 = tkinter.ttk.Notebook(self.frame3)
        style = tk.ttk.Style()
        style.configure('TNotbook.tab', font=('Lucida Grande', '15'))
        notebook1.add(frameOne, text='数据输入')
        notebook1.add(frameTwo, text='模型选择')
        notebook1.add(frame3, text='权重选择')
        notebook1.add(frame4, text='FPS选择')
        notebook1.add(frame5, text='一键导入')

        #
        tk.Entry(frameOne, textvariable=cap_str, width=30).grid(row=1)
        tkinter.Button(frameOne, text='下一步', font=fontStyle).grid(column=1, row=1)

        #
        tkinter.Button(frameTwo, text='yolo', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frameTwo, text='paddle', font=fontStyle).grid(column=2, row=1)
        #
        tkinter.Button(frame3, text='p5', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frame3, text='e6e', font=fontStyle).grid(column=2, row=1)
        #
        tkinter.Button(frame4, text='1/s', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frame4, text='4/s', font=fontStyle).grid(column=2, row=1)
        tkinter.Button(frame4, text='16/s', font=fontStyle).grid(column=3, row=1)
        #
        tkinter.Button(frame5, text='编辑导入', font=fontStyle, command=self.open_excel).grid(column=1, row=1, padx=10)
        tkinter.Button(frame5, text='确认导入', font=fontStyle).grid(column=2, row=1)

        # entry1
        entry1 = tk.Entry(self.frame3, textvariable=event_str, width=20, font=(15))

        # notebook2
        frameThree = tkinter.Frame()
        frameFour = tkinter.Frame()

        notebook2 = tkinter.ttk.Notebook(self.frame3)
        notebook2.add(frameThree, text='事故灾难')
        notebook2.add(frameFour, text='自然灾害')

        tkinter.Button(frameThree, text='事件1', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frameThree, text='事件2', font=fontStyle).grid(column=1, row=2)

        tkinter.Button(frameFour, text='事件3', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frameFour, text='事件4', font=fontStyle).grid(column=1, row=2)

        # notebook3 数据筛选区
        notebook3 = tkinter.ttk.Notebook(self.frame3)
        frame5 = tkinter.Frame()
        notebook3.add(frame5, text='数据筛选')
        tkinter.Checkbutton(frame5, text='人', font=fontStyle).grid(column=1, row=1)
        tkinter.Checkbutton(frame5, text='车', font=fontStyle).grid(column=2, row=1)

        # notebook4 鼠标事件区
        notebook4 = tkinter.ttk.Notebook(self.frame3)
        frame6 = tkinter.Frame()
        notebook4.add(frame6, text='自定义标记画笔')
        tkinter.Button(frame6, text='矩形', font=fontStyle).grid(column=1, row=1)
        tkinter.Button(frame6, text='线条', font=fontStyle).grid(column=2, row=1)
        tk.Scale(frame6, from_=0, to=255, orient='horizontal', length=200).grid(column=1, row=2, columnspan=2)

        # 功能按钮
        tkinter.Button(self.frame3, text=' 退    出 ', font=fontStyle, command=self.login_frame2).grid(column=17, row=6)
        tkinter.Button(self.frame3, text=' 发布 web ', font=fontStyle).grid(column=17, row=7)
        tkinter.Button(self.frame3, text='发布到屏幕2', font=fontStyle, command=self.login_frame5).grid(column=17, row=8)

        # 布局
        title.grid(column=7, row=0, pady=20)
        canvas1.grid(column=0, row=1, columnspan=16, rowspan=9)
        notebook1.grid(column=17, row=1)

        entry1.grid(column=17, row=2, sticky='s')
        notebook2.grid(column=17, row=3)

        notebook3.grid(column=17, row=4)

        notebook4.grid(column=17, row=5)

    def login_frame5(self):
        print('XXXXXXXXXXXXXXXXXXX')
        # self.frame3.destroy()
        frame5()
        # self.frame3.wait_window(frame5)
        # self.root.wait_window(frame5)
        # frame5(self.root)

    def login_frame2(self):
        print('XXXXXXXXXXXXXXXXXXX')
        self.frame3.destroy()
        frame2(self.root)

    # 打开编辑配置表
    def open_excel(self):
        import os
        finPath = os.getcwd() + '/多路视频流导入配置表.xlsx'
        os.startfile(finPath)


# 第四个页面 高密
class frame4:
    def __init__(self, root):
        self.root = root
        self.frame4 = tk.Frame(root)
        self.frame4.pack()
        # 所有控件
        event_str = tk.StringVar()
        # 画布
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        title = tk.Label(self.frame4, text='Ai视频分析系统', font=fontStyle)

        canvas1 = tk.Canvas(self.frame4, width=1536, height=864, bg='white')
        # notebook1
        frameOne = tkinter.Frame()
        frameTwo = tkinter.Frame()

        notebook1 = tkinter.ttk.Notebook(self.frame4)
        notebook1.add(frameOne, text='选项卡1')
        notebook1.add(frameTwo, text='选项卡2')

        tkinter.Button(frameOne, text='按钮1').grid(column=1, row=1)
        tkinter.Button(frameOne, text='按钮2').grid(column=1, row=2)

        tkinter.Button(frameTwo, text='按钮1').grid(column=1, row=1)
        tkinter.Button(frameTwo, text='按钮2').grid(column=1, row=2)
        # entry1
        entry1 = tk.Entry(self.frame4, textvariable=event_str, width=20, font=(15))
        # notebook2
        frameThree = tkinter.Frame()
        frameFour = tkinter.Frame()

        notebook2 = tkinter.ttk.Notebook(self.frame4)
        notebook2.add(frameThree, text='类型1')
        notebook2.add(frameFour, text='类型2')

        tkinter.Button(frameThree, text='事件1').grid(column=1, row=1)
        tkinter.Button(frameThree, text='事件2').grid(column=1, row=2)

        tkinter.Button(frameFour, text='事件1').grid(column=1, row=1)
        tkinter.Button(frameFour, text='事件2').grid(column=1, row=2)

        # 功能按钮
        button1 = tkinter.Button(self.frame4, text='退出')
        button2 = tkinter.Button(self.frame4, text='发布web')
        button3 = tkinter.Button(self.frame4, text='发布到屏幕2', command=self.login_frame5)

        # 布局
        title.grid(column=7, row=0)
        canvas1.grid(column=0, row=1, columnspan=16, rowspan=9)
        notebook1.grid(column=17, row=1)

        entry1.grid(column=17, row=2)
        notebook2.grid(column=17, row=3)
        button1.grid(column=17, row=4)
        button2.grid(column=17, row=5)
        button3.grid(column=17, row=6)

    def login_frame5(self):
        print('XXXXXXXXXXXXXXXXXXX')
        self.frame4.destroy()
        frame5(self.root)


# 第五个页面
class frame5:
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.geometry("1920x1080+1920+0")
        self.frame5 = tk.Frame(self.root2)
        self.frame5.pack()
        # 所有控件
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        title = tk.Label(self.frame5, text='Ai视频识别分析系统', font=fontStyle)
        canvas1 = tk.Canvas(self.frame5, width=1574, height=885, bg='white')
        label1 = tk.Label(self.frame5, text='Ai识别分析结果显示', font=fontStyle, bg='white', height=12, width=39)
        canvas2 = tk.Canvas(self.frame5, width=320, height=180, bg='white')
        canvas3 = tk.Canvas(self.frame5, width=320, height=180, bg='white')
        # 布局




        title.grid(column=7, row=0, pady=20)
        canvas1.grid(column=0, row=1, columnspan=16, rowspan=9,pady =14)
        label1.grid(column=18, row=1)

        canvas2.grid(column=18, row=4)
        canvas3.grid(column=18, row=7)

        self.root2.bind("<Key>", self.black)
        self.root2.overrideredirect(True)
        self.root2.mainloop()

    def black(self, event):
        if event.keycode == 27:
            self.root2.destroy()
            self.frame5.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    master(root)
    root.overrideredirect(True)
    root.mainloop()
