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
from chess_interface import chessInterface
import queue
import time

class chess_tkinter(chessInterface):

    def __init__(self):
        self.queue = queue.Queue()
        self.queueP = queue.Queue()
        self.fenetre = Tk()
        self.pion_b=PhotoImage(file="pion_b.png")
        self.pion_n=PhotoImage(file="pion_n.png")
        self.cavalier_b=PhotoImage(file="cavalier_b.png")
        self.cavalier_n=PhotoImage(file="cavalier_n.png")
        self.roi_b=PhotoImage(file="roi_b.png")
        self.roi_n=PhotoImage(file="roi_n.png")
        self.reine_b=PhotoImage(file="reine_b.png")
        self.reine_n=PhotoImage(file="reine_n.png")
        self.fou_b=PhotoImage(file="fou_b.png")
        self.fou_n=PhotoImage(file="fou_n.png")
        self.tour_b=PhotoImage(file="tour_b.png")
        self.tour_n=PhotoImage(file="tour_n.png")

        self.menubar = Menu(self.fenetre)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.newGame)
        self.filemenu.add_command(label="Open", command=self.openFile)
        self.filemenu.add_command(label="Save", command=self.saveFile)

        self.filemenu.add_separator()
        
        self.filemenu.add_command(label="Undo", command=self.undoCommand)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Start server", command=self.startServer)
        self.filemenu.add_command(label="Stop server", command=self.stopServer)
        self.filemenu.add_command(label="Connect server", command=self.connectServer)
        self.filemenu.add_command(label="Disconnect server", command=self.disconnectServer)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.fenetre.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.fenetre.config(menu=self.menubar)
        self.fenetre.title("Echecs")
        self.canvas=Canvas(self.fenetre, width=340, height=340)
        self.canvas.grid(row=1, column = 1, columnspan=2, sticky=W)
        self.curPlayerName=StringVar()
        self.curPlayerName.set("Joueur blanc")
        self.label = Label(self.fenetre, textvariable=self.curPlayerName)
        self.label.grid(row=2, column = 1, columnspan=2, sticky=N)
        self.fenetre.bind('<Button-1>', self.button1)

    def newGame(self):
        self.queue.put(("new", ))

    def undoCommand(self):
        self.queue.put(("undo", ))

    def openFile(self):
        filename = askopenfilename(filetypes=(("Chess files", "*.chy"),
                                               ("All files", "*.*") ))
        if filename != "":
            self.queue.put(("open", filename))

    def saveFile(self):
        filename = asksaveasfilename(filetypes=(("Chess files", "*.chy"),
                                          ("All files", "*.*") ))
        if filename != "":    
            self.queue.put(("save", filename))
    
    def startCB(self, port, window):
        self.queue.put(("start_server", port))
        window.destroy()
        
    def startServer(self):
        toplevel = Toplevel()
        toplevel.title("Starting ...")
        portLabel = Label(toplevel, text="Port :")
        portLabel.grid(row=0, column = 0)
        portValue = StringVar()
        port = Entry(toplevel, textvariable=portValue)
        port.grid(row=0,column=1)
        b = Button(toplevel, text="OK", width=10, command= lambda : self.startCB(int(port.get()), toplevel))
        b.grid(row=1, column=1)

    def stopServer(self):
        self.queue.put(("stop_server", ))
        
    def connectCB(self, host, port, window):
        self.queue.put(("connect_server", host, port))
        window.destroy()
        
    def connectServer(self):
        toplevel = Toplevel()
        toplevel.title("Connecting ...")
        hostLabel = Label(toplevel, text="Host :")
        hostLabel.grid(row=0, column = 0)
        hostValue = StringVar()
        host = Entry(toplevel, textvariable=hostValue)
        host.grid(row=0, column = 1)
        portLabel = Label(toplevel, text="Port :")
        portLabel.grid(row=1, column = 0)
        portValue = StringVar()
        port = Entry(toplevel, textvariable=portValue)
        port.grid(row=1, column = 1)
        b = Button(toplevel, text="OK", width=10, command= lambda : self.connectCB(host.get(), int(port.get()), toplevel))
        b.grid(row=2, column = 1)
        
    def disconnectServer(self):
        self.queue.put(("disconnect_server", ))
        
    def showMessage(self, message):
        toplevel = Toplevel()
        toplevel.title("Warning !")
        label1 = Label(toplevel, text=message)
        label1.pack()

    def button1(self, event):
        pos_x = int((event.x - 10) / 40)
        pos_y = int((event.y - 10) / 40)
        self.queue.put(("play", pos_x, pos_y))
        
    def getPromoted(self, event):
        while True:
            pos_x = int((event.x - 10) / 40)
            if pos_x == 0:
                self.queueP.put(("promotion", "T"))
                break
            elif pos_x == 1:
                self.queueP.put(("promotion", "C"))
                break
            elif pos_x == 2:
                self.queueP.put(("promotion", "F"))
                break
            elif pos_x == 3:
                self.queueP.put(("promotion", "Q"))
                break
        self.promotion.destroy()
        
    def showPromotion(self, tableau):
        color = tableau.getCurPlayer()
        self.promotion = Toplevel()
        self.promotion.title("Promotion")
        canvas=Canvas(self.promotion, width=300, height=100)
        canvas.grid(row=1, column = 1, sticky=W)
        if (color == 1 or color == 0):
            canvas.create_image(10, 10, anchor=NW, image=self.tour_n)
            canvas.create_image(50, 10, anchor=NW, image=self.cavalier_n)
            canvas.create_image(90, 10, anchor=NW, image=self.fou_n)
            canvas.create_image(130, 10, anchor=NW, image=self.reine_n)
        if (color == -1 or color == 0):
            canvas.create_image(10, 50, anchor=NW, image=self.tour_b)
            canvas.create_image(50, 50, anchor=NW, image=self.cavalier_b)
            canvas.create_image(90, 50, anchor=NW, image=self.fou_b)
            canvas.create_image(130, 50, anchor=NW, image=self.reine_b)
        self.promotion.bind('<Button-1>', self.getPromoted)
        while True:
            self.fenetre.update()
            try:
                item = self.queueP.get(False)
                command = item[0]
                if command == "promotion":
                    piece = item[1]
                    if piece == "T":
                        tableau.setPromoted(tour.tour(color))
                        break
                    elif piece == "C":
                        tableau.setPromoted(cavalier.cavalier(color))
                        break
                    elif piece == "F":
                        tableau.setPromoted(fou.fou(color))
                        break
                    elif piece == "Q":
                        tableau.setPromoted(reine.reine(color))
                        break
                    break
            except KeyboardInterrupt:
                item = (-1,-1)
            except queue.Empty:
                time.sleep(0.3)
                continue
        
        
    def draw(self, tableau):
        if tableau.getCurPlayer() == 1:
            self.curPlayerName.set("Joueur noir")
        else:
            self.curPlayerName.set("Joueur blanc")
        for X in range(0,8):
            for Y in range(0,8):
                if ((X+Y) % 2 == 0):
                    color = 'white'
                else:
                    color = 'grey'
                self.canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill=color)
                if (tableau.isPossible(X, Y)):
                    self.canvas.create_rectangle(10 + 40 * X,10 + 40 * Y, 50 + 40 * X, 50 + 40 * Y, fill='red')
                pionV=tableau.getPion(X, Y)
                if pionV != None:
                    if type(pionV) is pion.pion and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.pion_n
                    if type(pionV) is pion.pion and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.pion_b
                    if type(pionV) is tour.tour and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.tour_n
                    if type(pionV) is tour.tour and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.tour_b
                    if type(pionV) is cavalier.cavalier and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.cavalier_n
                    if type(pionV) is cavalier.cavalier and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.cavalier_b
                    if type(pionV) is fou.fou and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.fou_n
                    if type(pionV) is fou.fou and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.fou_b
                    if type(pionV) is roi.roi and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.roi_n
                    if type(pionV) is roi.roi and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.roi_b
                    if type(pionV) is reine.reine and pionV.getColor() == piece._players['NOIR']:
                        imageP=self.reine_n
                    if type(pionV) is reine.reine and pionV.getColor() == piece._players['BLANC']:
                        imageP=self.reine_b
                    
                    self.canvas.create_image(10 + 40 * X, 10 + 40 * Y, anchor=NW, image=imageP)


    def mainLoop(self, tableau):
        while True:
            self.fenetre.update()
            try:
                item = self.queue.get(False)
                command = item[0]
                if command == "play":
                    if tableau.askForAction():
                        tableau.insertMove(item[1], item[2], tableau.getCurPlayer())
                        break
                elif command == "undo":
                    tableau.undoLastMove()
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "open":
                    tableau.openFile(item[1])
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "save":
                    tableau.saveFile(item[1])
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "new":
                    tableau.reset()
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "start_server":
                    tableau.startServer(int(item[1]))
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "stop_server":
                    tableau.stopServer()
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "connect_server":
                    tableau.startClient(item[1], int(item[2]))
                    tableau.insertMove(-2, -2, -1)
                    break
                elif command == "disconnect_server":
                    tableau.stopClient()
                    tableau.insertMove(-2, -2, -1)
                    break
            except KeyboardInterrupt:
                item = (-1,-1)
            except queue.Empty:
                time.sleep(0.3)
                continue
