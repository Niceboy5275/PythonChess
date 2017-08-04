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

class chess_simple(chessInterface):

    def showMessage(self, message):
        print(message)

    def showPromotion(self, tableau):
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
        
    def draw(self, tableau):
        for Y in range(0,8):
            for Z in range(0,3):
                strValue = ""
                for X in range(0, 8):
                    if ((X+Y) % 2 == 0):
                        bkg = "*"
                    else:
                        bkg = " "
                    if (tableau.isPossible(X, Y)):
                        bkg = "+"
                    if Z != 1:
                        if X == 0:
                            strValue = '  '
                        strValue = strValue + bkg + bkg + bkg + bkg
                    else:
                        if X == 0:
                            strValue = str(8 - Y) + ' '
                        pionClass = tableau.getPion(X, Y)
                        bkg_pion = bkg
                        if (pionClass == None):
                            pionString = bkg + bkg
                        elif (pionClass.getColor() < 0):
                            pionString = pionClass.getLetter() + "B"
                        elif (pionClass.getColor() > 0):
                            pionString = pionClass.getLetter() + "N"
                        else:
                            pass
                        strValue = strValue + bkg + pionString + bkg 
                print(strValue)
        print("    A   B   C   D   E   F   G   H")
        print("")

    def mainLoop(self, tableau):
        if tableau.askForAction():
            if (tableau.getCurPlayer() == piece._players['NOIR']) :
                action = input("Action (Joueur noir) : ")
            else:
                action = input("Action (Joueur blanc) : ")
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
            except:
                print("Commande non comprise")
                traceback.print_exc(file=sys.stdout)
