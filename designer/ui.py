from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.tabWidget.setCurrentIndex(0)
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
