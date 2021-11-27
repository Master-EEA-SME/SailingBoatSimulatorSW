import os
import sys
from MainWindow import MainWindow
from PySide6 import QtWidgets
from PySide6 import QtGui, QtQml

def main(argv):
    app = QtWidgets.QApplication(argv)
    win = MainWindow()
    win.show()
    return app.exec()
    

if __name__ == "__main__":
    sys.exit(main(sys.argv))