from PySide6 import QtXml


class SvgModifier():
    def changeRect(elem: QtXml.QDomElement, x, y, w, h):
        if elem.tagName() != "rect":
            return
        elem.setAttribute("x", str(x))
        elem.setAttribute("y", str(y))
        elem.setAttribute("width", str(w))
        elem.setAttribute("height", str(h))
    
    def moveRect(elem: QtXml.QDomElement, x, y):
        pass
    def resizeRect(elem: QtXml.QDomElement, w = None, h = None):
        if w != None:
            elem.setAttribute("width", str(w))
        if h != None:
            elem.setAttribute("height", str(h))

    def changeEllipse(node: QtXml.QDomNode, cx, cy, rx, ry):
        if node.nodeName() != "ellipse":
            return
        attributes = node.attributes()
        for i in range(attributes.size()):
            attr = attributes.item(i)
            if attr.nodeName() == "cx":
                attr.setNodeValue(str(cx))
                attributes.setNamedItem(attr)
            elif attr.nodeName() == "cy":
                attr.setNodeValue(str(cy))
                attributes.setNamedItem(attr)
            elif attr.nodeName() == "rx":
                attr.setNodeValue(str(rx))
                attributes.setNamedItem(attr)
            elif attr.nodeName() == "ry":
                attr.setNodeValue(str(ry))
                attributes.setNamedItem(attr)
    def moveEllipse(elem: QtXml.QDomElement, xoff = None, yoff = None):
        if xoff != None:
            cx = float(elem.attribute("cx"))
            cx += xoff
            elem.setAttribute("cx", str(cx))
        if yoff != None:
            cy = float(elem.attribute("cy"))
            cy += yoff
            elem.setAttribute("cy", str(cy))
            
    def getElementbyId(id : str, nodes : QtXml.QDomNamedNodeMap) -> QtXml.QDomElement:
        for i in range(nodes.size()):
            elem = nodes.item(i).toElement()
            if elem.hasAttribute("id") and elem.attribute("id") == id:
                return elem
            elif elem.hasChildNodes():
                ret = SvgModifier.getElementbyId(id, elem.childNodes())
                if ret != None:
                    return ret
        return None

class SvgRotation():
    def __init__(self, args : str = None, r = None, x = None, y = None) -> None:
        if args != None:
            vargs = args.split(",")
            self.__r = float(vargs[0])
            if len(vargs) > 1:
                self.__x = float(vargs[1])
                self.__y = float(vargs[2])
        else:
            self.__r = r
            self.__x = x
            self.__y = y
            
    def rotate(self, r):
        self.__r = r
    def setPosX(self, x):
        self.__x = x
    def setPosY(self, y):
        self.__y = y
    def setPos(self, x, y):
        self.setPosX(x)
        self.setPosY(y)
    def __str__(self) -> str:
        if self.__x == None or self.__y == None:
            return "rotate({0})".format(self.__r)
        else:
            return "rotate({0},{1},{2})".format(self.__r, self.__x, self.__y)
class SvgTranslate():
    def __init__(self, args : str = None, x = None, y = None) -> None:
        if args != None:
            vargs = args.split(",")
            self.__x = float(vargs[0])
            self.__y = float(vargs[1])
        else:
            self.__x = x
            self.__y = y

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
    def translate(self, x, y):
        self.__x = x
        self.__y = y
    def x(self):
        return self.__x
    def y(self):
        return self.__y
    def __str__(self) -> str:
        return "translate({0},{1})".format(self.__x, self.__y)
class SvgTransform():
    def __init__(self, transformStr : str) -> None:
        transformStrArr = transformStr.split()
        self.transformFunList = []
        for transFun in transformStrArr:
            transFunName = transFun.split("(")
            if transFunName[0] == "rotate":
                self.transformFunList.append(SvgRotation(args=transFunName[1][0:-1]))
            elif transFunName[0] == "translate":
                self.transformFunList.append(SvgTranslate(args=transFunName[1][0:-1]))
    def __str__(self) -> str:
        ret = str()
        for transformFun in self.transformFunList:
            ret += str(transformFun) + " "
        return ret
    def __getitem__(self, index) -> list:
        return self.transformFunList[index]
    def append(self, fun):
        if isinstance(fun, SvgRotation) or isinstance(fun, SvgTranslate):
            self.transformFunList.append(fun)