from piece import piece

class roi(piece):
    def move(self, pos_x, pos_y, tableau, array):
        curColor = tableau.getPion(pos_x, pos_y).getColor()
        tableau.setPossible(pos_x - 1, pos_y - 1, curColor, array)
        tableau.setPossible(pos_x - 1, pos_y, curColor, array)
        tableau.setPossible(pos_x - 1, pos_y + 1, curColor, array)
        tableau.setPossible(pos_x, pos_y + 1, curColor, array)
        tableau.setPossible(pos_x + 1, pos_y + 1, curColor, array)
        tableau.setPossible(pos_x + 1, pos_y, curColor, array)
        tableau.setPossible(pos_x + 1, pos_y - 1, curColor, array)
        tableau.setPossible(pos_x, pos_y - 1, curColor, array)
        if self == tableau._selectedPion:
            try:
                opponent = set()
                tableau.setPion(pos_x, pos_y, None, False)
                tableau.computePossible((-1) * curColor, opponent)
                tableau.setPion(pos_x, pos_y, self, False)
                for item in opponent:
                    try:
                        array.remove(item)
                    except KeyError as e:
                        continue
            except Exception as e:
                print (e)

    def checkRoque(self, tableau, array):
        #King has moved ==> Roque not possible
        leftRoque = True
        rightRoque = True
        if self.hasMoved() == True:
            return;
        if self.getColor() == piece._players['BLANC']:
            ligne = 7
        else:
            ligne = 0
        #Tours have moved ==> Roque not possible
        tourLeft=tableau.getPion(0, ligne)
        if tourLeft == None or tourLeft.getLetter() != "T" or tourLeft.hasMoved() == True:
            leftRoque = False
        tourRight=tableau.getPion(7, ligne)
        if tourRight == None or tourRight.getLetter() != "T" or tourRight.hasMoved() == True:
            rightRoque = False
        if leftRoque:
            # Check if the cases are empty
            if (tableau.getPion(1, ligne) != None):
                leftRoque = False
            if (tableau.getPion(2, ligne) != None):
                leftRoque = False
            if (tableau.getPion(3, ligne) != None):
                leftRoque = False
        if rightRoque:
            # Check if the cases are empty
            if (tableau.getPion(5, ligne) != None):
                rightRoque = False
            if (tableau.getPion(6, ligne) != None):
                rightRoque = False
        if rightRoque or leftRoque:
            opponent = set()
            tableau.computePossible(-1 * self.getColor(), opponent)
            if ((4, ligne) in opponent):
                leftRoque = False            
                rightRoque = False
            if leftRoque:
                # Check if king is in mat position
                if ((3, ligne) in opponent):
                    leftRoque = False
                if ((2, ligne) in opponent):
                    leftRoque = False
            if rightRoque:
                # Check if king is in mat position
                if ((5, ligne) in opponent):
                    rightRoque = False
                if ((6, ligne) in opponent):
                    rightRoque = False
        
        if leftRoque:
            tableau.setPossible(2, ligne, self.getColor(), array)
        if rightRoque:
            tableau.setPossible(6, ligne, self.getColor(), array)
    
    def getLetter(self):
        return "K"
