from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 
import csv

def donothing():
   filewin = Toplevel(fenetre)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def newGame():
    global tableau
    global curPlayer
    print ("called newGame")
    tableau = [[1,2,3,4,5,3,2,1],
           [6,6,6,6,6,6,6,6],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [-6,-6,-6,-6,-6,-6,-6,-6],
           [-1,-2,-3,-4,-5,-3,-2,-1]]
    curPlayer = -1
    computePossible()
    draw()
   
def openFile():
    global curPlayer
    filename = askopenfilename(filetypes=(("Chess files", "*.chy"),
                                           ("All files", "*.*") ))
    print ("file : " + filename)
    if filename != "":
        for X in range(0, 8):
            for Y in range(0, 8):
                tableau[X][Y]=0
        with open(filename) as f:
            content = f.readlines()
            f.close()
        for line in content:
            print ("data : " + line)
            values = line.split(',')
            print(values)
            tableau[int(values[1])][int(values[0])]=int(values[2].replace('\n', ''))
        curPlayer = -1
        computePossible()
        draw()

def saveFile():
    filename = asksaveasfilename(filetypes=(("Chess files", "*.chy"),
                                      ("All files", "*.*") ))
    print ("file : " + filename)
    if filename != "":
        file = open(filename, 'w')
        for Y in range(0, 8):
            for X in range(0, 8):
                pion = getPion(X, Y)
                if (pion != 0):
                    file.write(str(X)+","+str(Y)+","+str(pion)+"\n")
        file.close()

tableau = [[1,2,3,4,5,3,2,1],
           [6,6,6,6,6,6,6,6],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [-6,-6,-6,-6,-6,-6,-6,-6],
           [-1,-2,-3,-4,-5,-3,-2,-1]]

possible= set()

possibleBlanc= set()

possibleNoir= set()

def resetPossible(array=possible):
    array.clear()

def computePossible():
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if (pion > 0):
                array=possibleNoir
            if (pion < 0):
                array=possibleBlanc
            if abs(pion) == 2:
                moveCavalier(X, Y, array)
            if abs(pion) == 1:
                moveTour(X, Y, array)
            if abs(pion) == 3:
                moveFou(X, Y, array)
            if abs(pion) == 4:
                moveFou(X, Y, array)
                moveTour(X, Y, array)
            if abs(pion) == 5:
                moveRoi(X, Y, array)
            if pion == -6:
                movePionBlanc(X, Y, array)
            if pion == 6:
                movePionNoir(X, Y, array)
                
def getPion(pos_x, pos_y):
    if (pos_x < 0):
        return None
    if (pos_x > 7):
        return None
    if (pos_y < 0):
        return None
    if (pos_y > 7):
        return None
    return tableau[pos_y][pos_x]

def setPossible(pos_x, pos_y, color = 0, array=possible):
    if ((getPion(pos_x, pos_y) != None) and (getPion(pos_x, pos_y) * color <= 0)):
        array.add((pos_x, pos_y))

def isPossible(pos_x, pos_y, array=possible):
    return (pos_x, pos_y) in array

def moveRoi(pos_x, pos_y, array=possible):
    movePossible = 0
    curColor = getPion(pos_x, pos_y)
    if (curColor > 0):
        opponent = possibleBlanc
    else:
        opponent = possibleNoir
    if (getPion(pos_x - 1, pos_y - 1) != None) and not isPossible(pos_x - 1, pos_y - 1,opponent):
        setPossible(pos_x - 1, pos_y - 1, curColor, array)
        movePossible = movePossible + 1
    if (getPion(pos_x - 1, pos_y) != None) and not isPossible(pos_x - 1, pos_y,opponent):
        setPossible(pos_x - 1, pos_y, curColor, array)
        movePossible = movePossible + 2
    if (getPion(pos_x - 1, pos_y + 1) != None) and not isPossible(pos_x - 1, pos_y + 1,opponent):
        setPossible(pos_x - 1, pos_y + 1, curColor, array)
        movePossible = movePossible + 4
    if (getPion(pos_x, pos_y + 1) != None) and not isPossible(pos_x, pos_y + 1,opponent):
        setPossible(pos_x, pos_y + 1, curColor, array)
        movePossible = movePossible + 8
    if (getPion(pos_x + 1, pos_y + 1) != None) and not isPossible(pos_x + 1, pos_y + 1,opponent):
        setPossible(pos_x + 1, pos_y + 1, curColor, array)
        movePossible = movePossible + 16
    if (getPion(pos_x + 1, pos_y) != None) and not isPossible(pos_x + 1, pos_y,opponent):
        setPossible(pos_x + 1, pos_y, curColor, array)
        movePossible = movePossible + 32
    if (getPion(pos_x + 1, pos_y - 1) != None) and not isPossible(pos_x + 1, pos_y - 1,opponent):
        setPossible(pos_x + 1, pos_y - 1, curColor, array)
        movePossible = movePossible + 64
    if (getPion(pos_x, pos_y - 1) != None) and not isPossible(pos_x, pos_y - 1,opponent):
        setPossible(pos_x, pos_y - 1, curColor, array)
        movePossible = movePossible + 128
    return movePossible

def moveCavalier(pos_x, pos_y, array=possible):
    curColor = getPion(pos_x, pos_y)
    if (getPion(pos_x - 1, pos_y - 2) != None):
        setPossible(pos_x - 1, pos_y - 2, curColor, array)
    if (getPion(pos_x + 1, pos_y - 2) != None):
        setPossible(pos_x + 1, pos_y - 2, curColor, array)
    if (getPion(pos_x - 1, pos_y + 2) != None):
        setPossible(pos_x - 1, pos_y + 2, curColor, array)
    if (getPion(pos_x + 1, pos_y + 2) != None):
        setPossible(pos_x + 1, pos_y + 2, curColor, array)
    if (getPion(pos_x - 2, pos_y - 1) != None):
        setPossible(pos_x - 2, pos_y - 1, curColor, array)
    if (getPion(pos_x - 2, pos_y + 1) != None):
        setPossible(pos_x - 2, pos_y + 1, curColor, array)
    if (getPion(pos_x + 2, pos_y - 1) != None):
        setPossible(pos_x + 2, pos_y - 1, curColor, array)
    if (getPion(pos_x + 2, pos_y + 1) != None):
        setPossible(pos_x + 2, pos_y + 1, curColor, array)

def moveTour(pos_x, pos_y, array=possible):
    curColor = getPion(pos_x, pos_y)
    curX = pos_x + 1
    curY = pos_y
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX + 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x - 1
    curY = pos_y
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX - 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x
    curY = pos_y + 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curY = curY + 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x
    curY = pos_y - 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curY = curY - 1
    setPossible(curX, curY, curColor, array)

def moveFou(pos_x, pos_y, array=possible):
    curColor = getPion(pos_x, pos_y)
    curX = pos_x + 1
    curY = pos_y + 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX + 1
       curY = curY + 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x - 1
    curY = pos_y - 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX - 1
       curY = curY - 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x - 1
    curY = pos_y + 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX - 1
       curY = curY + 1
    setPossible(curX, curY, curColor, array)
    curX = pos_x + 1
    curY = pos_y - 1
    while (getPion(curX, curY) != None and getPion(curX, curY) == 0):
       setPossible(curX, curY, 0, array)
       curX = curX + 1
       curY = curY - 1
    setPossible(curX, curY, curColor, array)

def movePionNoir(pos_x, pos_y, array=possible):
    if getPion(pos_x, pos_y + 1) != None and getPion(pos_x, pos_y + 1) == 0:
        setPossible(pos_x, pos_y + 1, 1, array)
        if pos_y == 1:
            if isPossible(pos_x, pos_y + 1, array):
                setPossible(pos_x, pos_y + 2, 1, array)
    if getPion(pos_x-1, pos_y + 1) != None and getPion(pos_x-1, pos_y + 1) < 0:
        setPossible(pos_x-1, pos_y + 1, 0, array)
    if getPion(pos_x+1, pos_y + 1) != None and getPion(pos_x+1, pos_y + 1) < 0:
        setPossible(pos_x+1, pos_y + 1, 0, array)

def movePionBlanc(pos_x, pos_y, array=possible):
    if getPion(pos_x, pos_y - 1) != None and getPion(pos_x, pos_y - 1) == 0:
        setPossible(pos_x, pos_y - 1, -1, array)
        if pos_y == 6:
            if isPossible(pos_x, pos_y - 1, array):
                setPossible(pos_x, pos_y - 2, -1, array)
    if getPion(pos_x-1, pos_y - 1) != None and getPion(pos_x-1, pos_y - 1) > 0:
        setPossible(pos_x-1, pos_y - 1, 0, array)
    if getPion(pos_x+1, pos_y - 1) != None and getPion(pos_x+1, pos_y - 1) > 0:
        setPossible(pos_x+1, pos_y - 1, 0, array)

def checkMat():
    print ("Call checkMat")
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if (pion == 5 and curPlayer == -1) or (pion == -5 and curPlayer == 1):
                roi_X = X
                roi_Y = Y
                posPion = set()
                moveRoi(X, Y, posPion)
                for (posRoiX, posRoiY) in posPion:
                    print ("a - position moved : " + str(posRoiX) + "/" + str(posRoiY))
                    oldValue = tableau[posRoiY][posRoiX]
                    tableau[posRoiY][posRoiX] = pion
                    tableau[Y][X] = 0
                    # compute Possible
                    resetPossible(possibleBlanc)
                    resetPossible(possibleNoir)
                    computePossible()
                    tableau[Y][X] = pion
                    tableau[posRoiY][posRoiX] = oldValue

                    # TODO Finish the check for the Mat
                    if curPlayer == 1 and not isPossible(posRoiX, posRoiY, possibleNoir):
                        print ("False - 1a")
                        return False
                    if curPlayer == -1 and not isPossible(posRoiX, posRoiY, possibleBlanc):
                        for (a,b) in possibleNoir:
                           print ("N : " + str(a) + "/" + str(b))
                        for (a,b) in possibleBlanc:
                           print ("B : " + str(a) + "/" + str(b))
                        print ("False - 1b")                        
                        return False
                
    # Check if by moving a piece, there is still mat position
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if (pion * curPlayer) < 0:
                print ("2 - Check : " + str(X) + "/" + str(Y))
                posPion = set()
                if abs(pion) == 2:
                    moveCavalier(X, Y, posPion)
                if abs(pion) == 1:
                    moveTour(X, Y, posPion)
                if abs(pion) == 3:
                    moveFou(X, Y, posPion)
                if abs(pion) == 4:
                    moveFou(X, Y, posPion)
                    moveTour(X, Y, posPion)
                if pion == -6:
                    movePionBlanc(X, Y, posPion)
                if pion == 6:
                    movePionNoir(X, Y, posPion)
                for (posPion_X, posPion_Y) in posPion:
                    print ("b - position moved : " + str(posPion_X) + "/" + str(posPion_Y))
                    oldValue = tableau[posPion_Y][posPion_X]
                    tableau[posPion_Y][posPion_X] = pion
                    tableau[Y][X] = 0
                    # compute Possible
                    resetPossible(possibleBlanc)
                    resetPossible(possibleNoir)
                    computePossible()
                    tableau[Y][X] = pion
                    tableau[posPion_Y][posPion_X] = oldValue

                    # TODO Finish the check for the Mat
                    if curPlayer == 1 and not isPossible(roi_X, roi_Y, possibleNoir):
                        print ("False - 2")
                        return False
                    if curPlayer == -1 and not isPossible(roi_X, roi_Y, possibleBlanc):
                        print ("False - 3")                        
                        return False
    return True
    
def checkEchec():
    resetPossible(possibleBlanc)
    resetPossible(possibleNoir)
    computePossible()
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if (pion == 5 and isPossible(X, Y, possibleBlanc) == 1):
                return 1
            if (pion == -5 and isPossible(X, Y, possibleNoir) == 1):
                return -1
    return 0

def button1(event):
    global selected
    global init_x
    global init_y
    global selectedPion
    global curPlayer
    pos_x = int((event.x - 10) / 40)
    pos_y = int((event.y - 10) / 40)
    if selected == False:
        selected = True
        resetPossible()
        pion = getPion(pos_x, pos_y)
        if pion * curPlayer > 0:
            selected = True
            selectedPion = pion
            init_x = pos_x
            init_y = pos_y
            if abs(pion) == 2:
                moveCavalier(pos_x, pos_y)
            if abs(pion) == 1:
                moveTour(pos_x, pos_y)
            if abs(pion) == 3:
                moveFou(pos_x, pos_y)
            if abs(pion) == 4:
                moveFou(pos_x, pos_y)
                moveTour(pos_x, pos_y)
            if abs(pion) == 5:
                moveRoi(pos_x, pos_y)
            if pion == -6:
                movePionBlanc(pos_x, pos_y)
            if pion == 6:
                movePionNoir(pos_x, pos_y)
    else:
        selected = False
        if isPossible(pos_x, pos_y):
            tableau[pos_y][pos_x]=selectedPion
            tableau[init_y][init_x]=0
            echec = checkEchec()
            if (echec == curPlayer):
                showEchec()
                tableau[pos_y][pos_x]=0
                tableau[init_y][init_x]=selectedPion
            elif (echec == (-1 * curPlayer)):
                if (checkMat()):
                    showEchecEtMat()
                else :
                    showEchec()
                curPlayer = curPlayer * (-1)
            else:
                curPlayer = curPlayer * (-1)
        computePossible()
        resetPossible()
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
                if (isPossible(X, Y, possibleNoir)):
                    canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 30 + 40 * X, 50 + 40 * Y, fill='green')
            if (blancsCB.get() == 1):
                if (isPossible(X, Y, possibleBlanc)):
                    canvas.create_rectangle(30 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='yellow')
            if (isPossible(X, Y, possible)):
                canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='red')
            pion=None
            if (tableau[Y][X] == 1):
                pion=tour_n
            elif (tableau[Y][X] == 2):
                pion=cavalier_n
            elif (tableau[Y][X] == 3):
                pion=fou_n
            elif (tableau[Y][X] == 4):
                pion=reine_n
            elif (tableau[Y][X] == 5):
                pion=roi_n
            elif (tableau[Y][X] == 6):
                pion=pion_n
            elif (tableau[Y][X] == -1):
                pion=tour_b
            elif (tableau[Y][X] == -2):
                pion=cavalier_b
            elif (tableau[Y][X] == -3):
                pion=fou_b
            elif (tableau[Y][X] == -4):
                pion=reine_b
            elif (tableau[Y][X] == -5):
                pion=roi_b
            elif (tableau[Y][X] == -6):
                pion=pion_b
            canvas.create_image(10 + 40 * X, 10 + 40 * Y, anchor=NW, image=pion)

fenetre = Tk()

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
