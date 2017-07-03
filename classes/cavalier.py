from piece import piece

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
