from PySide6 import QtGui, QtWidgets, QtCore
from ui.MainWindowUI import Ui_MainWindow
from fpga.Comm import Comm
from fpga.Components import *
import logging
import utils.utils as utils
class MainWindow(QtWidgets.QMainWindow):
    __REG_BASE = 0xC0
    __CAP_BASE = 0x40
    __ANEMO_BASE = 0x00
    __GIRO_BASE = 0x20
    __VERIN_BASE = 0x80
    __VERIN_ANGLE_BASE = 0xA0
    __POLLING_RATE_MS = 100
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        #self.ui.CapControlMinusButton.clicked.connect(self.ui.BoatWidget.insert)
        #self.ui.CapControlPlusButton.clicked.connect(self.ui.BoatWidget.extract)
        self.__checkPortTimer = QtCore.QTimer(self)
        self.__checkPortTimer.timeout.connect(self.scanPorts)
        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self.rotate)
        #timer.start(100)
        self.__WindForce = 0
        self.__WindDirection = 0
        self.__CompassDirection = 0
        self.__HydraulicPos = 50
        self.ui.CapControlMinusButton.clicked.connect(lambda : self.__updateHydraulic(self.__HydraulicPos - 10))
        self.ui.CapControlPlusButton.clicked.connect(lambda : self.__updateHydraulic(self.__HydraulicPos + 10))

        self.rot = 0
        self.__Comm = Comm()
        self.cnt = 0
        self.pwmR = 0
        self.pwmG = 0
        self.pwmB = 0
        self.pwmLR = Pwm(self.__Comm, 0x80, 4)
        self.pwmLG = Pwm(self.__Comm, 0x90, 4)
        self.pwmLB = Pwm(self.__Comm, 0xA0, 4)
        self.pwmRR = Pwm(self.__Comm, 0xB0, 4)
        self.pwmRG = Pwm(self.__Comm, 0xC0, 4)
        self.pwmRB = Pwm(self.__Comm, 0xD0, 4)
        self.__CapPwm = Pwm(self.__Comm, MainWindow.__CAP_BASE, 4)
        self.__AnemoPwm = Pwm(self.__Comm, MainWindow.__ANEMO_BASE, 4)
        self.__GiroPwm = Pwm(self.__Comm, MainWindow.__GIRO_BASE, 4)
        self.__VerinPwm = Pwm(self.__Comm, MainWindow.__VERIN_BASE, 4)
        #self.ui.CompassACWButton.clicked.connect(self.minusR)
        #self.ui.CompassACWButton.clicked.connect(self.__decreaseCompassAngle)
        self.ui.CompassACWButton.clicked.connect(lambda: self.__updateCompass((self.__CompassDirection - 10) % 360))
        self.ui.CompassCWButton.clicked.connect(lambda: self.__updateCompass((self.__CompassDirection + 10) % 360))
        #self.ui.CompassCWButton.clicked.connect(self.__increaseCompassAngle)
        #self.ui.CompassCWButton.clicked.connect(((lambda self, x: MainWindow.updateCompass(self, x))(self, self.__CompassDirection + 10)))
        #self.ui.WdACWButton.clicked.connect(self.minusG)
        #self.ui.WdCWButton.clicked.connect(self.plusG)
        #self.ui.WfDecreaseButton.clicked.connect(self.minusB)
        #self.ui.WfIncreaseButton.clicked.connect(self.plusB)
        self.ui.WdACWButton.clicked.connect(lambda: self.__updateWind((self.__WindDirection - 10) % 360, self.__WindForce))
        self.ui.WdCWButton.clicked.connect(lambda: self.__updateWind((self.__WindDirection + 10) % 360, self.__WindForce))
        self.ui.WfDecreaseButton.clicked.connect(lambda: self.__updateWind(self.__WindDirection, self.__WindForce - 10))
        self.ui.WfIncreaseButton.clicked.connect(lambda: self.__updateWind(self.__WindDirection, self.__WindForce + 10))
        self.ui.HydraulicManualControl.toggled.connect(self.__hydraulicManualControlEnableDisable)
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
        self.updateTimer = QtCore.QTimer(self)
        self.updateTimer.timeout.connect(self.__update)
        self.__updateCompass(0)
        self.__updateWind(0, 0)
        self.__hydraulicManualControlEnableDisable()
        self.__updateHydraulic(self.__HydraulicPos)
        self.__FpgaFreq = 0
        self.ui.BabordButton.pressed.connect(lambda : self.__sendBtnValue(0x4))
        self.ui.BabordButton.released.connect(lambda : self.__sendBtnValue(0x0))
        self.ui.StandbyButton.pressed.connect(lambda : self.__sendBtnValue(0x2))
        self.ui.StandbyButton.released.connect(lambda : self.__sendBtnValue(0x0))
        self.ui.TribordButton.pressed.connect(lambda : self.__sendBtnValue(0x1))
        self.ui.TribordButton.released.connect(lambda : self.__sendBtnValue(0x0))
        self.__initFPGA()

    def __hydraulicManualControlEnableDisable(self):  
        self.ui.CapControlMinusButton.setDisabled(not self.ui.HydraulicManualControl.isChecked())
        self.ui.CapControlPlusButton.setDisabled(not self.ui.HydraulicManualControl.isChecked())
    def __update(self):
        if self.__Comm.isOpen():
            if not self.ui.HydraulicManualControl.isChecked():
                freq = self.__VerinPwm.getFreq()
                duty = 0
                sens = 0
                if freq != 0:
                    duty = self.__VerinPwm.getDuty() / freq
                    freq = self.__FpgaFreq / freq
                    value = utils.map(duty, 0, 1, 0, 5)
                    sens = int.from_bytes(self.__Comm.readAt(MainWindow.__REG_BASE + 4, 1), 'little')
                    if sens:
                        value = -value
                    self.__updateHydraulic(self.__HydraulicPos + value)
#                    print("value = {0}".format(value))
#                print("sens = {0}".format(sens))
#                print("duty = {0}".format(duty))
#                print("freq = {0}".format(freq))
            leds_status = int.from_bytes(self.__Comm.readAt(MainWindow.__REG_BASE + 5, 1), 'little')
            self.ui.LedBabord.setChecked( leds_status & 0x4) 
            self.ui.LedStandby.setChecked(leds_status & 0x2) 
            self.ui.LedTribord.setChecked(leds_status & 0x1) 
                #self.__updateHydraulic()
        
#            self.pwmLR.getDuty()
#            self.pwmLG.getDuty()
#            self.pwmLB.getDuty()
#            self.pwmRR.getDuty()
#            self.pwmRG.getDuty()
#            self.pwmRB.getDuty()
        
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
            self.__FpgaFreq = int.from_bytes(self.__Comm.readAt(MainWindow.__REG_BASE, 4, True), 'little')
            if self.__FpgaFreq == 0:
                logging.info("Can't read Fpga frequency")
                self.__openClosePort()
            else:
                logging.info("Fpga freq = {0}".format(self.__FpgaFreq))
                self.__initFPGA()
                self.__checkPortTimer.start(1000)
                self.updateTimer.start(MainWindow.__POLLING_RATE_MS)
        else:
            self.__Comm.close()
            logging.info("Closed {0}".format(self.__Comm.getPort()))
            self.ui.actionOpen.setText("Open")
            self.__checkPortTimer.stop()
            self.updateTimer.stop()

    def rotate(self) -> None:
        self.ui.CompassWidget.rotate(self.rot)
        self.ui.WindWidget.rotate(self.rot)
        self.rot += 10
    def minusR(self):
        self.pwmR -= 10
        if self.pwmR <= 0:
            self.pwmR = 0
        value = int(self.pwmR / 100 * (2**32 - 1))
        self.pwmLR.setDuty(value)
        self.pwmRR.setDuty(value)
    def minusG(self):
        self.pwmG -= 10
        if self.pwmG <= 0:
            self.pwmG = 0
        value = int(self.pwmG / 100 * (2**32 - 1))
        self.pwmLG.setDuty(value)
        self.pwmRG.setDuty(value)
    def minusB(self):
        self.pwmB -= 10
        if self.pwmB <= 0:
            self.pwmB = 0
        value = int(self.pwmB / 100 * (2**32 - 1))
        self.pwmLB.setDuty(value)
        self.pwmRB.setDuty(value)
    def plusR(self):
        self.pwmR += 10
        if self.pwmR >= 100:
            self.pwmR = 100
        value = int(self.pwmR / 100 * (2**32 - 1))
        self.pwmLR.setDuty(value)
        self.pwmRR.setDuty(value)
    def plusG(self):
        self.pwmG += 10
        if self.pwmG >= 100:
            self.pwmG = 100
        value = int(self.pwmG / 100 * (2**32 - 1))
        self.pwmLG.setDuty(value)
        self.pwmRG.setDuty(value)
    def plusB(self):
        self.pwmB += 10
        if self.pwmB >= 100:
            self.pwmB = 100
        value = int(self.pwmB / 100 * (2**32 - 1))
        self.pwmLB.setDuty(value)
        self.pwmRB.setDuty(value)
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

    def __updateCompass(self, directionValue):
        self.__CompassDirection = directionValue
        self.ui.CompassValueLabel.setText("{0}°".format(self.__CompassDirection))
        self.ui.CompassWidget.rotate(self.__CompassDirection)
        if self.__Comm.isOpen():
            compassTon = 1 + self.__CompassDirection / 10
            freq = int(1/((compassTon + 65)*1e-3 * self.__FpgaFreq) * (2**32 - 1))
            duty = int(compassTon/(compassTon + 65) * (2**32 - 1))
            self.__CapPwm.setFreq(freq)
            self.__CapPwm.setDuty(duty)
    def __updateWind(self, directionValue, forceValue):
        self.__WindDirection = directionValue
        if forceValue < 0:
            self.__WindForce = 0
        elif forceValue > 250:
            self.__WindForce = 250
        else:
            self.__WindForce = forceValue
        self.ui.WindValueLabel.setText("{0}Km/h {1}°".format(self.__WindForce, self.__WindDirection))
        self.ui.WindWidget.rotate(self.__WindDirection)
        anemoTon = 1 + self.__WindDirection / 10
        #freq = int(1e3/self.__FpgaFreq * 2**32)
        if self.__Comm.isOpen():
            freq = int(1/((anemoTon + 65)*1e-3 * self.__FpgaFreq) * (2**32 - 1))
            duty = int(anemoTon/(anemoTon + 65) * (2**32 - 1))
            self.__AnemoPwm.setFreq(freq)
            self.__AnemoPwm.setDuty(duty)
            duty = int(0.5*(2**32 - 1))
            freq = int(self.__WindForce / self.__FpgaFreq * (2**32 - 1))
            self.__GiroPwm.setDuty(duty)
            self.__GiroPwm.setFreq(freq)
        #self.__AnemoPwm.setDuty(utils.map(self.__WindDirection, 0, 360, (2**32 - 1)*0.1, 2**32 - 1))
        #self.__GiroPwm.setDuty()
    def __updateHydraulic(self, value):
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        if value != self.__HydraulicPos: 
            self.__HydraulicPos = value
            self.ui.BoatWidget.set_pos(self.__HydraulicPos)
            adcValue = int(utils.map(int(self.ui.BoatWidget.get_turningAngle()), -40, 40, 1300, 3000))
            self.ui.HydraulicAngle.setText("{0}° ({1})".format(int(self.ui.BoatWidget.get_turningAngle()), adcValue))
            if self.__Comm.isOpen():
                self.__Comm.writeAt(MainWindow.__VERIN_ANGLE_BASE, 2, adcValue.to_bytes(2, 'little'), True)
    def __sendBtnValue(self, value : int):
        if self.__Comm.isOpen():
            self.__Comm.writeAt(MainWindow.__REG_BASE, 1, value.to_bytes(1, 'little'))
    def __initFPGA(self):
        self.__updateCompass(self.__CompassDirection)
        self.__updateWind(self.__WindDirection, self.__WindForce)
        self.__updateHydraulic(self.__HydraulicPos)