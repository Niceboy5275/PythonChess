from piece import piece
from pion import pion
from fou import fou
from tour import tour
from cavalier import cavalier
from roi import roi
from reine import reine

class tableau():
    _tableau = [ [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None] ]

    def __init__(self):
        self.reset()

    def reset(self):
        for X in range(0, 8):
            for Y in range(2, 6):
                self._tableau[X][Y]=None
        self._tableau[0][0]=tour(piece._players['NOIR'])
        self._tableau[1][0]=cavalier(piece._players['NOIR'])
        self._tableau[2][0]=fou(piece._players['NOIR'])
        self._tableau[3][0]=reine(piece._players['NOIR'])
        self._tableau[4][0]=roi(piece._players['NOIR'])
        self._tableau[5][0]=fou(piece._players['NOIR'])
        self._tableau[6][0]=cavalier(piece._players['NOIR'])
        self._tableau[7][0]=tour(piece._players['NOIR'])

        self._tableau[0][1]=pion(piece._players['NOIR'])
        self._tableau[1][1]=pion(piece._players['NOIR'])
        self._tableau[2][1]=pion(piece._players['NOIR'])
        self._tableau[3][1]=pion(piece._players['NOIR'])
        self._tableau[4][1]=pion(piece._players['NOIR'])
        self._tableau[5][1]=pion(piece._players['NOIR'])
        self._tableau[6][1]=pion(piece._players['NOIR'])
        self._tableau[7][1]=pion(piece._players['NOIR'])

        self._tableau[0][6]=pion(piece._players['BLANC'])
        self._tableau[1][6]=pion(piece._players['BLANC'])
        self._tableau[2][6]=pion(piece._players['BLANC'])
        self._tableau[3][6]=pion(piece._players['BLANC'])
        self._tableau[4][6]=pion(piece._players['BLANC'])
        self._tableau[5][6]=pion(piece._players['BLANC'])
        self._tableau[6][6]=pion(piece._players['BLANC'])
        self._tableau[7][6]=pion(piece._players['BLANC'])

        self._tableau[0][7]=tour(piece._players['BLANC'])
        self._tableau[1][7]=cavalier(piece._players['BLANC'])
        self._tableau[2][7]=fou(piece._players['BLANC'])
        self._tableau[3][7]=reine(piece._players['BLANC'])
        self._tableau[4][7]=roi(piece._players['BLANC'])
        self._tableau[5][7]=fou(piece._players['BLANC'])
        self._tableau[6][7]=cavalier(piece._players['BLANC'])
        self._tableau[7][7]=tour(piece._players['BLANC'])

    def computePossible(self, color, array):
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if pion != None and pion.getColor() == color and not(type(pion) is roi):
                    pion.move(X, Y, self, array)

    def isPossible(self, pos_x, pos_y, array):
        return (pos_x, pos_y) in array

    def setPossible(self, pos_x, pos_y, color, array):
        if (pos_x <= 7 and pos_x >= 0 and pos_y <= 7 and pos_y >= 0):        
            if ((self.getPion(pos_x, pos_y) == None) or (self.getPion(pos_x, pos_y).getColor() * color <= 0)):
                array.add((pos_x, pos_y))

    def setPion(self, X, Y, pion):
        if (X <= 7 and X >= 0 and Y <= 7 and Y >= 0):
            self._tableau[X][Y]=pion

    def getPion(self, X, Y):
        if (X < 0):
            return None
        if (X > 7):
            return None
        if (Y < 0):
            return None
        if (Y > 7):
            return None
        return self._tableau[X][Y]
