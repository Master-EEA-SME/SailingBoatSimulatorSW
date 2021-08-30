# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from ui.BoatWidget import BoatWidget
from ui.Compass import Compass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(976, 670)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionCOM1 = QAction(MainWindow)
        self.actionCOM1.setObjectName(u"actionCOM1")
        self.action4800 = QAction(MainWindow)
        self.action4800.setObjectName(u"action4800")
        self.action9600 = QAction(MainWindow)
        self.action9600.setObjectName(u"action9600")
        self.action19200 = QAction(MainWindow)
        self.action19200.setObjectName(u"action19200")
        self.action38400 = QAction(MainWindow)
        self.action38400.setObjectName(u"action38400")
        self.action57600 = QAction(MainWindow)
        self.action57600.setObjectName(u"action57600")
        self.action115200 = QAction(MainWindow)
        self.action115200.setObjectName(u"action115200")
        self.action128000 = QAction(MainWindow)
        self.action128000.setObjectName(u"action128000")
        self.action256000 = QAction(MainWindow)
        self.action256000.setObjectName(u"action256000")
        self.action1000000 = QAction(MainWindow)
        self.action1000000.setObjectName(u"action1000000")
        self.action2000000 = QAction(MainWindow)
        self.action2000000.setObjectName(u"action2000000")
        self.action4000000 = QAction(MainWindow)
        self.action4000000.setObjectName(u"action4000000")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CompassGroupBox = QGroupBox(self.centralwidget)
        self.CompassGroupBox.setObjectName(u"CompassGroupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompassGroupBox.sizePolicy().hasHeightForWidth())
        self.CompassGroupBox.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.CompassGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CompassLayout = QVBoxLayout()
        self.CompassLayout.setObjectName(u"CompassLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.CompassWidget = Compass(self.CompassGroupBox)
        self.CompassWidget.setObjectName(u"CompassWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CompassWidget.sizePolicy().hasHeightForWidth())
        self.CompassWidget.setSizePolicy(sizePolicy1)
        self.CompassWidget.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.CompassWidget)


        self.CompassLayout.addLayout(self.horizontalLayout_6)

        self.CompassValueLabel = QLabel(self.CompassGroupBox)
        self.CompassValueLabel.setObjectName(u"CompassValueLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CompassValueLabel.sizePolicy().hasHeightForWidth())
        self.CompassValueLabel.setSizePolicy(sizePolicy2)
        self.CompassValueLabel.setTextFormat(Qt.AutoText)
        self.CompassValueLabel.setAlignment(Qt.AlignCenter)

        self.CompassLayout.addWidget(self.CompassValueLabel)

        self.CompassControlGb = QGroupBox(self.CompassGroupBox)
        self.CompassControlGb.setObjectName(u"CompassControlGb")
        self.verticalLayout_3 = QVBoxLayout(self.CompassControlGb)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.CompassControlButtonsLayout = QHBoxLayout()
        self.CompassControlButtonsLayout.setObjectName(u"CompassControlButtonsLayout")
        self.CompassACWButton = QPushButton(self.CompassControlGb)
        self.CompassACWButton.setObjectName(u"CompassACWButton")

        self.CompassControlButtonsLayout.addWidget(self.CompassACWButton)

        self.CompassCWButton = QPushButton(self.CompassControlGb)
        self.CompassCWButton.setObjectName(u"CompassCWButton")

        self.CompassControlButtonsLayout.addWidget(self.CompassCWButton)


        self.verticalLayout_3.addLayout(self.CompassControlButtonsLayout)


        self.CompassLayout.addWidget(self.CompassControlGb)


        self.verticalLayout.addLayout(self.CompassLayout)


        self.horizontalLayout.addWidget(self.CompassGroupBox)

        self.WindGb = QGroupBox(self.centralwidget)
        self.WindGb.setObjectName(u"WindGb")
        self.verticalLayout_2 = QVBoxLayout(self.WindGb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WindLayout = QVBoxLayout()
        self.WindLayout.setObjectName(u"WindLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.WindWidget = Compass(self.WindGb)
        self.WindWidget.setObjectName(u"WindWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.WindWidget.sizePolicy().hasHeightForWidth())
        self.WindWidget.setSizePolicy(sizePolicy3)
        self.WindWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.WindWidget)


        self.WindLayout.addLayout(self.horizontalLayout_5)

        self.WindValueLabel = QLabel(self.WindGb)
        self.WindValueLabel.setObjectName(u"WindValueLabel")
        self.WindValueLabel.setTextFormat(Qt.AutoText)
        self.WindValueLabel.setAlignment(Qt.AlignCenter)

        self.WindLayout.addWidget(self.WindValueLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.WdGb = QGroupBox(self.WindGb)
        self.WdGb.setObjectName(u"WdGb")
        self.verticalLayout_5 = QVBoxLayout(self.WdGb)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.WdGbLayout = QHBoxLayout()
        self.WdGbLayout.setObjectName(u"WdGbLayout")
        self.WdACWButton = QPushButton(self.WdGb)
        self.WdACWButton.setObjectName(u"WdACWButton")

        self.WdGbLayout.addWidget(self.WdACWButton)

        self.WdCWButton = QPushButton(self.WdGb)
        self.WdCWButton.setObjectName(u"WdCWButton")

        self.WdGbLayout.addWidget(self.WdCWButton)


        self.verticalLayout_5.addLayout(self.WdGbLayout)


        self.horizontalLayout_4.addWidget(self.WdGb)

        self.WfGb = QGroupBox(self.WindGb)
        self.WfGb.setObjectName(u"WfGb")
        self.verticalLayout_6 = QVBoxLayout(self.WfGb)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.WfGbLayout = QHBoxLayout()
        self.WfGbLayout.setObjectName(u"WfGbLayout")
        self.WfDecreaseButton = QPushButton(self.WfGb)
        self.WfDecreaseButton.setObjectName(u"WfDecreaseButton")

        self.WfGbLayout.addWidget(self.WfDecreaseButton)

        self.WfIncreaseButton = QPushButton(self.WfGb)
        self.WfIncreaseButton.setObjectName(u"WfIncreaseButton")

        self.WfGbLayout.addWidget(self.WfIncreaseButton)


        self.verticalLayout_6.addLayout(self.WfGbLayout)


        self.horizontalLayout_4.addWidget(self.WfGb)


        self.WindLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.WindLayout)


        self.horizontalLayout.addWidget(self.WindGb)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.NMEAGb = QGroupBox(self.centralwidget)
        self.NMEAGb.setObjectName(u"NMEAGb")
        self.horizontalLayout_3 = QHBoxLayout(self.NMEAGb)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.NMEALayout = QHBoxLayout()
        self.NMEALayout.setObjectName(u"NMEALayout")
        self.NMEAOutput = QPlainTextEdit(self.NMEAGb)
        self.NMEAOutput.setObjectName(u"NMEAOutput")
        self.NMEAOutput.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.NMEAOutput.setReadOnly(True)

        self.NMEALayout.addWidget(self.NMEAOutput)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.NMEASelect = QComboBox(self.NMEAGb)
        self.NMEASelect.addItem("")
        self.NMEASelect.addItem("")
        self.NMEASelect.addItem("")
        self.NMEASelect.setObjectName(u"NMEASelect")
        self.NMEASelect.setEditable(False)

        self.verticalLayout_10.addWidget(self.NMEASelect, 0, Qt.AlignTop)

        self.NMEAClearButton = QPushButton(self.NMEAGb)
        self.NMEAClearButton.setObjectName(u"NMEAClearButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.NMEAClearButton.sizePolicy().hasHeightForWidth())
        self.NMEAClearButton.setSizePolicy(sizePolicy4)

        self.verticalLayout_10.addWidget(self.NMEAClearButton, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.NMEALayout.addLayout(self.verticalLayout_10)


        self.horizontalLayout_3.addLayout(self.NMEALayout)


        self.verticalLayout_7.addWidget(self.NMEAGb)

        self.HmiGridLayout = QGridLayout()
        self.HmiGridLayout.setObjectName(u"HmiGridLayout")
        self.TribordButton = QPushButton(self.centralwidget)
        self.TribordButton.setObjectName(u"TribordButton")

        self.HmiGridLayout.addWidget(self.TribordButton, 1, 2, 1, 1)

        self.BabordButton = QPushButton(self.centralwidget)
        self.BabordButton.setObjectName(u"BabordButton")

        self.HmiGridLayout.addWidget(self.BabordButton, 1, 0, 1, 1)

        self.StandbyButton = QPushButton(self.centralwidget)
        self.StandbyButton.setObjectName(u"StandbyButton")

        self.HmiGridLayout.addWidget(self.StandbyButton, 1, 1, 1, 1)

        self.LedBabord = QRadioButton(self.centralwidget)
        self.LedBabord.setObjectName(u"LedBabord")
        self.LedBabord.setEnabled(False)
        self.LedBabord.setAutoExclusive(False)

        self.HmiGridLayout.addWidget(self.LedBabord, 0, 0, 1, 1)

        self.LedStandby = QRadioButton(self.centralwidget)
        self.LedStandby.setObjectName(u"LedStandby")
        self.LedStandby.setEnabled(False)
        self.LedStandby.setCheckable(True)
        self.LedStandby.setAutoExclusive(False)

        self.HmiGridLayout.addWidget(self.LedStandby, 0, 1, 1, 1)

        self.LedTribord = QRadioButton(self.centralwidget)
        self.LedTribord.setObjectName(u"LedTribord")
        self.LedTribord.setEnabled(False)
        self.LedTribord.setCheckable(True)
        self.LedTribord.setAutoExclusive(False)

        self.HmiGridLayout.addWidget(self.LedTribord, 0, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.HmiGridLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.BoatGb = QGroupBox(self.centralwidget)
        self.BoatGb.setObjectName(u"BoatGb")
        self.verticalLayout_4 = QVBoxLayout(self.BoatGb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BoatLayout = QVBoxLayout()
        self.BoatLayout.setObjectName(u"BoatLayout")
        self.BoatLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.BoatWidget = BoatWidget(self.BoatGb)
        self.BoatWidget.setObjectName(u"BoatWidget")
        sizePolicy3.setHeightForWidth(self.BoatWidget.sizePolicy().hasHeightForWidth())
        self.BoatWidget.setSizePolicy(sizePolicy3)

        self.BoatLayout.addWidget(self.BoatWidget)

        self.HydraulicAngle = QLabel(self.BoatGb)
        self.HydraulicAngle.setObjectName(u"HydraulicAngle")

        self.BoatLayout.addWidget(self.HydraulicAngle, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.HydraulicManualControl = QRadioButton(self.BoatGb)
        self.HydraulicManualControl.setObjectName(u"HydraulicManualControl")

        self.BoatLayout.addWidget(self.HydraulicManualControl, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.BoatControlGb = QGroupBox(self.BoatGb)
        self.BoatControlGb.setObjectName(u"BoatControlGb")
        self.verticalLayout_9 = QVBoxLayout(self.BoatControlGb)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.CapControl = QHBoxLayout()
        self.CapControl.setSpacing(6)
        self.CapControl.setObjectName(u"CapControl")
        self.CapControl.setSizeConstraint(QLayout.SetNoConstraint)
        self.CapControlMinusButton = QPushButton(self.BoatControlGb)
        self.CapControlMinusButton.setObjectName(u"CapControlMinusButton")

        self.CapControl.addWidget(self.CapControlMinusButton)

        self.CapControlPlusButton = QPushButton(self.BoatControlGb)
        self.CapControlPlusButton.setObjectName(u"CapControlPlusButton")

        self.CapControl.addWidget(self.CapControlPlusButton)


        self.verticalLayout_9.addLayout(self.CapControl)


        self.BoatLayout.addWidget(self.BoatControlGb)

        self.SimulateButton = QPushButton(self.BoatGb)
        self.SimulateButton.setObjectName(u"SimulateButton")

        self.BoatLayout.addWidget(self.SimulateButton)


        self.verticalLayout_4.addLayout(self.BoatLayout)


        self.horizontalLayout_2.addWidget(self.BoatGb)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 976, 22))
        self.menuSerialPort = QMenu(self.menubar)
        self.menuSerialPort.setObjectName(u"menuSerialPort")
        self.menuPort = QMenu(self.menuSerialPort)
        self.menuPort.setObjectName(u"menuPort")
        self.menuBaudRate = QMenu(self.menuSerialPort)
        self.menuBaudRate.setObjectName(u"menuBaudRate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSerialPort.menuAction())
        self.menuSerialPort.addAction(self.menuPort.menuAction())
        self.menuSerialPort.addAction(self.menuBaudRate.menuAction())
        self.menuSerialPort.addAction(self.actionOpen)
        self.menuPort.addAction(self.actionCOM1)
        self.menuBaudRate.addAction(self.action4800)
        self.menuBaudRate.addAction(self.action9600)
        self.menuBaudRate.addAction(self.action19200)
        self.menuBaudRate.addAction(self.action38400)
        self.menuBaudRate.addAction(self.action57600)
        self.menuBaudRate.addAction(self.action115200)
        self.menuBaudRate.addAction(self.action128000)
        self.menuBaudRate.addAction(self.action256000)
        self.menuBaudRate.addAction(self.action1000000)
        self.menuBaudRate.addAction(self.action2000000)
        self.menuBaudRate.addAction(self.action4000000)

        self.retranslateUi(MainWindow)

        self.NMEASelect.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionCOM1.setText(QCoreApplication.translate("MainWindow", u"COM1", None))
        self.action4800.setText(QCoreApplication.translate("MainWindow", u"4800", None))
        self.action9600.setText(QCoreApplication.translate("MainWindow", u"9600", None))
        self.action19200.setText(QCoreApplication.translate("MainWindow", u"19200", None))
        self.action38400.setText(QCoreApplication.translate("MainWindow", u"38400", None))
        self.action57600.setText(QCoreApplication.translate("MainWindow", u"57600", None))
        self.action115200.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.action128000.setText(QCoreApplication.translate("MainWindow", u"128000", None))
        self.action256000.setText(QCoreApplication.translate("MainWindow", u"256000", None))
        self.action1000000.setText(QCoreApplication.translate("MainWindow", u"1000000", None))
        self.action2000000.setText(QCoreApplication.translate("MainWindow", u"2000000", None))
        self.action4000000.setText(QCoreApplication.translate("MainWindow", u"4000000", None))
        self.CompassGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Compass", None))
        self.CompassValueLabel.setText(QCoreApplication.translate("MainWindow", u"250\u00b0", None))
        self.CompassControlGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.CompassACWButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CompassCWButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.WindGb.setTitle(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.WindValueLabel.setText(QCoreApplication.translate("MainWindow", u"10Km/h 90\u00b0 NE", None))
        self.WdGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.WdACWButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.WdCWButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.WfGb.setTitle(QCoreApplication.translate("MainWindow", u"Force", None))
        self.WfDecreaseButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.WfIncreaseButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.NMEAGb.setTitle(QCoreApplication.translate("MainWindow", u"NMEA", None))
        self.NMEAOutput.setPlainText("")
        self.NMEASelect.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.NMEASelect.setItemText(1, QCoreApplication.translate("MainWindow", u"GPGGA", None))
        self.NMEASelect.setItemText(2, QCoreApplication.translate("MainWindow", u"GPRMC", None))

        self.NMEASelect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NMEA", None))
        self.NMEAClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.TribordButton.setText(QCoreApplication.translate("MainWindow", u"Tribord", None))
        self.BabordButton.setText(QCoreApplication.translate("MainWindow", u"Babord", None))
        self.StandbyButton.setText(QCoreApplication.translate("MainWindow", u"Standby", None))
        self.LedBabord.setText(QCoreApplication.translate("MainWindow", u"Led Babord", None))
        self.LedStandby.setText(QCoreApplication.translate("MainWindow", u"Led Standby", None))
        self.LedTribord.setText(QCoreApplication.translate("MainWindow", u"Led Tribord", None))
        self.BoatGb.setTitle(QCoreApplication.translate("MainWindow", u"Boat", None))
        self.HydraulicAngle.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.HydraulicManualControl.setText(QCoreApplication.translate("MainWindow", u"Manual control", None))
        self.BoatControlGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.CapControlMinusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CapControlPlusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.SimulateButton.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
        self.menuSerialPort.setTitle(QCoreApplication.translate("MainWindow", u"Serial Port", None))
        self.menuPort.setTitle(QCoreApplication.translate("MainWindow", u"Port", None))
        self.menuBaudRate.setTitle(QCoreApplication.translate("MainWindow", u"BaudRate", None))
    # retranslateUi

