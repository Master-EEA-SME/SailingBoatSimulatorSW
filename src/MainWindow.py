from PySide6 import QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
from Comm import Comm
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.ui.CapControlMinusButton.clicked.connect(self.ui.BoatWidget.insert)
        self.ui.CapControlPlusButton.clicked.connect(self.ui.BoatWidget.extract)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.rotate)
        timer.start(100)
        self.rot = 0
        self.ui.SimulateButton.clicked.connect(self.test)
        self.__Comm = Comm()
        self.__Comm.setConfig("COM5", 115200)
        self.__Comm.open()
        self.cnt = 0
        self.ui.CompassACWButton.clicked.connect(self.minus)
        self.ui.CompassCWButton.clicked.connect(self.plus)
    def rotate(self) -> None:
        self.ui.CompassWidget.rotate(self.rot)
        self.ui.WindWidget.rotate(self.rot)
        self.rot += 10
    def minus(self) -> None:
        for i in range(6):
            self.__Comm.writeAt(0x80 + i*0x10, 2, int(500).to_bytes(2, 'little'), True)
    def plus(self) -> None:
        for i in range(6):
            self.__Comm.writeAt(0x80 + i*0x10, 2, int(40000).to_bytes(2, 'little'), True)
    def test(self) -> None:
        dat = [0] * 16
        for i in range(len(dat)):
            temp = (self.cnt + i) % 256
            dat[i] = temp
        if not self.__Comm.writeAt(0x0, 16, dat, True):
            print("Write Ko")
        #else:
        #    print("Write Ok")
        rxDat = self.__Comm.readAt(0, 16, True)
        if rxDat != None:
            print("RxData :")
            print("    ", end='')
            for i in range(16):
                print(" {0:02X}".format(i), end='')
            print()
            for i in range(0, len(rxDat) - 1, 16):
                print("0x{0:02X}".format(i), end='')
                for j in range(16):
                    if i + j >= len(rxDat):
                        break
                    print(" {0:02X}".format(rxDat[i + j]), end='')
                print()
        self.cnt = (self.cnt + 1) % 256
