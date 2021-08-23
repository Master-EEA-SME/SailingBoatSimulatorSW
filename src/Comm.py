from serial import Serial

class Comm():
    __STARTCODE = 0x55
    def __init__(self) -> None:
        self.__Serial = Serial()
    def setConfig(self, port : str = None, baud : int = None):
        if port != None:
            self.__Serial.port = port
        if baud != None:
            self.__Serial.baudrate = baud
        self.__Serial.bytesize = 8
        self.__Serial.timeout = 1
    def isOpen(self):
        return self.__Serial.is_open
    def open(self):
        self.__Serial.open()
    def close(self):
        self.__Serial.close()
    def __sendCmd(self, rw : bool, incr : bool, address : int, len : int):
        if len != 0:
            len -= 1
            cmd = 0x1 if rw == True else 0x00
            if incr == True: cmd |= 0x80
            self.__Serial.write([Comm.__STARTCODE, cmd, address, len])
    def __getAck(self) -> bool:
        ack = self.__Serial.read(3)
        return self.__parseData(ack, 1, True)

    def writeAt(self, address : int, len : int, data : list, incr : bool = False) -> bool:
        if len != 0:
            self.__sendCmd(False, incr, address, len)
            self.__Serial.write(data)
            return self.__getAck()
        return False

    def readAt(self, address : int, xlen : int, incr : bool = False) -> list:
        if xlen != 0:
            self.__sendCmd(True, incr, address, xlen)
            rxDat = self.__Serial.read(xlen + 2)
            if self.__parseData(rxDat, xlen, False):
                return list(rxDat[2:])
            else:
                return None
#            print(len(rxDat))
#            for i in range(0, len(rxDat) - 1, 16):
#                print("0x{0:02X}".format(i), end='')
#                for j in range(16):
#                    if i + j >= len(rxDat):
#                        break
#                    print(" {0:02X}".format(rxDat[i + j]), end='')
#                print()
    @staticmethod
    def __parseData(buf, expectedLen, isAck) -> bool:
        expectedLen -= 1
        for i in range(len(buf)):
            if i == 0:
                if buf[i] != Comm.__STARTCODE:
                    return False
            elif i == 1:
                if buf[i] != expectedLen:
                    return False
            elif i == 2 and isAck:
                if buf[i] != 1:
                    return False
        return True
    def getPort(self) -> str:
        return self.__Serial.port
    