from PySide6 import QtGui, QtWidgets, QtSvg, QtCore

class Compass(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        self.resize(600, 600)
        #self.heightForWidth()
        self.__base = QtSvg.QSvgRenderer("svg/Compass/base.svg")
        self.__needle = QtSvg.QSvgRenderer("svg/Compass/needle.svg")
        self.rot = 0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        rect = self.__getBoudingRect()
        #rect = painter.boundingRect(0, 0, self.width(), self.height(), QtGui.Qt.AlignHCenter | QtGui.Qt.AlignVCenter, "Helllsqdqsdqs")
        self.__base.render(painter, rect)
        painter.translate((self.width() / 2), (self.height() / 2))
        painter.rotate(self.rot + 45)
        painter.translate(-(self.width() / 2), -(self.height() / 2))
        self.__needle.render(painter, rect)

    def __getBoudingRect(self) -> QtCore.QRect:
        res = min(self.width(), self.height())
        x = (self.width() - res) / 2
        y = (self.height() - res) / 2
        rect = QtCore.QRect(x, y, res, res)
        return rect
        
    def rotate(self, rot : float):
        self.rot = rot
        self.update()

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        pass
        #print(self.objectName(), end=' ')
        #print(self.width(), end='x')
        #print(self.height())
        #self.resize(100, 100)
        #self.update()

#app = QtWidgets.QApplication()
#widget = Compass()
#widget.show()
#app.exec()