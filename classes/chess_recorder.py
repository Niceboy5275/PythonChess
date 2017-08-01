class recorder:

    def __init__(self):
        self._moves=[]

    def addMove(self, move=[]):
        self._moves.append(move)

    def getLastMove(self):
        if len(self._moves) > 0:
            return self._moves.pop()
        else:
            return None

    def printMoves(self):
        for move in self._moves:
            print ("+++++++++")
            for piece in move:
                print(piece)

    def prettyPrintMoves(self):
        for move in self._moves:
            print(self.prettyPrint(move[0]) + "-" + self.prettyPrint(move[1]))

    def prettyPrint(self, piece):
        return str(chr(ord('a') + piece[0]) + str(8 - piece[1]))
