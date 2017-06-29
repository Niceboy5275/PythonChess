from piece import piece
from tkinter import *

class roi(piece):
    def move(self, pos_x, pos_y, tableau, array):
        curColor = tableau.getPion(pos_x, pos_y).getColor()
        opponent = set()
        tableau.computePossible(-1 * curColor, opponent)
        if not tableau.isPossible(pos_x - 1, pos_y - 1,opponent):
            tableau.setPossible(pos_x - 1, pos_y - 1, curColor, array)
        if not tableau.isPossible(pos_x - 1, pos_y,opponent):
            tableau.setPossible(pos_x - 1, pos_y, curColor, array)
        if not tableau.isPossible(pos_x - 1, pos_y + 1,opponent):
            tableau.setPossible(pos_x - 1, pos_y + 1, curColor, array)
        if not tableau.isPossible(pos_x, pos_y + 1,opponent):
            tableau.setPossible(pos_x, pos_y + 1, curColor, array)
        if not tableau.isPossible(pos_x + 1, pos_y + 1,opponent):
            tableau.setPossible(pos_x + 1, pos_y + 1, curColor, array)
        if not tableau.isPossible(pos_x + 1, pos_y,opponent):
            tableau.setPossible(pos_x + 1, pos_y, curColor, array)
        if not tableau.isPossible(pos_x + 1, pos_y - 1,opponent):
            tableau.setPossible(pos_x + 1, pos_y - 1, curColor, array)
        if not tableau.isPossible(pos_x, pos_y - 1,opponent):
            tableau.setPossible(pos_x, pos_y - 1, curColor, array)

    def getLetter(self):
        return "K"

    def getImage(self):
        if self.getColor() == piece._players['NOIR']:
            return PhotoImage(file="roi_n.png")
        else:
            return PhotoImage(file="roi_b.png")
