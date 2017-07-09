import sys, traceback
import tableau
import tour
import fou
import cavalier
import pion
import roi
import reine
from piece import piece

tableau = tableau.tableau()

possible = set()

def openFile(filename):
    global curPlayer
    if filename != "":
        tableau.loadFile(filename)
        curPlayer = -1
        draw()


def showEchec():
    print("Echec !")

def showEchecEtMat():
    print("Echec et mat !")

def showPromotion(curPlayer):
    print("Enter the type of piece you want (P, T, C, F, Q) :")
    piece = input("Piece : ")
    if piece == "P":
        res = tableau.setPromoted(pion.pion(curPlayer), curPlayer)
    elif piece == "T":
        res = tableau.setPromoted(tour.tour(curPlayer), curPlayer)
    elif piece == "C":
        res = tableau.setPromoted(cavalier.cavalier(curPlayer), curPlayer)
    elif piece == "F":
        res = tableau.setPromoted(fou.fou(curPlayer), curPlayer)
    elif piece == "Q":
        res = tableau.setPromoted(reine.reine(curPlayer), curPlayer)
    else:
        return
    if res == 1:
        showEchec()
    elif res == 2:
        showEchecEtMat()
    elif res == 3:
        showEchec()
        curPlayer = curPlayer * (-1)
    elif res == 4:
        curPlayer = curPlayer * (-1)
    else:
        return
    possible.clear()
    draw()

    
def draw():
    for Y in range(0,8):
        for Z in range(0,3):
            strValue = ""
            for X in range(0, 8):
                if ((X+Y) % 2 == 0):
                    bkg = "*"
                else:
                    bkg = " "
                if (tableau.isPossible(X, Y, possible)):
                    bkg = "+"
                if Z == 0 or Z == 2:
                    if X == 0:
                        strValue = '  '
                    strValue = strValue + bkg + bkg + bkg + bkg
                else:
                    if X == 0:
                        strValue = str(Y) + ' '
                    pionClass = tableau.getPion(X, Y)
                    bkg_pion = bkg
                    if (pionClass == None):
                        bkg_pion = bkg
                        pionString = bkg + bkg
                    elif (pionClass.getColor() < 0):
                        pionString = pionClass.getLetter() + "B"
                    elif (pionClass.getColor() > 0):
                        pionString = pionClass.getLetter() + "N"
                    else:
                        bkg_pion = bkg
                        pionString = pionClass.getLetter()
                    strValue = strValue + bkg + pionString + bkg
            print (strValue)
    print("    A   B   C   D   E   F   G   H")
    print("")

curPlayer = piece._players['BLANC']
selected = False
selectedPion = 0
init_x = 0
init_y = 0

draw()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    if (curPlayer == piece._players['NOIR']) :
        print ("Joueur noir")
    else:
        print ("Joueur blanc")
    action = input("Action : ")
    try:
        if (action == "quit"):
            LOOP_ACTIVE = False
        elif (action.find("load") != -1):
            values = action.split(" ")
            print("Filename : " + values[1])
            openFile(values[1])
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
            res = tableau.play(input_x, input_y, curPlayer, possible)
            if res == 1:
                showEchec()
            elif res == 2:
                showEchecEtMat()
            elif res == 3:
                showEchec()
                curPlayer = curPlayer * (-1)
            elif res == 4:
                curPlayer = curPlayer * (-1)
            elif res ==8:
                showPromotion(curPlayer)
            draw()

    except:
        print ("Commande non comprise")
        traceback.print_exc(file=sys.stdout)
