import sys, traceback
import tableau
import tour
import fou
import cavalier
import pion
import roi
import reine
from piece import piece
from chess_interface import chessInterface

class chess_linux(chessInterface):

    def __init__(self):
        pass

    def showMessage(self, message):
        print(message)

    def showPromotion(self, tableau):
        try:
            curPlayer = tableau.getCurPlayer()
            print("Enter the type of piece you want (T, C, F, Q) :")
            piece = input("Piece : ")
            while (True):
                if piece == "T":
                    tableau.setPromoted(tour.tour(curPlayer))
                    break
                elif piece == "C":
                    tableau.setPromoted(cavalier.cavalier(curPlayer))
                    break
                elif piece == "F":
                    tableau.setPromoted(fou.fou(curPlayer))
                    break
                elif piece == "Q":
                    tableau.setPromoted(reine.reine(curPlayer))
                    break
                else:
                    piece = input("Piece : ")
            self.draw(tableau)
        except KeyboardInterrupt:  #pragma: no cover
            tableau.insertMove(-1, -1, -1)
    
        
    def draw(self, tableau):
        for Y in range(0,8):
            for Z in range(0,3):
                strValue = ""
                for X in range(0, 8):
                    if ((X+Y) % 2 == 0):
                        bkg = 47
                    else:
                        bkg = 40
                    if (tableau.isPossible(X, Y)):
                        bkg = 41
                    if Z == 0 or Z == 2:
                        if X == 0:
                            strValue = '  '
                        strValue = strValue + '\033[1;38;' + str(bkg) + 'm' + "     " + '\033[0m'
                    else:
                        if X == 0:
                            strValue = str(8 - Y) + ' '
                        pionClass = tableau.getPion(X, Y)
                        bkg_pion = bkg
                        if (pionClass == None):
                            color = "1;38"
                            bkg_pion = bkg
                            pionString = " "
                        elif (pionClass.getColor() < 0):
                            if (tableau.getCurPlayer() == piece._players['BLANC']):
                                bkg_pion = 42
                            color = "1;38"
                            pionString = pionClass.getLetter()
                        else:
                            if (tableau.getCurPlayer() == piece._players['NOIR']):
                                bkg_pion = 42
                            color = "1;30"
                            pionString = pionClass.getLetter()
                        strValue = strValue + '\033[1;38;' + str(bkg) + 'm \033[0m\033[' + color + ';' + str(bkg_pion) + 'm ' + pionString + ' \033[0m\033[1;38;' + str(bkg) + 'm \033[0m'
                print(strValue)
        print("    A    B    C    D    E    F    G    H")
        print("")

    def mainLoop(self, tableau):
        if tableau.askForAction() :
            try:
                if (tableau.getCurPlayer() == piece._players['NOIR']) :
                    action = input("Action (Joueur noir) : ")
                else:
                    action = input("Action (Joueur blanc) : ")
            except KeyboardInterrupt: #pragma: no cover
                tableau.insertMove(-1, -1, -1)
                return
            try:
                if (action == "quit"):
                    tableau.insertMove(-1, -1, -1)
                elif (action.find("load") != -1):
                    values = action.split(" ")
                    tableau.openFile(values[1])
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("save") != -1):
                    values = action.split(" ")
                    tableau.saveFile(values[1])
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("start server ") != -1):
                    values = action.split(" ")
                    tableau.startServer(int(values[2]))
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("start client ") != -1):
                    values = action.split(" ")
                    tableau.startClient(values[2], int(values[3]))
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("stop server") != -1):
                    tableau.stopServer()
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("stop client") != -1):
                    tableau.stopClient()
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("print moves") != -1):
                    tableau.printMoves()
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("undo") != -1):
                    tableau.undoLastMove()
                    tableau.insertMove(-2, -2, -1)
                elif (action.find("help") != -1):
                    print ("Available commands:")
                    print ("===================")
                    print ("load <file name> : load a file with piece positions")
                    print ("save <file name> : save current chessboard into file")
                    print ("start server <port number> : start a server listening on given port")
                    print ("stop server : stop the running server")
                    print ("start client <ip> <port number> : connect to the server on given ip/ port")
                    print ("stop client : stop the connection to the server")
                    print ("undo : revert the last move")
                    print ("print moves : print the moves (not in PGN format yet)")
                    print ("help : print this help")
                else:
                    input_x = -1
                    if (action[0] == "A" or action[0] == "a"):
                        input_x = 0
                    if (action[0] == "B" or action[0] == "b"):
                        input_x = 1
                    if (action[0] == "C" or action[0] == "c"):
                        input_x = 2
                    if (action[0] == "D" or action[0] == "d"):
                        input_x = 3
                    if (action[0] == "E" or action[0] == "e"):
                        input_x = 4
                    if (action[0] == "F" or action[0] == "f"):
                        input_x = 5
                    if (action[0] == "G" or action[0] == "g"):
                        input_x = 6
                    if (action[0] == "H" or action[0] == "h"):
                        input_x = 7
                    if input_x == -1:
                        values = action.split(" ")
                        input_x = int(values[0])
                        input_y =int(values[1])
                    else:
                        input_y = 8-int(action[1])
                    tableau.insertMove(input_x, input_y, tableau.getCurPlayer())
            except:   #pragma: no cover
                print("Commande non comprise")
                traceback.print_exc(file=sys.stdout)
                tableau.insertMove(-2, -2, -1)
