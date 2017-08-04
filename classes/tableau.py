from piece import piece
from pion import pion
from fou import fou
from tour import tour
from cavalier import cavalier
from roi import roi
from reine import reine
import chess_interface
import queue
import chess_server
import time
from chess_recorder import recorder

class tableau():
    _tableau = [ [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None] ]
    _selected = False
    _init_x = -1
    _init_y = -1
    _curPlayer = -1
    _selectedPion = None
    _interface = None
    _queue = None
    _possible = set()
    _server = None
    _client = None
    _recorder = recorder()
    _currentMove = []
    
    def __init__(self, interface):
        self.reset()
        self._interface = interface
        self._queue = queue.Queue()

    def setPromoted(self, pion):
        if self._curPlayer != pion.getColor():
            return 0
        self.setPion(self._init_x, self._init_y, pion)       
        
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
        self._curPlayer = -1

    def computePossible(self, color, array):
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if pion != None and pion.getColor() == color:
                    pion.move(X, Y, self, array)

    def isPossible(self, pos_x, pos_y, array = _possible):
        return (pos_x, pos_y) in array

    def setPossible(self, pos_x, pos_y, color, array):
        if (pos_x <= 7 and pos_x >= 0 and pos_y <= 7 and pos_y >= 0):        
            if ((self.getPion(pos_x, pos_y) == None) or (self.getPion(pos_x, pos_y).getColor() * color <= 0)):
                array.add((pos_x, pos_y))

    def setPion(self, X, Y, pion):
        if (X <= 7 and X >= 0 and Y <= 7 and Y >= 0):
            oldPion=self._tableau[X][Y]
            if oldPion != None:
                self._currentMove.append((X, Y, oldPion.getLetter(), oldPion.getColor()))
            else:
                self._currentMove.append((X, Y, " ", 0))
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

    def checkMat(self):
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if type(pion) == roi and ((pion.getColor() == piece._players['NOIR'] and self._curPlayer == -1) or (pion.getColor() == piece._players['BLANC'] and self._curPlayer == 1)):
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

                        if self._curPlayer == 1 and not self.isPossible(posRoiX, posRoiY, possibleNoir):
                            return False
                        if self._curPlayer == -1 and not self.isPossible(posRoiX, posRoiY, possibleBlanc):
                            return False
                    
        # Check if by moving a piece, there is still mat position
        for X in range(0, 8):
            for Y in range(0, 8):
                pion = self.getPion(X, Y)
                if pion != None:
                    if (pion.getColor() * self._curPlayer) < 0:
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
                                if self._curPlayer == 1 and not self.isPossible(posPion_X, posPion_Y, possibleNoir):
                                    return False
                                if self._curPlayer == -1 and not self.isPossible(posPion_X, posPion_Y, possibleBlanc):
                                    return False
                            else:
                                if self._curPlayer == 1 and not self.isPossible(roi_X, roi_Y, possibleNoir):
                                    return False
                                if self._curPlayer == -1 and not self.isPossible(roi_X, roi_Y, possibleBlanc):
                                    return False
        return True
        
    def checkEchec(self):
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
            return self._curPlayer
        elif (noirEchec):
            return piece._players['NOIR']
        elif (blancEchec):
            return piece._players['BLANC']
        else:              
            return 0

    def play(self, pos_x, pos_y):
        if self._client != None and self._curPlayer == 1:
            self._client.sendData((pos_x, pos_y, self._curPlayer)) # client is white
        if self._server != None and self._curPlayer == -1:
            if not self._server.isConnected():
                self._interface.showMessage ("No client connected to the server")
                return
            self._server.sendData((pos_x, pos_y, self._curPlayer)) # server is black
        if self._selected == False:
            self._possible.clear()
            pionV = self.getPion(pos_x, pos_y)
            if (pionV != None and pionV.getColor() * self._curPlayer) > 0:
                self._selected = True
                self._selectedPion = pionV
                self._init_x = pos_x
                self._init_y = pos_y
                pionV.move(pos_x, pos_y, self, self._possible)
                if type(pionV) is roi:
                    pionV.checkRoque(self, self._possible)
            else:
                self._interface.showMessage ("Case non valide")
        else:
            self._selected = False
            if self.isPossible(pos_x, pos_y, self._possible):
                if type(self._selectedPion) is pion and pos_x != self._init_x and self.getPion(pos_x, pos_y) == None:
                    # Prise en passant
                    if (self._curPlayer == 1):
                        self.setPion(pos_x, pos_y - 1, None)
                    if (self._curPlayer == -1):
                        self.setPion(pos_x, pos_y + 1, None)                
                oldPion=self.getPion(pos_x, pos_y)
                self.setPion(self._init_x, self._init_y, None)
                self.setPion(pos_x, pos_y, self._selectedPion)
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
                        self._interface.showPromotion(self)
                    if pos_y == 0 and self._selectedPion.getColor() == -1:
                        self._init_x = pos_x
                        self._init_y = pos_y
                        self._interface.showPromotion(self)
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
                echec = self.checkEchec()
                if (echec == self._curPlayer):
                    self.setPion(pos_x, pos_y, oldPion)
                    self.setPion(self._init_x, self._init_y, self._selectedPion)
                    self._currentMove = []
                elif (echec == (-1 * self._curPlayer)):
                    self._selectedPion.setMoved()
                    if (self.checkMat()):
                        self._interface.showMessage("Echec et mat !")
                    else :
                        self._interface.showMessage("Echec !")
                    self.changePlayer()
                else:
                    self._selectedPion.setMoved()
                    self.changePlayer()
            else:
                self._interface.showMessage("Mouvement impossible")
            self._possible.clear()

    def resetTakeable(self, curPlayer):
        for X in range(0, 8):
            for Y in range(0, 8):
                curPion = self.getPion(X, Y)
                if type(curPion) is pion and curPion.getColor() == curPlayer:
                    curPion.setTakeableLeft(False)
                    curPion.setTakeableRight(False)

    def setCurPlayer(self, curPlayer):
        self._curPlayer = curPlayer

    def getCurPlayer(self):
        return self._curPlayer

    def changePlayer(self, addMove = True):
        if addMove:
            self._recorder.addMove(self._currentMove)
        self._currentMove=[]
        self.resetTakeable(self._curPlayer)
        self._curPlayer = (-1) * self._curPlayer

    def insertMove(self, pos_x, pos_y, curPlayer):
        self._queue.put((pos_x, pos_y, curPlayer))

    def openFile(self, filename):
        if self._server != None or self._client != None:
            self._interface.showMessage ("load file not permitted while playing in network")
            return
        if filename != "":
            for X in range(0, 8):
                for Y in range(0, 8):
                    self.setPion(X, Y, None)
            with open(filename) as f:
                content = f.readlines()
                f.close()
            for line in content:
                values = line.split(',')
                color = int(values[3].replace('\n', ''))
                pionLetter = values[2]
                if pionLetter == "T":
                    pionV = tour(color)
                elif pionLetter == "C":
                    pionV = cavalier(color)
                elif pionLetter == "F":
                    pionV = fou(color)
                elif pionLetter == "K":
                    pionV = roi(color)
                elif pionLetter == "Q":
                    pionV = reine(color)
                elif pionLetter == "P":
                    pionV = pion(color)
                self.setPion(int(values[0]), int(values[1]), pionV)
            self.setCurPlayer(-1)
            self._interface.draw(self)

    def saveFile(self, filename):
        if filename != "":
            file = open(filename, 'w')
            for Y in range(0, 8):
                for X in range(0, 8):
                    pion = self.getPion(X, Y)
                    if (pion != None):
                        file.write(str(X)+","+str(Y)+","+pion.getLetter()+"," + pion.getColor() + "\n")
            file.close()

    def start(self):
        self._interface.draw(self)
        while True:
            self._interface.mainLoop(self)
            try:
                 item = self._queue.get(True, 1)
            except KeyboardInterrupt:
                 item = (-1,-1,-1)
            except queue.Empty:
                 continue
            if item[0] == -1:
                if item[1] == -1:
                    self._interface.showMessage ("Exiting ...")
                elif item[1] == -2:
                    self._interface.showMessage ("Connection closed by opponent")
                else:
                    pass
                if self._client != None:
                    self._interface.showMessage ("Stopping client")
                    if item[1] == -1:
                        self._client.sendData((-1,-2,-1))
                    self._client.stop()
                if self._server != None:
                    self._interface.showMessage ("Stopping server")
                    if item[1] == -1:
                        self._server.sendData((-1,-2,-1))
                    self._server.stop()
                break
            elif item[0] == -2:
                pass
            else:
                self.play(item[0], item[1])
            self._interface.draw(self)

    def askForAction(self):
        if (self._server != None and self._curPlayer == -1):
            return True
        if (self._client != None and self._curPlayer == 1):
            return True
        if (self._client == None and self._server == None):
            return True
        return False

    def printMoves(self):
        self._recorder.printMoves()
        self._recorder.prettyPrintMoves()

    def undoLastMove(self):
        lastMove = self._recorder.getLastMove()
        if lastMove != None:
            for move in lastMove:
                pionV = None
                pionLetter = move[2]
                color = move[3]
                if pionLetter == "T":
                    pionV = tour(color)
                elif pionLetter == "C":
                    pionV = cavalier(color)
                elif pionLetter == "F":
                    pionV = fou(color)
                elif pionLetter == "K":
                    pionV = roi(color)
                elif pionLetter == "Q":
                    pionV = reine(color)
                elif pionLetter == "P":
                    pionV = pion(color)
                self.setPion(move[0], move[1], pionV)
            self.changePlayer(False)
        else:
            self._interface.showMessage ("No moves recorded")

    def stopServer(self):
        self._server.stop()
        self._server = None

    def stopClient(self):
        self._client.stop()
        self._client = None

    def startServer(self, port):
        try:
            self._server = chess_server.chessServer(self._queue, port)
            self._server.start()
            self.reset()
        except:
            self._server = None

    def startClient(self, host, port):
        try:
            self._client = chess_server.chessClient(self._queue, host, port)
            self._client.start()
            time.sleep(2)
            if (self._client.isConnected()):
                self.reset()
            else:
                self._client = None
        except Exception as e:
            print (e)
            self._client = None
