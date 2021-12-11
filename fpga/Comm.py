from serial import Serial
import logging
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

    def writeAt(self, address : int, xlen : int, data : list, incr : bool = False) -> bool:
        ret = False
        if xlen != 0:
            self.__sendCmd(False, incr, address, xlen)
            self.__Serial.write(data)
            ret = self.__getAck()
        if ret:
            #logging.info("Write at {0:02X} {1} [{2:02X}] incr={3}".format(address, xlen, data, incr))
            #logging.info("Write at {0:02X} {1} [{2:02X}] incr={3}".format(address, xlen, data, incr))
            logging.info("Write at {0:02X} {1} [{2}] incr={3}".format(address, xlen, " ".join("{:02X}".format(x) for x in data), incr))
        else:
            logging.warning("Could not write at {0:02X}".format(address))
        return ret

    def readAt(self, address : int, xlen : int, incr : bool = False) -> list:
        ret = []
        if xlen != 0:
            self.__sendCmd(True, incr, address, xlen)
            rxDat = self.__Serial.read(xlen + 2)
            if self.__parseData(rxDat, xlen, False):
                ret = list(rxDat[2:])
                logging.info("Read at {0:02X} {1} [{2}] incr={3}".format(address, xlen, " ".join("{:02X}".format(x) for x in ret), incr))
            else:
                logging.warning("Could not read at {0:02X}".format(address))
        return ret
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
    