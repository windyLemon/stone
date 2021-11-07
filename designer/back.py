from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from PyQt5.QtGui import QPixmap, QImage
import time
from rock_detect.check_rock import NetOutput
import os
import cv2


class Worker(QtCore.QThread):
    sin_out = QtCore.pyqtSignal(QtGui.QImage, list)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.w = True
        self.total = os.listdir('/Users/jhchen/PycharmProjects/stones/Desktop/seg1')
        self.iter = 0
        self.read_dictionary = np.load(r'/Users/jhchen/PycharmProjects/stones/my_file.npy', allow_pickle=True).item()
        self.seg = NetOutput()
        self.rank1 = 4.75
        self.rank2 = 10
        self.rank3 = 26.5

    def run(self):
        # schedule.every(10).seconds.do(self.detect)
        while self.w:
            self.detect()
            time.sleep(10)

    def detect(self):
        image = self.read_image()
        self.segmentation()
        self.sin_out.emit(image, self.res)

    def read_image(self):
        path = self.total[self.iter]
        self.read_path = os.path.join('/Users/jhchen/PycharmProjects/stones/Desktop/seg1', path)
        image = cv2.imread(os.path.join('/Users/jhchen/PycharmProjects/stones/Desktop/seg1', path))
        self.iter += 1
        if self.iter >= len(self.total):
            self.iter = 0
        image = cv2.resize(image, (144 * 5, 108 * 4))
        image = QImage(image, 144 * 5, 108 * 4, QImage.Format_RGB888)
        return image

    def segmentation(self):
        self.r1, self.r2, self.r3 = self.seg.check_rock_dist(self.read_path)
        self.r1, self.r2, self.r3 = self.r1 * 100, self.r2 * 100, self.r3 * 100
        self.r4 = 0
        self.res = [self.r1, self.r2, self.r3, self.r4]

    def __del__(self):
        self.w = False