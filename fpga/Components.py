from fpga.Comm import Comm
class Component():
    __LENINDEX = 0
    __DATAINDEX = 1
    def __init__(self, base : int, Comm : Comm) -> None:
        self._base = base
        self._Comm = Comm

class Pwm(Component):
    def __init__(self, Comm : Comm, base : int, byteSize : int = 2) -> None:
        super().__init__(base, Comm)
        self.__byteSize = byteSize
    
    def getDuty(self) -> int:
        return int.from_bytes(self._Comm.readAt(self._base, self.__byteSize, True), 'little')        
    
    def setDuty(self, duty : int):
        self._Comm.writeAt(self._base, self.__byteSize, duty.to_bytes(self.__byteSize, 'little'), True)
    
    def getFreq(self) -> int:
        return int.from_bytes(self._Comm.readAt(self._base + self.__byteSize, self.__byteSize, True), 'little')
    
    def setFreq(self, freq : int):
        self._Comm.writeAt(self._base + self.__byteSize, self.__byteSize, freq.to_bytes(self.__byteSize, 'little'), True)
