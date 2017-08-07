from abc import ABCMeta, abstractmethod

class piece(metaclass=ABCMeta):
    _players = {'BLANC' : -1, 'NOIR' : 1}
    _color = 0
    _moved = False

    def __init__(self, color):
        self._color = color

    @abstractmethod
    def move(self, pox_x, pos_y, tableau, isPossible):  #pragma: no cover
        raise NotImplementedException()

    @abstractmethod
    def getLetter(self):  #pragma: no cover
        raise NotImplementedException()

    def getColor(self):
        return self._color

    def setMoved(self):
        self._moved=True

    def hasMoved(self):
        return self._moved
