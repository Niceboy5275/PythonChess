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
        for X in range(0, 8):
            for Y in range(0, 8):
                tableau.setPion(X, Y, None)
        with open(filename) as f:
            content = f.readlines()
            f.close()
        for line in content:
            values = line.split(',')
            color = int(values[3].replace('\n', ''))
            pionLetter = values[2]
            if pionLetter == "T":
                pionV = tour.tour(color)
            elif pionLetter == "C":
                pionV = cavalier.cavalier(color)
            elif pionLetter == "F":
                pionV = fou.fou(color)
            elif pionLetter == "K":
                pionV = roi.roi(color)
            elif pionLetter == "Q":
                pionV = reine.reine(color)
            elif pionLetter == "P":
                pionV = pion.pion(color)
            tableau.setPion(int(values[0]), int(values[1]), pionV)
        curPlayer = -1
        draw()


def showEchec():
    print("Echec !")

def showEchecEtMat():
    print("Echec et mat !")

def showPromotion():
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
    print ("    0   1   2   3   4   5   6   7")
    print (" ")
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
