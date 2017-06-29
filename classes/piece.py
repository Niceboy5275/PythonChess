class piece(object):
    _players = {'BLANC' : -1, 'NOIR' : 1}
    _color = 0

    def __init__(self, color):
        self._color = color

    def move(self, pox_x, pos_y, tableau, isPossible):
        raise NotImplementedException()

    def getLetter(self):
        raise NotImplementedException()

    def getColor(self):
        return self._color

    def getImage():
        raise NotImplementedException()
