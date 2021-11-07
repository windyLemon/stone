from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsPixmapItem, QGraphicsScene

import sys
from designer.front import Detect


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Detect()
    c.show()
    sys.exit(app.exec_())
