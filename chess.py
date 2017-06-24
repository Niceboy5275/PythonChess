from tkinter import * 

tableau = [[1,2,3,4,5,3,2,1],
           [6,6,6,6,6,6,6,6],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [-6,-6,-6,-6,-6,-6,-6,-6],
           [-1,-2,-3,-4,-5,-3,-2,-1]]

possible= [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]

possibleBlanc= [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]

possibleNoir= [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]

def resetPossible(array=possible):
    for X in range(0, 8):
        for Y in range(0, 8):
            array[X][Y] = 0

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
    if (getPion(pos_x, pos_y) != None and getPion(pos_x, pos_y) * color <= 0):
        array[pos_y][pos_x] = 1

def isPossible(pos_x, pos_y, array=possible):
    return array[pos_y][pos_x] == 1

def moveRoi(pos_x, pos_y, array=possible):
    pos=set()
    curColor = getPion(pos_x, pos_y)
    if (getPion(pos_x - 1, pos_y - 1) != None):
        pos.add((pos_x - 1, pos_y - 1))
        setPossible(pos_x - 1, pos_y - 1, curColor, array)
        isPossible = True
    if (getPion(pos_x - 1, pos_y) != None):
        pos.add((pos_x - 1, pos_y))
        setPossible(pos_x - 1, pos_y, curColor, array)
        isPossible = True
    if (getPion(pos_x - 1, pos_y + 1) != None):
        pos.add((pos_x - 1, pos_y + 1))        
        setPossible(pos_x - 1, pos_y + 1, curColor, array)
        isPossible = True
    if (getPion(pos_x, pos_y + 1) != None):
        pos.add((pos_x, pos_y + 1))        
        setPossible(pos_x, pos_y + 1, curColor, array)
        isPossible = True
    if (getPion(pos_x + 1, pos_y + 1) != None):
        pos.add((pos_x + 1, pos_y + 1))        
        setPossible(pos_x + 1, pos_y + 1, curColor, array)
        isPossible = True
    if (getPion(pos_x + 1, pos_y) != None):
        pos.add((pos_x + 1, pos_y))        
        setPossible(pos_x + 1, pos_y, curColor, array)
        isPossible = True
    if (getPion(pos_x + 1, pos_y - 1) != None):
        pos.add((pos_x + 1, pos_y - 1))        
        setPossible(pos_x + 1, pos_y - 1, curColor, array)
        isPossible = True
    if (getPion(pos_x, pos_y - 1) != None):
        pos.add((pos_x, pos_y - 1))        
        setPossible(pos_x, pos_y - 1, curColor, array)
        isPossible = True
    return pos

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

def checkMat(pos_x, pos_y, color):
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if pion == 5 and curColor == -1:
                if (len(moveRoi(X, Y)) != 0):
                    return False
            if pion == -5 and curColor == 1:
                if (len(moveRoi(X, Y)) != 0):
                    return False
    return True
    
def checkEchec():
    resetPossible(possibleBlanc)
    resetPossible(possibleNoir)
    computePossible()
    for X in range(0, 8):
        for Y in range(0, 8):
            pion = getPion(X, Y)
            if pion == 5 and isPossible(X, Y, possibleBlanc) == 1:
                return 1
            if pion == -5 and isPossible(X, Y, possibleNoir) == 1:
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
                showEchec()
                if (checkMat()):
                    showEchecEtMat()
                curPlayer = curPlayer * (-1)
                if curPlayer == 1:
                    curPlayerName.set("Joueur noir")
                else:
                    curPlayerName.set("Joueur blanc")                
            else:
                curPlayer = curPlayer * (-1)
                if curPlayer == 1:
                    curPlayerName.set("Joueur noir")
                else:
                    curPlayerName.set("Joueur blanc")
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
    for X in range(0,8):
        for Y in range(0,8):
            if ((X+Y) % 2 == 0):
                color = 'white'
            else:
                color = 'grey'
            canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill=color)
            if (noirsCB.get() == 1):
                if (possibleNoir[Y][X] == 1):
                    canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 30 + 40 * X, 50 + 40 * Y, fill='green')
            if (blancsCB.get() == 1):
                if (possibleBlanc[Y][X] == 1):
                    canvas.create_rectangle(30 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='yellow')
            if (possible[Y][X] == 1):
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
