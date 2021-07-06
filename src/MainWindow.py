from PyQt6 import QtWidgets
from ui.MainWindowUI import Ui_MainWindow
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)