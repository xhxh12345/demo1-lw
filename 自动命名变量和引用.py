import cv2 as cv
import pandas as pd


class image_read(object):
    def __init__(self, paths, size):
        '''
        :param paths:从表格中读取的一系列图像路径
        :param size:输入的宫格数，如4宫格、9宫格等
        '''
        ori_w = 1728
        ori_h = 942

        # ori_w = 1536
        # ori_h = 864

        scale = int(size ** 0.5)
        new_w = int(ori_w / scale)
        new_h = int(ori_h / scale)

        names = self.__dict__
        for i in range(len(paths)):
            names['img' + str(i)] = cv.resize(
                cv.imread(paths[i][0]),
                (new_w, new_h),
                cv.INTER_CUBIC)
            # names['img' + str(i)] = cv.imread(paths[i][0])
        self.l = len(names)

    def concat(self):
        # 动态调用
        for i in range(self.l):
            exec('cv.imshow(str(i), p.img{})'.format(i))
        cv.waitKey(0)  # 无限期显示窗口


#读取工作簿和工作簿中的工作表
data_frameA=pd.read_excel(r'E:\test_video\path_all.xlsx',usecols='C', header=None, keep_default_na=False)
path_list = data_frameA.values.tolist()

while [''] in path_list:
    path_list.remove([''])

p = image_read(path_list, 4)
p.concat()
