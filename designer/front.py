from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from designer.ui import Ui_MainWindow
from designer.back import Worker


class Detect(QMainWindow, Ui_MainWindow):
    switch_camera = QtCore.pyqtSignal()
    switch_ip = QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.click)
        # self.pushButton_2.clicked.connect(self.click2)
        self.read_dictionary = np.load(r'/Users/jhchen/PycharmProjects/stones/my_file.npy', allow_pickle=True).item()
        self.figure1 = MyFigure()
        self.figure2 = MyFigure2()
        self.figure3 = MyFigure3()
        self.assist()

        self.work = Worker()
        self.work.sin_out.connect(self.time_click)
        self.work.start()

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

    def visual_image(self, frame):
        # img = self.read_image()
        # img = cv2.resize(img, (144 * 5, 108 * 4))
        # frame = QImage(img, 144 * 5, 108 * 4, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        item = QGraphicsPixmapItem(pix)  # 创建像素图元
        # self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(item)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

        self.graphicsView_5.setScene(self.scene)
        self.graphicsView_5.show()

    def time_click(self, frame, result):
        self.r1, self.r2, self.r3, self.r4 = result
        self.segmentation()
        self.visual_image(frame)
        self.draw1()
        self.draw2()
        self.draw3()

    def draw1(self):
        self.figure1.clear()
        self.figure1.add(self.r1, self.r2, self.r3, self.r4)
        self.figure1.draw()
        self.graphicsView_2.show()

    def draw2(self):
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

    def segmentation(self):

        self.textBrowser_5.setText('{:.2f}%'.format(float(self.r1)))
        self.textBrowser_6.setText('{:.2f}%'.format(float(self.r2)))
        self.textEdit_7.setText('{:.2f}%'.format(float(self.r3)))
        self.textBrowser_8.setText('{:.2f}%'.format(float(self.r4)))

        # self.textBrowser_12.setText('{:.2f}'.format(max(self.res)))
        # self.textBrowser_13.setText('{:}'.format(len(self.res)))

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