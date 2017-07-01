from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import csv
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

possible= set()

possibleBlanc= set()

possibleNoir= set()

def newGame():
    tableau.reset()
    curPlayer = -1
    draw()

def openFile():
    global curPlayer
    filename = askopenfilename(filetypes=(("Chess files", "*.chy"),
                                           ("All files", "*.*") ))
    print ("file : " + filename)
    if filename != "":
        for X in range(0, 8):
            for Y in range(0, 8):
                tableau.setPion(X, Y, None)
        with open(filename) as f:
            content = f.readlines()
            f.close()
        for line in content:
            print ("data : " + line)
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

def saveFile():
    filename = asksaveasfilename(filetypes=(("Chess files", "*.chy"),
                                      ("All files", "*.*") ))
    print ("file : " + filename)
    if filename != "":
        file = open(filename, 'w')
        for Y in range(0, 8):
            for X in range(0, 8):
                pion = tableau.getPion(X, Y)
                if (pion != None):
                    file.write(str(X)+","+str(Y)+","+pion.getLetter()+"," + pion.getColor() + "\n")
        file.close()


def button1(event):
    global selected
    global init_x
    global init_y
    global selectedPion
    global curPlayer
    pos_x = int((event.x - 10) / 40)
    pos_y = int((event.y - 10) / 40)
    if selected == False:
        pion = tableau.getPion(pos_x, pos_y)
        if (pion != None and pion.getColor() * curPlayer) > 0:
            selected = True
            selectedPion = pion
            init_x = pos_x
            init_y = pos_y
            pion.move(pos_x, pos_y, tableau, possible)
        else:
            print ("Case non valide")
    else:
        selected = False
        if tableau.isPossible(pos_x, pos_y, possible):
            oldPion=tableau.getPion(pos_x, pos_y)
            tableau.setPion(pos_x, pos_y, selectedPion)
            tableau.setPion(init_x, init_y, None)
            echec = tableau.checkEchec(curPlayer)
            if (echec == curPlayer):
                showEchec()
                tableau.setPion(pos_x, pos_y, oldPion)
                tableau.setPion(init_x, init_y, selectedPion)
            elif (echec == (-1 * curPlayer)):
                if (tableau.checkMat(curPlayer)):
                    showEchecEtMat()
                else :
                    showEchec()
                curPlayer = curPlayer * (-1)
            else:
                curPlayer = curPlayer * (-1)
        else:
            print("Mouvement impossible")
        tableau.computePossible(piece._players['NOIR'], possibleNoir)
        tableau.computePossible(piece._players['BLANC'], possibleBlanc)
        possible.clear()
    draw()
    
def showEchec():
    toplevel = Toplevel()
    label1 = Label(toplevel, text="Echec !!")
    label1.pack()

def showEchecEtMat():
    toplevel = Toplevel()
    label1 = Label(toplevel, text="Echec et mat!!")
    label1.pack()

def draw():
    global tableau
    if curPlayer == 1:
        curPlayerName.set("Joueur noir")
    else:
        curPlayerName.set("Joueur blanc")
    for X in range(0,8):
        for Y in range(0,8):
            if ((X+Y) % 2 == 0):
                color = 'white'
            else:
                color = 'grey'
            canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill=color)
            if (noirsCB.get() == 1):
                if (tableau.isPossible(X, Y, possibleNoir)):
                    canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 30 + 40 * X, 50 + 40 * Y, fill='green')
            if (blancsCB.get() == 1):
                if (tableau.isPossible(X, Y, possibleBlanc)):
                    canvas.create_rectangle(30 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='yellow')
            if (tableau.isPossible(X, Y, possible)):
                canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='red')
            pionV=tableau.getPion(X, Y)
            if pionV != None:
                if type(pionV) is pion.pion and pionV.getColor() == piece._players['NOIR']:
                    imageP=pion_n
                if type(pionV) is pion.pion and pionV.getColor() == piece._players['BLANC']:
                    imageP=pion_b
                if type(pionV) is tour.tour and pionV.getColor() == piece._players['NOIR']:
                    imageP=tour_n
                if type(pionV) is tour.tour and pionV.getColor() == piece._players['BLANC']:
                    imageP=tour_b
                if type(pionV) is cavalier.cavalier and pionV.getColor() == piece._players['NOIR']:
                    imageP=cavalier_n
                if type(pionV) is cavalier.cavalier and pionV.getColor() == piece._players['BLANC']:
                    imageP=cavalier_b
                if type(pionV) is fou.fou and pionV.getColor() == piece._players['NOIR']:
                    imageP=fou_n
                if type(pionV) is fou.fou and pionV.getColor() == piece._players['BLANC']:
                    imageP=fou_b
                if type(pionV) is roi.roi and pionV.getColor() == piece._players['NOIR']:
                    imageP=roi_n
                if type(pionV) is roi.roi and pionV.getColor() == piece._players['BLANC']:
                    imageP=roi_b
                if type(pionV) is reine.reine and pionV.getColor() == piece._players['NOIR']:
                    imageP=reine_n
                if type(pionV) is reine.reine and pionV.getColor() == piece._players['BLANC']:
                    imageP=reine_b
                
                canvas.create_image(10 + 40 * X, 10 + 40 * Y, anchor=NW, image=imageP)


fenetre = Tk()

pion_b=PhotoImage(file="pion_b.png")
pion_n=PhotoImage(file="pion_n.png")
cavalier_b=PhotoImage(file="cavalier_b.png")
cavalier_n=PhotoImage(file="cavalier_n.png")
roi_b=PhotoImage(file="roi_b.png")
roi_n=PhotoImage(file="roi_n.png")
reine_b=PhotoImage(file="reine_b.png")
reine_n=PhotoImage(file="reine_n.png")
fou_b=PhotoImage(file="fou_b.png")
fou_n=PhotoImage(file="fou_n.png")
tour_b=PhotoImage(file="tour_b.png")
tour_n=PhotoImage(file="tour_n.png")

menubar = Menu(fenetre)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=newGame)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=filemenu)

fenetre.config(menu=menubar)
fenetre.title("Echecs")
canvas=Canvas(fenetre, width=340, height=340)
canvas.grid(row=1, column = 1, columnspan=2, sticky=W)
curPlayerName=StringVar()
curPlayerName.set("Joueur blanc")
label = Label(fenetre, textvariable=curPlayerName)
label.grid(row=2, column = 1, columnspan=2, sticky=N)
noirsCB = IntVar()
Checkbutton(fenetre, text="noirs", variable=noirsCB).grid(row=3, column = 1, sticky=W)
blancsCB = IntVar()
Checkbutton(fenetre, text="blancs", variable=blancsCB).grid(row=3, column = 2, sticky=W)

curPlayer = -1
selected = False
selectedPion = 0 
init_x = 0
init_y = 0

fenetre.bind('<Button-1>', button1)
draw()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    fenetre.update()
