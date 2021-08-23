from PySide6 import QtGui, QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
from Comm import Comm
import logging
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        self.ui.CapControlMinusButton.clicked.connect(self.ui.BoatWidget.insert)
        self.ui.CapControlPlusButton.clicked.connect(self.ui.BoatWidget.extract)
        self.__checkPortTimer = QtCore.QTimer(self)
        self.__checkPortTimer.timeout.connect(self.scanPorts)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.rotate)
        timer.start(100)
        self.rot = 0
        self.__Comm = Comm()
        self.cnt = 0
        self.pwmR = 0
        self.pwmG = 0
        self.pwmB = 0
        self.ui.CompassACWButton.clicked.connect(self.minusR)
        self.ui.CompassCWButton.clicked.connect(self.plusR)
        self.ui.WdACWButton.clicked.connect(self.minusG)
        self.ui.WdCWButton.clicked.connect(self.plusG)
        self.ui.WfDecreaseButton.clicked.connect(self.minusB)
        self.ui.WfIncreaseButton.clicked.connect(self.plusB)
        self.portActionGroup = QtGui.QActionGroup(self)
        self.portActionGroup.setExclusive(True)
        self.baudrateActionGroup = QtGui.QActionGroup(self)
        for action in self.ui.menuBaudRate.actions():
            self.baudrateActionGroup.addAction(action)
            action.setCheckable(True)
            if action.text() == "115200":
                action.setChecked(True)
        self.baudrateActionGroup.setExclusive(True)
        self.ui.menuBaudRate.triggered.connect(self.__baudSelected)
        self.ui.menuSerialPort.aboutToShow.connect(self.scanPorts)
        self.ui.menuPort.triggered.connect(self.__portSelected)
        self.ui.menuBaudRate.setEnabled(False)
        self.ui.actionOpen.setEnabled(False)
        self.ui.actionOpen.triggered.connect(self.__openClosePort)
    def __portSelected(self, action : QtGui.QAction):
        self.ui.menuBaudRate.setEnabled(True)
        self.ui.actionOpen.setEnabled(True)
        if self.__Comm.getPort() != self.portActionGroup.checkedAction().text() and self.__Comm.isOpen():
            self.__openClosePort()
    def __openClosePort(self):
        if not self.__Comm.isOpen():
            self.__Comm.setConfig(self.portActionGroup.checkedAction().text(), int(self.baudrateActionGroup.checkedAction().text()))
            self.__Comm.open()
            logging.info("Opened {0}, baud = {1}".format(self.portActionGroup.checkedAction().text(), int(self.baudrateActionGroup.checkedAction().text())))
            self.ui.actionOpen.setText("Close")
            self.__checkPortTimer.start(1000)
        else:
            self.__Comm.close()
            logging.info("Closed {0}".format(self.__Comm.getPort()))
            self.ui.actionOpen.setText("Open")
            self.__checkPortTimer.stop()

    def rotate(self) -> None:
        self.ui.CompassWidget.rotate(self.rot)
        self.ui.WindWidget.rotate(self.rot)
        self.rot += 10
    def minusR(self):
        self.pwmR -= 1000
        if self.pwmR < 1:
            self.pwmR = 1
        for i in range(2):
            self.__Comm.writeAt(0x80 + i*0x30, 2, int(self.pwmR).to_bytes(2, 'little'), True)
    def minusG(self):
        self.pwmG -= 1000
        if self.pwmG < 1:
            self.pwmG = 1
        for i in range(2):
            self.__Comm.writeAt(0x80 + 0x10 + i*0x30, 2, int(self.pwmG).to_bytes(2, 'little'), True)
    def minusB(self):
        self.pwmB -= 1000
        if self.pwmB < 1:
            self.pwmB = 1
        for i in range(2):
            self.__Comm.writeAt(0x80 + 0x20 + i*0x30, 2, int(self.pwmB).to_bytes(2, 'little'), True)
    def plusR(self):
        self.pwmR += 1000
        if self.pwmR >= 32767:
            self.pwmR = 32767
        for i in range(2):
            self.__Comm.writeAt(0x80 + i*0x30, 2, int(self.pwmR).to_bytes(2, 'little'), True)
    def plusG(self):
        self.pwmG += 1000
        if self.pwmG >= 32767:
            self.pwmG = 32767
        for i in range(2):
            self.__Comm.writeAt(0x80 + 0x10 + i*0x30, 2, int(self.pwmG).to_bytes(2, 'little'), True)
    def plusB(self):
        self.pwmB += 1000
        if self.pwmB >= 32767:
            self.pwmB = 32767
        for i in range(2):
            self.__Comm.writeAt(0x80 + 0x20 + i*0x30, 2, int(self.pwmB).to_bytes(2, 'little'), True)
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

    def scanPorts(self):
        disconnected = True
        if self.portActionGroup.checkedAction() != None:
            currentPort = self.portActionGroup.checkedAction().text()
        else:
            currentPort = ''
        import serial.tools.list_ports
        portList = serial.tools.list_ports.comports()
        self.ui.menuPort.clear()
        if len(portList):
            self.ui.menuPort.setDisabled(False)
            portList.sort()
            for port in portList:
                self.ui.menuPort.addAction(port.name)
                if currentPort == port.name:
                    self.ui.menuPort.actions()[-1].setChecked(True)
                    disconnected = False        
        else:
            self.ui.menuPort.setDisabled(True)
        if disconnected:
            self.ui.menuBaudRate.setDisabled(True)
            self.ui.actionOpen.setDisabled(True)
            self.ui.actionOpen.setText("Open")
            if self.__Comm.isOpen():
                self.__openClosePort()
        for action in self.ui.menuPort.actions():
            self.portActionGroup.addAction(action)
            action.setCheckable(True)
    def __baudSelected(self, action : QtGui.QAction):
        baud = int(action.text())
        logging.info("Changed baud to {0}".format(baud))
        self.__Comm.setConfig(baud=baud)