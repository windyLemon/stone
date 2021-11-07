from old.Main import MainWindow
from old.lin import Detect
from old.camera_dialog import CameraNew
from old.ip import IP


class Controller:
    def __init__(self):
        self.main_window = MainWindow()
        self.detect = Detect()
        self.camera = CameraNew()
        self.cur_window = self.main_window
        self.ip = IP()

    def show_main(self):
        self.cur_window.hide()
        self.main_window.show()
        self.main_window.switch_window.connect(self.show_detect)
        self.cur_window = self.main_window

    def show_detect(self):
        self.cur_window.hide()
        self.detect.show()
        self.detect.switch_camera.connect(self.show_camera)
        self.detect.switch_ip.connect(self.show_ip)
        self.cur_window = self.detect

    def show_camera(self):
        self.camera.show()

    def show_ip(self):
        self.ip.show()
