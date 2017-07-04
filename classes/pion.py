from piece import piece

class pion(piece):

    _takeableLeft = False
    _takeableRight = False

    def setTakeableLeft(self, val):
        self._takeableLeft = val

    def setTakeableRight(self, val):
        self._takeableRight = val

    def move(self, pos_x, pos_y, tableau, possible):
        if (self.getColor() == piece._players['NOIR']):
            if tableau.getPion(pos_x, pos_y + 1) == None:
                tableau.setPossible(pos_x, pos_y + 1, piece._players['NOIR'], possible)
                if pos_y == 1:
                    if tableau.getPion(pos_x, pos_y + 2) == None:
                        tableau.setPossible(pos_x, pos_y + 2, 1, possible)
            if tableau.getPion(pos_x-1, pos_y + 1) != None and tableau.getPion(pos_x-1, pos_y + 1).getColor() < 0:
                tableau.setPossible(pos_x-1, pos_y + 1, 0, possible)
            if tableau.getPion(pos_x+1, pos_y + 1) != None and tableau.getPion(pos_x+1, pos_y + 1).getColor() < 0:
                tableau.setPossible(pos_x+1, pos_y + 1, 0, possible)
            if (self._takeableLeft):
                tableau.setPossible(pos_x+1, pos_y + 1, 0, possible)
            if (self._takeableRight):
                tableau.setPossible(pos_x-1, pos_y + 1, 0, possible)
        if (self.getColor() == piece._players['BLANC']):
            if tableau.getPion(pos_x, pos_y - 1) == None:
                tableau.setPossible(pos_x, pos_y - 1, -1, possible)
                if pos_y == 6:
                    if tableau.getPion(pos_x, pos_y - 2) == None:
                        tableau.setPossible(pos_x, pos_y - 2, piece._players['BLANC'], possible)
            if tableau.getPion(pos_x-1, pos_y - 1) != None and tableau.getPion(pos_x-1, pos_y - 1).getColor() > 0:
                tableau.setPossible(pos_x-1, pos_y - 1, 0, possible)
            if tableau.getPion(pos_x+1, pos_y - 1) != None and tableau.getPion(pos_x+1, pos_y - 1).getColor() > 0:
                tableau.setPossible(pos_x+1, pos_y - 1, 0, possible)
            if (self._takeableLeft):
                tableau.setPossible(pos_x+1, pos_y - 1, 0, possible)
            if (self._takeableRight):
                tableau.setPossible(pos_x-1, pos_y - 1, 0, possible)

    def getLetter(self):
        return "P"
