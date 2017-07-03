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
    for X in range(0, 8):
        for Y in range(0, 8):
            tableau.setPion(X, Y, None)
    with open(filename) as f:
        content = f.readlines()
        f.close()
    for line in content:
        values = line.split(',')
        tableau.setPion(int(values[1]), int(values[0]), int(values[2].replace('\n', '')))
    curPlayer = -1
    draw()

def showEchec():
    print "Echec !"

def showEchecEtMat():
    print "Echec et mat !"

def draw():
    print "    0    1    2    3    4    5    6    7"
    print "                                        "
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
            print strValue
curPlayer = piece._players['BLANC']
selected = False
selectedPion = 0
init_x = 0
init_y = 0

draw()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    if (curPlayer == piece._players['NOIR']) :
        print "Joueur noir"
    else:
        print "Joueur blanc"
    action = raw_input("Action : ")
    try:
        if (action == "quit"):
            LOOP_ACTIVE = False
        elif (action.find("load") != -1):
            values = action.split(" ")
            print("Filename : " + values[1])
            openfile(values[1])
        else:
            values = action.split(" ")
            val, possible = tableau.play(int(values[0]), int(values[1]), curPlayer)
            if (val == 0):
                if (curPlayer == piece._players['NOIR']):
                    curPlayer = piece._players['BLANC']
                else:
                    curPlayer = piece._players['NOIR']
            draw()
    except:
        print "Commande non comprise"
        traceback.print_exc(file=sys.stdout)
