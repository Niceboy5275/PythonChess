from piece import piece

class tour(piece):

    def __init__(self, color):
        super(tour, self).__init__(color)

    def move(self, pos_x, pos_y, tableau, array):
        curColor = tableau.getPion(pos_x, pos_y).getColor()
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
        return "T"
