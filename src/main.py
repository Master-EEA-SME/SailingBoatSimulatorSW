from PyQt6 import QtWidgets 
import sys
from MainWindow import MainWindow

def main(argv):
    print("Hello, World!")
    app = QtWidgets.QApplication(argv)
    win = MainWindow()
    win.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main(sys.argv))