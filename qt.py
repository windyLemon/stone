from PyQt5.QtWidgets import QApplication
import sys
from old.tmp1 import Detect


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # w = MainWindow()
    # w.show()
    c = Detect()
    c.show()
    sys.exit(app.exec_())
        