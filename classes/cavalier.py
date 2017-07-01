from piece import piece
from tkinter import *

class cavalier(piece):

    def move(self, pos_x, pos_y, tableau, array):
        curColor = tableau.getPion(pos_x, pos_y).getColor()
        tableau.setPossible(pos_x - 1, pos_y - 2, curColor, array)
        tableau.setPossible(pos_x + 1, pos_y - 2, curColor, array)
        tableau.setPossible(pos_x - 1, pos_y + 2, curColor, array)
        tableau.setPossible(pos_x + 1, pos_y + 2, curColor, array)
        tableau.setPossible(pos_x - 2, pos_y - 1, curColor, array)
        tableau.setPossible(pos_x - 2, pos_y + 1, curColor, array)
        tableau.setPossible(pos_x + 2, pos_y - 1, curColor, array)
        tableau.setPossible(pos_x + 2, pos_y + 1, curColor, array)

    def getLetter(self):
        return "C"

    def getImage(self):
        if self.getColor() == piece._players['NOIR']:
            return PhotoImage(file="cavalier_n.png")
        else:
            return PhotoImage(file="cavalier_b.png")
