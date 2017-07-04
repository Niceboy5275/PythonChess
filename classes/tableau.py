from piece import piece
from pion import pion
from fou import fou
from tour import tour
from cavalier import cavalier
from roi import roi
from reine import reine

class tableau():
    _tableau = [ [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None] ]
    _selected = False
    _init_x = -1
    _init_y = -1
    _selectedPion = None

    def __init__(self):
        self.reset()

    def setPromoted(self, pion, curPlayer):
        if curPlayer != pion.getColor():
            return 0
        self.setPion(self._init_x, self._init_y, pion)       
        echec = self.checkEchec(curPlayer)
        if (echec == curPlayer):
            res = 1
            self.setPion(pos_x, pos_y, oldPion)
            self.setPion(self._init_x, self._init_y, self._selectedPion)
        elif (echec == (-1 * curPlayer)):
            self._selectedPion.setMoved()
            if (self.checkMat(curPlayer)):
                res = 2
            else :
                res = 3
        else:
            self._selectedPion.setMoved()
            res = 4
        return res
        
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
                if pion != None and pion.getColor() == color:
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

    def checkMat(self, curPlayer):
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if type(pion) == roi and ((pion.getColor() == piece._players['NOIR'] and curPlayer == -1) or (pion.getColor() == piece._players['BLANC'] and curPlayer == 1)):
                    roi_X = X
                    roi_Y = Y
                    posPion = set()
                    pion.move(X, Y, self, posPion)
                    for (posRoiX, posRoiY) in posPion:
                        oldValue = self.getPion(posRoiX, posRoiY)
                        self.setPion(posRoiX, posRoiY, pion)
                        self.setPion(X, Y, None)
                        # compute Possible
                        possibleBlanc = set()
                        possibleNoir = set()
                        self.computePossible(piece._players['NOIR'], possibleNoir)
                        self.computePossible(piece._players['BLANC'], possibleBlanc)
                        self.setPion(X, Y, pion)
                        self.setPion(posRoiX, posRoiY, oldValue)

                        if curPlayer == 1 and not self.isPossible(posRoiX, posRoiY, possibleNoir):
                            print ("CheckMat - 1")
                            return False
                        if curPlayer == -1 and not self.isPossible(posRoiX, posRoiY, possibleBlanc):
                            print ("CheckMat - 2")
                            return False
                    
        # Check if by moving a piece, there is still mat position
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if pion != None:
                    if (pion.getColor() * curPlayer) < 0:
                        posPion = set()
                        pion.move(X, Y, self, posPion)
                        for (posPion_X, posPion_Y) in posPion:
                            oldValue = self.getPion(posPion_X, posPion_Y)
                            self.setPion(posPion_X, posPion_Y, pion)
                            self.setPion(X, Y, None)
                            # compute Possible
                            possibleBlanc = set()
                            possibleNoir = set()
                            self.computePossible(piece._players['NOIR'], possibleNoir)
                            self.computePossible(piece._players['BLANC'], possibleBlanc)
                            self.setPion(X, Y, pion)
                            self.setPion(posPion_X, posPion_Y, oldValue)
                            if (type(pion) == roi):
                                if curPlayer == 1 and not self.isPossible(posPion_X, posPion_Y, possibleNoir):
                                    print ("CurPos : " + str(X) + "/" + str(Y))
                                    print ("NextPos : " + str(posPion_X) + "/" + str(posPion_Y))
                                    print ("CheckMat - 3")
                                    return False
                                if curPlayer == -1 and not self.isPossible(posPion_X, posPion_Y, possibleBlanc):
                                    print ("CurPos : " + str(X) + "/" + str(Y))
                                    print ("NextPos : " + str(posPion_X) + "/" + str(posPion_Y))
                                    for (pX, pY) in possibleBlanc:
                                        print ("Possible : " + str(pX) + "/" + str(pY))
                                    print ("CheckMat - 4")
                                    return False
                            else:
                                if curPlayer == 1 and not self.isPossible(roi_X, roi_Y, possibleNoir):
                                    print ("CurPos : " + str(X) + "/" + str(Y))
                                    print ("NextPos : " + str(posPion_X) + "/" + str(posPion_Y))
                                    print ("CheckMat - 3")
                                    return False
                                if curPlayer == -1 and not self.isPossible(roi_X, roi_Y, possibleBlanc):
                                    print ("CurPos : " + str(X) + "/" + str(Y))
                                    print ("NextPos : " + str(posPion_X) + "/" + str(posPion_Y))
                                    for (pX, pY) in possibleBlanc:
                                        print ("Possible : " + str(pX) + "/" + str(pY))
                                    print ("CheckMat - 4")
                                    return False
        return True
        
    def checkEchec(self, curPlayer):
        possibleBlanc = set()
        possibleNoir = set()
        self.computePossible(piece._players['NOIR'], possibleNoir)
        self.computePossible(piece._players['BLANC'], possibleBlanc)
        noirEchec=False
        blancEchec=False
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if (type(pion) is roi):
                    if (pion.getColor() == piece._players['NOIR'] and self.isPossible(X, Y, possibleBlanc) == 1):
                        noirEchec=True
                    if (pion.getColor() == piece._players['BLANC'] and self.isPossible(X, Y, possibleNoir) == 1):
                        blancEchec=True
        if (noirEchec and blancEchec):
            return curPlayer
        elif (noirEchec):
            return piece._players['NOIR']
        elif (blancEchec):
            return piece._players['BLANC']
        else:              
            return 0

    def play(self, pos_x, pos_y, curPlayer, possible):
        if self._selected == False:
            pionV = self.getPion(pos_x, pos_y)
            if (pionV != None and pionV.getColor() * curPlayer) > 0:
                self._selected = True
                self._selectedPion = pionV
                self._init_x = pos_x
                self._init_y = pos_y
                pionV.move(pos_x, pos_y, self, possible)
                if type(pionV) is roi:
                    pionV.checkRoque(self, possible)
                res = 5
            else:
                print ("Case non valide")
                res = 6
        else:
            self._selected = False
            if self.isPossible(pos_x, pos_y, possible):
                if type(self._selectedPion) is pion and pos_x != self._init_x and self.getPion(pos_x, pos_y) == None:
                    # Prise en passant
                    if (curPlayer == 1):
                        self.setPion(pos_x, pos_y - 1, None)
                    if (curPlayer == -1):
                        self.setPion(pos_x, pos_y + 1, None)
                oldPion=self.getPion(pos_x, pos_y)
                self.setPion(pos_x, pos_y, self._selectedPion)
                self.setPion(self._init_x, self._init_y, None)
                if type(self._selectedPion) is roi:
                    #Check roque position
                    if (self._init_x - pos_x) * (self._init_x - pos_x) + (self._init_y - pos_y) * (self._init_y - pos_y) == 4:
                        if self._init_x > pos_x:
                            # Left roque
                            tour = self.getPion(0, self._init_y)
                            self.setPion(3, self._init_y, tour)
                            self.setPion(0, self._init_y, None)
                        else:
                            #right roque
                            tour = self.getPion(7, self._init_y)
                            self.setPion(5, self._init_y, tour)
                            self.setPion(7, self._init_y, None)
                if type(self._selectedPion) is pion:
                    if pos_y == 7 and self._selectedPion.getColor() == 1:
                        self._init_x = pos_x
                        self._init_y = pos_y
                        return 8
                    if pos_y == 0 and self._selectedPion.getColor() == -1:
                        self._init_x = pos_x
                        self._init_y = pos_y
                        return 8
                    if pos_y == 3 and self._selectedPion.getColor() == 1:
                        if (pos_y - self._init_y == 2):
                            neighborPion = self.getPion(pos_x - 1, pos_y)
                            if type(neighborPion) is pion and neighborPion.getColor() == -1:
                                neighborPion.setTakeableLeft(True)
                            neighborPion = self.getPion(pos_x + 1, pos_y)
                            if type(neighborPion) is pion and neighborPion.getColor() == -1:
                                neighborPion.setTakeableRight(True)
                    if pos_y == 4 and self._selectedPion.getColor() == -1:
                        if (self._init_y - pos_y  == 2):
                            neighborPion = self.getPion(pos_x - 1, pos_y)
                            if type(neighborPion) is pion and neighborPion.getColor() == 1:
                                neighborPion.setTakeableLeft(True)
                            neighborPion = self.getPion(pos_x + 1, pos_y)
                            if type(neighborPion) is pion and neighborPion.getColor() == 1:
                                neighborPion.setTakeableRight(True)
                echec = self.checkEchec(curPlayer)
                if (echec == curPlayer):
                    res = 1
                    self.setPion(pos_x, pos_y, oldPion)
                    self.setPion(self._init_x, self._init_y, self._selectedPion)
                elif (echec == (-1 * curPlayer)):
                    self._selectedPion.setMoved()
                    if (self.checkMat(curPlayer)):
                        res = 2
                    else :
                        self.resetTakeable(curPlayer)
                        res = 3
                else:
                    self.resetTakeable(curPlayer)
                    self._selectedPion.setMoved()
                    res = 4
            else:
                print("Mouvement impossible")
                res = 7
            possible.clear()
        return res

    def resetTakeable(self, curPlayer):
        for X in range(0, 8):
            for Y in range(0, 8):
                curPion = self.getPion(X, Y)
                if type(curPion) is pion and curPion.getColor() == curPlayer:
                    curPion.setTakeableLeft(False)
                    curPion.setTakeableRight(False)                    
