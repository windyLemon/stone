# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from preprocess import preprocess
from segmentation import binary_image, segmentation, auto_canny, calculate, algorithm_watershed
import numpy as np
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import time
import os
import matplotlib.pyplot as plt
from rock_detect.check_rock import NetOutput
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1239, 919)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1221, 901))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 741, 441))
        self.graphicsView.setObjectName("graphicsView")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_9.setGeometry(QtCore.QRect(240, 470, 251, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 510, 741, 351))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(900, 70, 201, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 1, 1, 1, 1)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout.addWidget(self.textBrowser_8, 3, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 0, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 3, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)
        self.textEdit_7 = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_7.setObjectName("textEdit_7")
        self.gridLayout.addWidget(self.textEdit_7, 2, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 0, 1, 1, 1)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_11.setGeometry(QtCore.QRect(930, 20, 131, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(900, 280, 201, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout_2.addWidget(self.textBrowser_7, 1, 0, 1, 1)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.gridLayout_2.addWidget(self.textBrowser_12, 0, 1, 1, 1)
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout_2.addWidget(self.textBrowser_13, 1, 1, 1, 1)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_4.setGeometry(QtCore.QRect(760, 510, 441, 351))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_18.setGeometry(QtCore.QRect(870, 470, 251, 31))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 510, 741, 351))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_10.setGeometry(QtCore.QRect(240, 470, 251, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_5.setGeometry(QtCore.QRect(10, 10, 741, 441))
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_16.setGeometry(QtCore.QRect(310, 270, 71, 31))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 270, 311, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_17.setGeometry(QtCore.QRect(310, 310, 71, 31))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 310, 311, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_14.setGeometry(QtCore.QRect(370, 160, 311, 31))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser_15.setGeometry(QtCore.QRect(290, 220, 61, 31))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(370, 220, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.actiongongneng = QtWidgets.QAction(MainWindow)
        # self.actiongongneng.setObjectName("actiongongneng")
        # self.actiongongenng2 = QtWidgets.QAction(MainWindow)
        # self.actiongongenng2.setObjectName("actiongongenng2")
        # self.actionMain_interface = QtWidgets.QAction(MainWindow)
        # self.actionMain_interface.setObjectName("actionMain_interface")
        # self.actionCamera = QtWidgets.QAction(MainWindow)
        # self.actionCamera.setObjectName("actionCamera")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">实时粒度统计</p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">222</p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">444</p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">三级尺寸</p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">四级尺寸</p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">二级尺寸</p></body></html>"))
        self.textEdit_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">333</p></body></html>"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">一级尺寸</p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">111</p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">粒度分布</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">最大粒径</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">石子数目</p></body></html>"))
        self.textBrowser_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">实时粒度统计(饼图)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">当前粒度分布</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">光照设置</p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">光圈设置</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IP设置</p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输入</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        # self.actiongongneng.setText(_translate("MainWindow", "gongneng"))
        # self.actiongongenng2.setText(_translate("MainWindow", "gongenng2"))
        # self.actionMain_interface.setText(_translate("MainWindow", "Main interface"))
        # self.actionCamera.setText(_translate("MainWindow", "Camera"))


class Detect(QMainWindow, Ui_MainWindow):
    switch_camera = QtCore.pyqtSignal()
    switch_ip = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.click)
        # self.pushButton_2.clicked.connect(self.click2)
        self.rank1 = 4.75
        self.rank2 = 10
        self.rank3 = 26.5

        self.figure1 = MyFigure()
        self.figure2 = MyFigure2()
        self.figure3 = MyFigure3()
        self.assist()

        self.work = TimerClick()
        self.work.sin_out.connect(self.time_click)
        self.work.start()

        self.total = os.listdir('/Users/jhchen/PycharmProjects/stones/Desktop/seg1')
        self.iter = 0

        self.read_dictionary = np.load(r'/Users/jhchen/PycharmProjects/stones/my_file.npy', allow_pickle=True).item()
        self.seg = NetOutput()

    def assist(self):
        self.figure_scene = QGraphicsScene()
        self.figure_scene.addWidget(self.figure1)
        self.graphicsView_2.setScene(self.figure_scene)
        self.scene = QGraphicsScene()

        self.figure_scene2 = QGraphicsScene()
        self.figure_scene2.addWidget(self.figure2)
        self.graphicsView_3.setScene(self.figure_scene2)

        self.figure_scene3 = QGraphicsScene()
        self.figure_scene3.addWidget(self.figure3)
        self.graphicsView_4.setScene(self.figure_scene3)

    def visual_image(self, img):
        # img = self.read_image()
        img = cv2.resize(img, (144 * 5, 108 * 4))
        frame = QImage(img, 144 * 5, 108 * 4, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(item)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

        self.graphicsView_5.setScene(self.scene)
        self.graphicsView_5.show()

    def time_click(self):
        img = self.read_image()
        self.segmentation(img)
        self.visual_image(img)
        self.draw1()
        self.draw2()
        self.draw3()

    def draw1(self):
        self.figure1.clear()
        self.figure1.add(self.r1, self.r2, self.r3, self.r4)
        self.figure1.draw()
        self.graphicsView_2.show()

    def draw2(self):
        # y = [0 for _ in range(10)]
        # for i in range(9):
        #     y[i] = ((self.res > self.figure2.x[i]) & (self.res < self.figure2.x[i+1])).sum() / len(self.figure2.x) * 100
        # y[9] = (self.res > self.figure2.x[9]).sum() / len(self.figure2.x) * 100
        y1 = [self.r1, self.r2, self.r3]
        y2 = self.read_dictionary[list(self.read_dictionary.keys())[0]]
        self.figure2.clear()
        self.figure2.add(y1, y2)
        self.figure2.draw()
        self.graphicsView_3.show()

    def draw3(self):
        self.figure3.clear()
        self.figure3.add(self.r1, self.r2, self.r3, self.r4)
        self.figure3.draw()
        self.graphicsView_3.show()

    def segmentation(self, image):
        # v, final = algorithm_watershed(image)
        # self.res = np.array(calculate(v, final))
        # self.r1 = (self.res > self.rank3).sum() / len(self.res) * 100
        # self.r2 = (self.res < self.rank1).sum() / len(self.res) * 100
        # self.r3 = ((self.rank2 > self.res) & (self.res > self.rank1)).sum() / len(self.res) * 100
        # self.r4 = ((self.rank3 > self.res) & (self.res > self.rank2)).sum() / len(self.res) * 100

        self.r1, self.r2, self.r3 = self.seg.check_rock_dist(self.read_path)
        self.r1, self.r2, self.r3 = self.r1 * 100, self.r2 * 100, self.r3 * 100
        self.r4 = 0
        self.res = [self.r1, self.r2, self.r3]
        self.textBrowser_5.setText('{:.2f}%'.format(float(self.r1)))
        self.textBrowser_6.setText('{:.2f}%'.format(float(self.r2)))
        self.textEdit_7.setText('{:.2f}%'.format(float(self.r3)))
        self.textBrowser_8.setText('{:.2f}%'.format(float(self.r4)))

        self.textBrowser_12.setText('{:.2f}'.format(max(self.res)))
        self.textBrowser_13.setText('{:}'.format(len(self.res)))
        return image

    def read_image(self):
        path = self.total[self.iter]
        self.read_path = os.path.join('/Users/jhchen/PycharmProjects/stones/Desktop/seg1', path)
        image = cv2.imread(os.path.join('/Users/jhchen/PycharmProjects/stones/Desktop/seg1', path))
        self.iter += 1
        if self.iter >= len(self.total):
            self.iter = 0
        return image

    def switch1(self):
        self.switch_camera.emit()

    def switch2(self):
        self.switch_ip.emit()


class MyFigure(FigureCanvas):
    def __init__(self, parent=None, width=4.3, height=3.3):
        fig = Figure(figsize=(width, height))

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)
        fig.tight_layout()
        self.x = [1, 2, 3, 4, 5, 6, 7, 8, 9][::-1]
        self.y1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.y4 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def add(self, item1, item2, item3, item4):
        self.y1.pop(0)
        self.y2.pop(0)
        self.y3.pop(0)
        self.y4.pop(0)

        self.y1.append(item1)
        self.y2.append(item2)
        self.y3.append(item3)
        self.y4.append(item4)
        l1 = self.axes.plot(self.x, self.y1, label='1')
        l2 = self.axes.plot(self.x, self.y2, label='2')
        l3 = self.axes.plot(self.x, self.y3, label='3')
        l4 = self.axes.plot(self.x, self.y4, label='4')

        self.axes.set_xlabel('time')
        self.axes.set_ylabel('Particle size distribution')

        self.axes.margins(0.)
        # self.axes.subplots_adjust(bottom=0.)

        self.axes.grid()
        self.axes.legend()
        self.axes.set_ylim(0, 100)

    def clear(self):
        self.axes.clear()


class MyFigure2(FigureCanvas):
    def __init__(self, parent=None, width=4.3, height=3.3):
        fig = Figure(figsize=(width, height))

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)
        fig.tight_layout()
        # self.x = [2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 22.5, 25]
        self.x = [1, 10, 26.5]

    def add(self, y1, y2):
        self.axes.plot(self.x, y1)
        self.axes.plot(self.x, y2)
        self.axes.set_xlabel('Particle size')
        self.axes.set_ylabel('Particle size distribution')

        self.axes.margins(0.)
        self.axes.grid()
        self.axes.set_ylim(0, 100)

    def clear(self):
        self.axes.clear()


class MyFigure3(FigureCanvas):
    def __init__(self, parent=None, width=4.3, height=3.3):
        fig = Figure(figsize=(width, height))

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)

    def add(self, item1, item2, item3, item4):
        y = np.array([item1, item2, item3, item4])
        self.axes.pie(y, labels=['1', '2', '3', '4'], colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],
                      autopct='%.2f%%')

    def clear(self):
        self.axes.clear()


class TimerClick(QtCore.QThread):
    sin_out = QtCore.pyqtSignal()

    def __init__(self):
        super(TimerClick, self).__init__()
        self.w = True

    def run(self) -> None:
        while self.w:
            if time.gmtime().tm_sec % 10 == 0:
                self.sin_out.emit()
                self.sleep(1)

    def __del__(self):
        self.w = False


class Worker(QtCore.QThread):
    sinOut = QtCore.pyqtSignal(str, QtGui.QImage)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.w = True
        self.num = 0

    def run(self):
        while self.w:
            # 获取文本
            file_str = 'File index{0}'.format(self.num)
            self.num += 1
            # 发射信号
            self.sinOut.emit(file_str)
            # 线程休眠2秒
            self.sleep(2)

    def __del__(self):
        # 线程状态改变与线程终止
        self.w = False
        self.wait()
