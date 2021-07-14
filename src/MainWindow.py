from PySide6 import QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.rotate)
        timer.start(100)
        self.rot = 0

    def rotate(self) -> None:
        self.ui.CompassWidget.rotate(self.rot)
        self.ui.WindWidget.rotate(self.rot)
        self.rot += 10