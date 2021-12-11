from typing import Tuple
from PySide6 import QtWidgets, QtGui, QtCore, QtSvg, QtXml
from ui.SvgModifier import *
import math
def get_intersections(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1
    d=math.sqrt((x1-x0)**2 + (y1-y0)**2)
    
    # non intersecting
    if d > r0 + r1 :
        return None
    # One circle within other
    if d < abs(r0-r1):
        return None
    # coincident circles
    if d == 0 and r0 == r1:
        return None
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=math.sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d   
        y2=y0+a*(y1-y0)/d   
        x3=x2+h*(y1-y0)/d     
        y3=y2-h*(x1-x0)/d 

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        return (x3, y3, x4, y4)
class BoatWidget(QtWidgets.QWidget):
    def __init__(self, parent : QtWidgets.QWidget = None) -> None:
        super().__init__(parent=parent)
        self.__HydraulicPos = 50
        self.__SvgFile = QtCore.QFile("svg/Hydraulic/Hydraulic.svg")
        self.__SvgFile.open(QtCore.QIODevice.ReadOnly)
        self.__Doc = QtXml.QDomDocument()
        self.__Doc.setContent(self.__SvgFile)
        self.__RudderAnchorElem = SvgModifier.getElementbyId("RudderAnchor", self.__Doc.childNodes())
        self.__RudderRot = SvgRotation(r=0, x=float(self.__RudderAnchorElem.attribute("cx")), y=float(self.__RudderAnchorElem.attribute("cy")))
        self.__RudderPart = SvgModifier.getElementbyId("RubberPart", self.__Doc.childNodes())
        self.__HydraulicAnchorElem = SvgModifier.getElementbyId("HydraulicAnchor", self.__Doc.childNodes())
        self.__HydraulicRot = SvgRotation(r=0, x=float(self.__HydraulicAnchorElem.attribute("cx")), y=float(self.__HydraulicAnchorElem.attribute("cy")))
        self.__HydraulicPart = SvgModifier.getElementbyId("HydraulicPart", self.__Doc.childNodes())
        self.__HydraulicArmElem = SvgModifier.getElementbyId("HydraulicArm", self.__Doc.childNodes())
        self.__HydraulicArmConnectorElem = SvgModifier.getElementbyId("HydraulicConnector", self.__Doc.childNodes())
        self.__HydraulicArmConnectorTrans = SvgTranslate(x=0, y=0)
        self.__HydraulicArmLenght = float(self.__HydraulicArmElem.attribute("width"))*2
        self.__HydraulicArmConnectorPoint = QtCore.QPointF(float(self.__HydraulicArmConnectorElem.childNodes().at(0).toElement().attribute("cx")), float(self.__HydraulicArmConnectorElem.childNodes().at(0).toElement().attribute("cy")))
        self.__RudderAnchorPoint = QtCore.QPointF(float(self.__RudderAnchorElem.attribute("cx")), float(self.__RudderAnchorElem.attribute("cy")))
        self.__HydraulicAnchorPoint = QtCore.QPointF(float(self.__HydraulicAnchorElem.attribute("cx")), float(self.__HydraulicAnchorElem.attribute("cy")))

    def insert(self):
        if (self.__HydraulicPos > 0):
            self.__HydraulicPos -= 10
            self.update()
    def extract(self):
        if (self.__HydraulicPos < 100):
            self.__HydraulicPos += 10
            self.update()
    def __getBoudingRect(self, renderSize : QtCore.QSize) -> QtCore.QRect:
        ratio = renderSize.width() / renderSize.height()
        if self.width() < self.height()*ratio:
            height = self.width()/ratio
            width = self.width()
        else:
            height = self.height()
            width = self.height()*ratio
        x = (self.width() - width) / 2
        y = (self.height() - height) / 2
        rect = QtCore.QRect(x, y, width, height)
        return rect
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QtGui.QPainter(self)
        #HydraulicArmConnectorCurrentPos = QtCore.QPointF()
        #self.__HydraulicArmConnectorTrans.translate(self.__HydraulicArmLenght*self.__HydraulicPos/100 - self.__HydraulicArmLenght / 2, 0)
        #HydraulicArmConnectorCurrentPos.setX(self.__HydraulicArmConnectorPoint.x() + self.__HydraulicArmConnectorTrans.x())
        #inter = get_intersections(
        #    self.__HydraulicAnchorPoint.x(), self.__HydraulicAnchorPoint.y(), abs(HydraulicArmConnectorCurrentPos.x() - self.__HydraulicAnchorPoint.x()), 
        #    self.__RudderAnchorPoint.x(), self.__RudderAnchorPoint.y(), abs(self.__HydraulicArmConnectorPoint.y() - self.__RudderAnchorPoint.y()))
        #l = [abs(HydraulicArmConnectorCurrentPos.x() - self.__HydraulicAnchorPoint.x()), abs(self.__HydraulicArmConnectorPoint.y() - self.__RudderAnchorPoint.y())]
        #alpha = [
        #    math.acos((inter[2] - self.__HydraulicAnchorPoint.x())/l[0]), 
        #    math.asin((self.__RudderAnchorPoint.x() - inter[2])/l[1])]
        #alpha[0] *= 180.0/math.pi
        #alpha[1] *= 180.0/math.pi
        #self.__turningAngle = alpha[1]
        #print("alpha[0] = {0}".format(alpha[0]))
        #print("alpha[1] = {0}".format(alpha[1]))

        #self.__HydraulicRot.rotate(-self.__HydraulicAngle)
        self.__HydraulicPart.setAttribute("transform", str(self.__HydraulicRot))
        #self.__RudderRot.rotate(self.__RudderAngle)
        self.__RudderPart.setAttribute("transform", str(self.__RudderRot))
        self.__HydraulicArmConnectorElem.setAttribute("transform", str(self.__HydraulicArmConnectorTrans))
        self.__HydraulicArmElem.setAttribute("width", str(self.__HydraulicArmLenght*self.__HydraulicPos/100))
        render = QtSvg.QSvgRenderer(self.__Doc.toByteArray())
        render.render(painter, self.__getBoudingRect(render.defaultSize()))
        #painter.drawEllipse(self.__HydraulicAnchorPoint, abs(HydraulicArmConnectorCurrentPos.x() - self.__HydraulicAnchorPoint.x()), abs(HydraulicArmConnectorCurrentPos.x() - self.__HydraulicAnchorPoint.x()))
        #painter.drawEllipse(self.__RudderAnchorPoint, abs(self.__HydraulicArmConnectorPoint.y() - self.__RudderAnchorPoint.y()), abs(self.__HydraulicArmConnectorPoint.y() - self.__RudderAnchorPoint.y()))
        #if inter != None:
        #    painter.drawEllipse(QtCore.QPointF(inter[0], inter[1]), 10, 10)
        #    painter.drawEllipse(QtCore.QPointF(inter[2], inter[3]), 10, 10)
    def get_turningAngle(self):
        return -self.__RudderRot.get_rotation()
    def set_pos(self, pos):
        if pos < 0:
            pos = 0
        elif pos > 100:
            pos = 100
        self.__HydraulicPos = pos
        self.__setAngles()
        self.update()
    def __setAngles(self):
        HydraulicArmConnectorCurrentPos = QtCore.QPointF()
        self.__HydraulicArmConnectorTrans.translate(self.__HydraulicArmLenght*self.__HydraulicPos/100 - self.__HydraulicArmLenght / 2, 0)
        HydraulicArmConnectorCurrentPos.setX(self.__HydraulicArmConnectorPoint.x() + self.__HydraulicArmConnectorTrans.x())
        l = [abs(HydraulicArmConnectorCurrentPos.x() - self.__HydraulicAnchorPoint.x()), abs(self.__HydraulicArmConnectorPoint.y() - self.__RudderAnchorPoint.y())]
        inter = get_intersections(
            self.__HydraulicAnchorPoint.x(), self.__HydraulicAnchorPoint.y(), l[0], 
            self.__RudderAnchorPoint.x(), self.__RudderAnchorPoint.y(), l[1])
        alpha = [
            math.acos((inter[2] - self.__HydraulicAnchorPoint.x())/l[0]), 
            math.asin((self.__RudderAnchorPoint.x() - inter[2])/l[1])]
        alpha[0] *= 180.0/math.pi
        alpha[1] *= 180.0/math.pi
        self.__HydraulicRot.rotate(-alpha[0])
        self.__RudderRot.rotate(alpha[1])
