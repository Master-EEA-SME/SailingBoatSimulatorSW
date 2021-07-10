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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 9, 620, 502))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CompassGroupBox = QGroupBox(self.horizontalLayoutWidget_2)
        self.CompassGroupBox.setObjectName(u"CompassGroupBox")
        self.verticalLayout = QVBoxLayout(self.CompassGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CompassLayout = QVBoxLayout()
        self.CompassLayout.setObjectName(u"CompassLayout")
        self.CompassNorthLabel = QLabel(self.CompassGroupBox)
        self.CompassNorthLabel.setObjectName(u"CompassNorthLabel")
        self.CompassNorthLabel.setLayoutDirection(Qt.LeftToRight)
        self.CompassNorthLabel.setAlignment(Qt.AlignCenter)

        self.CompassLayout.addWidget(self.CompassNorthLabel)

        self.CompassSubLayout1 = QHBoxLayout()
        self.CompassSubLayout1.setObjectName(u"CompassSubLayout1")
        self.CompassWestLabel = QLabel(self.CompassGroupBox)
        self.CompassWestLabel.setObjectName(u"CompassWestLabel")

        self.CompassSubLayout1.addWidget(self.CompassWestLabel)

        self.CompassWidget = QWidget(self.CompassGroupBox)
        self.CompassWidget.setObjectName(u"CompassWidget")

        self.CompassSubLayout1.addWidget(self.CompassWidget)

        self.CompassEastLabel = QLabel(self.CompassGroupBox)
        self.CompassEastLabel.setObjectName(u"CompassEastLabel")
        self.CompassEastLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.CompassSubLayout1.addWidget(self.CompassEastLabel)


        self.CompassLayout.addLayout(self.CompassSubLayout1)

        self.CompassSouthLabel = QLabel(self.CompassGroupBox)
        self.CompassSouthLabel.setObjectName(u"CompassSouthLabel")
        self.CompassSouthLabel.setAlignment(Qt.AlignCenter)

        self.CompassLayout.addWidget(self.CompassSouthLabel)

        self.CompassValueLabel = QLabel(self.CompassGroupBox)
        self.CompassValueLabel.setObjectName(u"CompassValueLabel")
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

        self.WindGb = QGroupBox(self.horizontalLayoutWidget_2)
        self.WindGb.setObjectName(u"WindGb")
        self.verticalLayout_2 = QVBoxLayout(self.WindGb)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WindLayout = QVBoxLayout()
        self.WindLayout.setObjectName(u"WindLayout")
        self.WindNorthLabel = QLabel(self.WindGb)
        self.WindNorthLabel.setObjectName(u"WindNorthLabel")
        self.WindNorthLabel.setLayoutDirection(Qt.LeftToRight)
        self.WindNorthLabel.setAlignment(Qt.AlignCenter)

        self.WindLayout.addWidget(self.WindNorthLabel)

        self.WindSubLayout1 = QHBoxLayout()
        self.WindSubLayout1.setObjectName(u"WindSubLayout1")
        self.WindWestLabel = QLabel(self.WindGb)
        self.WindWestLabel.setObjectName(u"WindWestLabel")

        self.WindSubLayout1.addWidget(self.WindWestLabel)

        self.WindWidget = QWidget(self.WindGb)
        self.WindWidget.setObjectName(u"WindWidget")

        self.WindSubLayout1.addWidget(self.WindWidget)

        self.WindEastLabel = QLabel(self.WindGb)
        self.WindEastLabel.setObjectName(u"WindEastLabel")
        self.WindEastLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.WindSubLayout1.addWidget(self.WindEastLabel)


        self.WindLayout.addLayout(self.WindSubLayout1)

        self.WindSouthLabel = QLabel(self.WindGb)
        self.WindSouthLabel.setObjectName(u"WindSouthLabel")
        self.WindSouthLabel.setAlignment(Qt.AlignCenter)

        self.WindLayout.addWidget(self.WindSouthLabel)

        self.WindValueLabel = QLabel(self.WindGb)
        self.WindValueLabel.setObjectName(u"WindValueLabel")
        self.WindValueLabel.setTextFormat(Qt.AutoText)
        self.WindValueLabel.setAlignment(Qt.AlignCenter)

        self.WindLayout.addWidget(self.WindValueLabel)

        self.WindControlLayout = QVBoxLayout()
        self.WindControlLayout.setObjectName(u"WindControlLayout")
        self.WfGb = QGroupBox(self.WindGb)
        self.WfGb.setObjectName(u"WfGb")
        self.verticalLayout_6 = QVBoxLayout(self.WfGb)
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


        self.WindControlLayout.addWidget(self.WfGb)

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


        self.WindControlLayout.addWidget(self.WdGb)


        self.WindLayout.addLayout(self.WindControlLayout)


        self.verticalLayout_2.addLayout(self.WindLayout)


        self.horizontalLayout.addWidget(self.WindGb)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.NMEAGb = QGroupBox(self.horizontalLayoutWidget_2)
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
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NMEAClearButton.sizePolicy().hasHeightForWidth())
        self.NMEAClearButton.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.NMEAClearButton, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.NMEALayout.addLayout(self.verticalLayout_10)


        self.horizontalLayout_3.addLayout(self.NMEALayout)


        self.verticalLayout_7.addWidget(self.NMEAGb)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.BoatGb = QGroupBox(self.horizontalLayoutWidget_2)
        self.BoatGb.setObjectName(u"BoatGb")
        self.verticalLayout_4 = QVBoxLayout(self.BoatGb)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BoatLayout = QVBoxLayout()
        self.BoatLayout.setObjectName(u"BoatLayout")
        self.BoatLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.BoatWidget = BoatWidget(self.BoatGb)
        self.BoatWidget.setObjectName(u"BoatWidget")

        self.BoatLayout.addWidget(self.BoatWidget)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.NMEASelect.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.CompassGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Compass", None))
        self.CompassNorthLabel.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.CompassWestLabel.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.CompassEastLabel.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.CompassSouthLabel.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.CompassValueLabel.setText(QCoreApplication.translate("MainWindow", u"250\u00b0", None))
        self.CompassControlGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.CompassACWButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CompassCWButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.WindGb.setTitle(QCoreApplication.translate("MainWindow", u"Wind", None))
        self.WindNorthLabel.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.WindWestLabel.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.WindEastLabel.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.WindSouthLabel.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.WindValueLabel.setText(QCoreApplication.translate("MainWindow", u"10Km/h 90\u00b0 NE", None))
        self.WfGb.setTitle(QCoreApplication.translate("MainWindow", u"Force", None))
        self.WfDecreaseButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.WfIncreaseButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.WdGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.WdACWButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.WdCWButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.NMEAGb.setTitle(QCoreApplication.translate("MainWindow", u"NMEA", None))
        self.NMEAOutput.setPlainText("")
        self.NMEASelect.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.NMEASelect.setItemText(1, QCoreApplication.translate("MainWindow", u"GPGGA", None))
        self.NMEASelect.setItemText(2, QCoreApplication.translate("MainWindow", u"GPRMC", None))

        self.NMEASelect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NMEA", None))
        self.NMEAClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.BoatGb.setTitle(QCoreApplication.translate("MainWindow", u"Boat", None))
        self.BoatControlGb.setTitle(QCoreApplication.translate("MainWindow", u"Direction", None))
        self.CapControlMinusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.CapControlPlusButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.SimulateButton.setText(QCoreApplication.translate("MainWindow", u"Simulate", None))
    # retranslateUi

