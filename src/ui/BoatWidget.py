from PyQt6 import QtWidgets, QtGui, QtCore

class BoatWidget(QtWidgets.QWidget):
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.green, 8, QtCore.Qt.PenStyle.DashLine))
        painter.drawEllipse(0, 0, self.width(), self.height())
        return super().paintEvent(a0)