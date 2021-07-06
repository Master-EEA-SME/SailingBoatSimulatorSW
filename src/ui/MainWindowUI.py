# Form implementation generated from reading ui file '.\src\ui\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(480, 40, 211, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.BoatLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.BoatLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.BoatLayout.setContentsMargins(0, 0, 0, 0)
        self.BoatLayout.setObjectName("BoatLayout")
        self.BoatWidget = BoatWidget(self.verticalLayoutWidget_2)
        self.BoatWidget.setObjectName("BoatWidget")
        self.BoatLayout.addWidget(self.BoatWidget)
        self.CapControl = QtWidgets.QHBoxLayout()
        self.CapControl.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.CapControl.setSpacing(6)
        self.CapControl.setObjectName("CapControl")
        self.CapControlMinusButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.CapControlMinusButton.setObjectName("CapControlMinusButton")
        self.CapControl.addWidget(self.CapControlMinusButton)
        self.CapControlPlusButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.CapControlPlusButton.setObjectName("CapControlPlusButton")
        self.CapControl.addWidget(self.CapControlPlusButton)
        self.BoatLayout.addLayout(self.CapControl)
        self.SimulateButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.SimulateButton.setObjectName("SimulateButton")
        self.BoatLayout.addWidget(self.SimulateButton)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 210, 251, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.CompassLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.CompassLayout.setContentsMargins(0, 0, 0, 0)
        self.CompassLayout.setObjectName("CompassLayout")
        self.NorthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.NorthLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.NorthLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.NorthLabel.setObjectName("NorthLabel")
        self.CompassLayout.addWidget(self.NorthLabel)
        self.CompassSubLayout1 = QtWidgets.QHBoxLayout()
        self.CompassSubLayout1.setObjectName("CompassSubLayout1")
        self.WestLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.WestLabel.setObjectName("WestLabel")
        self.CompassSubLayout1.addWidget(self.WestLabel)
        self.CompassWidget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.CompassWidget.setObjectName("CompassWidget")
        self.CompassSubLayout1.addWidget(self.CompassWidget)
        self.EastLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.EastLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.EastLabel.setObjectName("EastLabel")
        self.CompassSubLayout1.addWidget(self.EastLabel)
        self.CompassLayout.addLayout(self.CompassSubLayout1)
        self.SouthLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.SouthLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.SouthLabel.setObjectName("SouthLabel")
        self.CompassLayout.addWidget(self.SouthLabel)
        self.CompassValueLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.CompassValueLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.CompassValueLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.CompassValueLabel.setObjectName("CompassValueLabel")
        self.CompassLayout.addWidget(self.CompassValueLabel)
        self.CompassSubLayout2 = QtWidgets.QHBoxLayout()
        self.CompassSubLayout2.setObjectName("CompassSubLayout2")
        self.CompassTurnLeftButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CompassTurnLeftButton.setObjectName("CompassTurnLeftButton")
        self.CompassSubLayout2.addWidget(self.CompassTurnLeftButton)
        self.CompassTurnRightButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.CompassTurnRightButton.setObjectName("CompassTurnRightButton")
        self.CompassSubLayout2.addWidget(self.CompassTurnRightButton)
        self.CompassLayout.addLayout(self.CompassSubLayout2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CapControlMinusButton.setText(_translate("MainWindow", "-"))
        self.CapControlPlusButton.setText(_translate("MainWindow", "+"))
        self.SimulateButton.setText(_translate("MainWindow", "Simulate"))
        self.NorthLabel.setText(_translate("MainWindow", "N"))
        self.WestLabel.setText(_translate("MainWindow", "W"))
        self.EastLabel.setText(_translate("MainWindow", "E"))
        self.SouthLabel.setText(_translate("MainWindow", "S"))
        self.CompassValueLabel.setText(_translate("MainWindow", "250°"))
        self.CompassTurnLeftButton.setText(_translate("MainWindow", "-"))
        self.CompassTurnRightButton.setText(_translate("MainWindow", "+"))
from ui.BoatWidget import BoatWidget