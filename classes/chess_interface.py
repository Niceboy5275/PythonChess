from abc import ABCMeta, abstractmethod

class chessInterface(metaclass=ABCMeta):

    @abstractmethod
    def showMessage(self, message): #pragma: no cover
        pass

    @abstractmethod
    def clearMessage(self, message): #pragma: no cover
        pass

    @abstractmethod
    def draw(self): #pragma: no cover
        pass

    @abstractmethod
    def showPromotion(self): #pragma: no cover
        pass

    @abstractmethod
    def mainLoop(self): #pragma: no cover
        pass
