from chessmoves import *
import pprint
class Chessgame:
    def __init__(self):
        self.funtions = PiceMoves()
    def setup(self):
        ''''
        self.bord = [
            ["br0", "bn0", "bb0", "bq0", "bk0", "bb0", "bn0", "br0"],
            ["bp0", "bp0", "bp0", "bp0", "bp0", "bp0", "bp0", "bp0"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["wp0", "wp0", "wp0", "wp0", "wp0", "wp0", "wp0", "wp0"],
            ["wr0", "wn0", "wb0", "wq0", "wk0", "wb0", "wn0", "wr0"]
        ]     '''
        
        self.bord = [
            ["br0", "bn0", "bb0", "bq0", "bk0", "bb0", "bn0", "br0"],
            ["bp0", "bp0", "bp0", "bp0", "bp0", "bp0", "000", "bp0"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["000", "000", "000", "000", "000", "000", "000", "000"],
            ["wp0", "000", "000", "wr0", "000", "bb0", "bp0", "000"],
            ["000", "000", "bp0", "000", "000", "000", "000", "000"],
            ["000", "wp0", "wp0", "000", "000", "wp0", "wp0", "wp0"],
            ["wr0", "000", "wb0", "wq0", "wk0", "wb0", "000", "wr0"]
        ] 
        pprint.pprint(self.bord)
    def readInput(self, prompt):
        self.inputt = str(input(prompt))
        return(self.inputt)
    def wereToMove(self, x, y):
        self.picetype = self.bord[y][x][1]
        self.canMove = []
        if self.picetype == 'r':
            self.canMove = self.funtions.moveRook(x,y,self.bord)
        elif self.picetype == 'k':
            self.canMove = self.funtions.moveKing(x,y,self.bord)
        elif self.picetype == 'n':
            self.canMove = self.funtions.moveKnight(x,y,self.bord)
        elif self.picetype == 'b':
            self.canMove = self.funtions.moveBishops(x,y,self.bord)
        elif self.picetype == 'q':
            self.canMove = self.funtions.moveQueen(x,y,self.bord)
        elif self.picetype == 'p':
            self.canMove = self.funtions.movePawn(x,y,self.bord)
        pprint.pprint(self.canMove)
        
    def movethere(self, x, y, newX, newY):
        self.picce = self.bord[y][x]
        self.bord[y][x] = 'xxx'
        self.bord[newY][newX] = self.picce
        