from PySide6 import QtGui, QtWidgets, QtCore
from PySide6 import QtSvg, QtXml
from ui.SvgModifier import *

class Compass(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super().__init__(parent)
        self.__SvgFile = QtCore.QFile("svg/Compass/Compass.svg")
        self.__SvgFile.open(QtCore.QIODevice.ReadOnly)
        self.__Doc = QtXml.QDomDocument()
        self.__Doc.setContent(self.__SvgFile)
        self.__NeedleElem = SvgModifier.getElementbyId("Needle", self.__Doc.childNodes())
        rotPointElem = self.__NeedleElem.childNodes().at(2).toElement() 
        self.__NeedleRot = SvgRotation(r=0, x=float(rotPointElem.attribute("cx")), y=float(rotPointElem.attribute("cy")))
        self.rot = 0

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        rect = self.__getBoudingRect()
        self.__NeedleRot.rotate(self.rot + 45)
        self.__NeedleElem.setAttribute("transform", str(self.__NeedleRot))
        render = QtSvg.QSvgRenderer(self.__Doc.toByteArray())
        render.render(painter, self.__getBoudingRect())

    def __getBoudingRect(self) -> QtCore.QRect:
        res = min(self.width(), self.height())
        x = (self.width() - res) / 2
        y = (self.height() - res) / 2
        rect = QtCore.QRect(x, y, res, res)
        return rect
        
    def rotate(self, rot : float):
        self.rot = rot
        self.update()

#app = QtWidgets.QApplication()
#widget = Compass()
#widget.show()
#app.exec()