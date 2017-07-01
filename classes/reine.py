from piece import piece
from tkinter import *

class reine(piece):

    def move(self, pos_x, pos_y, tableau, array):
        curColor = tableau.getPion(pos_x, pos_y).getColor()
        curX = pos_x + 1
        curY = pos_y + 1
        while (tableau.getPion(curX, curY) == None and curX <= 7 and curY <= 7):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX + 1
           curY = curY + 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x - 1
        curY = pos_y - 1
        while (tableau.getPion(curX, curY) == None and curX >= 0 and curY >= 0):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX - 1
           curY = curY - 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x - 1
        curY = pos_y + 1
        while (tableau.getPion(curX, curY) == None and curX >= 0 and curY <= 7):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX - 1
           curY = curY + 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x + 1
        curY = pos_y - 1
        while (tableau.getPion(curX, curY) == None and curX <= 7 and curY >= 0):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX + 1
           curY = curY - 1
        tableau.setPossible(curX, curY, curColor, array)

        curX = pos_x + 1
        curY = pos_y
        while (tableau.getPion(curX, curY) == None and curX <= 7):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX + 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x - 1
        curY = pos_y
        while (tableau.getPion(curX, curY) == None and curX >=0):
           tableau.setPossible(curX, curY, 0, array)
           curX = curX - 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x
        curY = pos_y + 1
        while (tableau.getPion(curX, curY) == None and curY <= 7):
           tableau.setPossible(curX, curY, 0, array)
           curY = curY + 1
        tableau.setPossible(curX, curY, curColor, array)
        curX = pos_x
        curY = pos_y - 1
        while (tableau.getPion(curX, curY) == None and curY >= 0):
           tableau.setPossible(curX, curY, 0, array)
           curY = curY - 1
        tableau.setPossible(curX, curY, curColor, array)

    def getLetter(self):
        return "Q"

    def getImage(self):
        if self.getColor() == piece._players['NOIR']:
            return PhotoImage(file="reine_n.png")
        else:
            return PhotoImage(file="reine_b.png")
