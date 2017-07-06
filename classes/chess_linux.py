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
    print ("Echec !")

def showEchecEtMat():
    print ("Echec et mat !")

def showPromotion(curPlayer):
    print ("Enter the type of piece you want (P, T, C, F, Q) :")
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
    print ("    0    1    2    3    4    5    6    7")
    print ("                                        ")
    for Y in range(0,8):
        for Z in range(0,3):
            strValue = ""
            for X in range(0, 8):
                if ((X+Y) % 2 == 0):
                    bkg = 47
                else:
                    bkg = 40
                if (tableau.isPossible(X, Y, possible)):
                    bkg = 41
                if Z == 0 or Z == 2:
                    if X == 0:
                        strValue = '  '
                    strValue = strValue + '\033[1;38;' + str(bkg) + 'm' + "     " + '\033[0m'
                else:
                    if X == 0:
                        strValue = str(Y) + ' '
                    pionClass = tableau.getPion(X, Y)
                    bkg_pion = bkg
                    if (pionClass == None):
                        color = "1;38"
                        bkg_pion = bkg
                        pionString = " "
                    elif (pionClass.getColor() < 0):
                        if (curPlayer == piece._players['BLANC']):
                            bkg_pion = 42
                        color = "1;38"
                        pionString = pionClass.getLetter()
                    elif (pionClass.getColor() > 0):
                        if (curPlayer == piece._players['NOIR']):
                            bkg_pion = 42
                        color = "1;30"
                        pionString = pionClass.getLetter()
                    else:
                        bkg_pion = bkg
                        pionString = pionClass.getLetter()
                    strValue = strValue + '\033[1;38;' + str(bkg) + 'm \033[0m\033[' + color + ';' + str(bkg_pion) + 'm ' + pionString + ' \033[0m\033[1;38;' + str(bkg) + 'm \033[0m'
            print (strValue)
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
            values = action.split(" ")
            res = tableau.play(int(values[0]), int(values[1]), curPlayer, possible)
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
