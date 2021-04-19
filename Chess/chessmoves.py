import pprint
class PiceMoves:
    def __init__(self):
        pass
    def clearBord(self):
        self.row = []
        self.returnBord = []
        for len in range(8):
            self.row = []
            for hei in range(8):
                self.row.append('xxx')
            self.returnBord.append(self.row)      
    def moveKing(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':
            self.oppPiceColor = 'b'
        else:
            self.oppPiceColor = 'w'
        for length in range(3):
            for heihgt in range(3):
                try:
                    if bord[(y-1)+heihgt][(x-1)+length][0] == self.oppPiceColor:
                        self.returnBord[(y-1)+heihgt][(x-1)+length] = '111'
                        break
                    elif bord[(y-1)+heihgt][(x-1)+length][0] != self.pice[0]: 
                        self.returnBord[(y-1)+heihgt][(x-1)+length] = '111'
                    
                except:
                    pass
        self.returnBord[y][x] = self.pice
        
        return(self.returnBord)
    def moveKnight(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':             
            self.oppPiceColor = 'b'         
        else:             
            self.oppPiceColor = 'w'
        self.piceMoves = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]

        for j in range(len(self.piceMoves)):
            if self.piceMoves[j][1] < 0:
                if x+self.piceMoves[j][1] >= 0:     
                    try: 
                        if bord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]][0] == self.oppPiceColor:
                            self.returnBord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]] = '111'
                            break 
                        elif bord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]][0] != self.pice[0]:
                            self.returnBord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]] = '111' 
                    except: 
                        pass
            else:
                try: 
                    if bord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]][0] == self.oppPiceColor:
                        self.returnBord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]] = '111' 
                    elif bord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]][0] != self.pice[0]:
                        self.returnBord[y+self.piceMoves[j][0]][x+self.piceMoves[j][1]] = '111'  
                except: 
                    pass
        self.returnBord[y][x] = self.pice
        
        return(self.returnBord)
    def moveRook(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':             
            self.oppPiceColor = 'b'         
        else:             
            self.oppPiceColor = 'w'
        for loop2 in range(2):
            self.posOrNeg = [1,-1]
            for length in range(1,7):
                try:
                    if bord[y][x+length*self.posOrNeg[loop2]][0] == self.oppPiceColor:
                        self.returnBord[y][x+length*self.posOrNeg[loop2]] = '111'
                        break
                    elif bord[y][x+length*self.posOrNeg[loop2]][0] == self.pice[0]:
                        break
                    elif bord[y][x+length*self.posOrNeg[loop2]][0] != self.pice[0]:
                        self.returnBord[y][x+length*self.posOrNeg[loop2]] = '111'
                except:
                    pass
        for loop2 in range(2):
            self.posOrNeg = [1,-1]
            for length in range(1,7):
                try:
                    if bord[y+length*self.posOrNeg[loop2]][x][0] == self.oppPiceColor:
                        self.returnBord[y+length*self.posOrNeg[loop2]][x] = '111'
                        break
                    elif bord[y+length*self.posOrNeg[loop2]][x][0] == self.pice[0]:
                        break
                    elif bord[y+length*self.posOrNeg[loop2]][x][0] != self.pice[0]:
                        self.returnBord[y+length*self.posOrNeg[loop2]][x] = '111'
                except:
                    pass
        self.returnBord[y][x] = self.pice
        
        return(self.returnBord)

    def moveBishops(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':             
            self.oppPiceColor = 'b'         
        else:             
            self.oppPiceColor = 'w'
#[y+number*self.posOrNegB[xx][0]][x+number*self.posOrNegB[xx][1]]

        for xx in range(4):
            for number in range(1,7):
                self.posOrNegB = [[1,1], [1,-1], [-1,1], [-1,-1]]
                try:
                    if number*self.posOrNegB[xx][1]+x >= 0 and number*self.posOrNegB[xx][1]+x <= 7:
                        if bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] == self.oppPiceColor:
                            self.returnBord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x] = '111'
                            break
                        elif bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] == self.pice[0]:
                            break
                        elif bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] != self.pice[0]:
                            self.returnBord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x] = '111'           
                except:
                    pass
        self.returnBord[y][x] = self.pice
        
        return(self.returnBord)
    def moveQueen(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':             
            self.oppPiceColor = 'b'         
        else:             
            self.oppPiceColor = 'w'
        for loop2 in range(2):
            self.posOrNeg = [1,-1]
            for length in range(1,7):
                try:
                    if bord[y][x+length*self.posOrNeg[loop2]][0] == self.oppPiceColor:
                        self.returnBord[y][x+length*self.posOrNeg[loop2]] = '111'
                        break
                    elif bord[y][x+length*self.posOrNeg[loop2]][0] == self.pice[0]:
                        break
                    elif bord[y][x+length*self.posOrNeg[loop2]][0] != self.pice[0]:
                        self.returnBord[y][x+length*self.posOrNeg[loop2]] = '111'
                except:
                    pass
        for loop2 in range(2):
            self.posOrNeg = [1,-1]
            for length in range(1,7):
                try:
                    if bord[y+length*self.posOrNeg[loop2]][x][0] == self.oppPiceColor:
                        self.returnBord[y+length*self.posOrNeg[loop2]][x] = '111'
                        break
                    elif bord[y+length*self.posOrNeg[loop2]][x][0] == self.pice[0]:
                        break
                    elif bord[y+length*self.posOrNeg[loop2]][x][0] != self.pice[0]:
                        self.returnBord[y+length*self.posOrNeg[loop2]][x] = '111'
                except:
                    pass

        for xx in range(4):
            for number in range(1,7):
                self.posOrNegB = [[1,1], [1,-1], [-1,1], [-1,-1]]
                try:
                    if number*self.posOrNegB[xx][1]+x >= 0 and number*self.posOrNegB[xx][1]+x <= 7:
                        if bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] == self.oppPiceColor:
                            self.returnBord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x] = '111'
                            break
                        elif bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] == self.pice[0]:
                            break
                        elif bord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x][0] != self.pice[0]:
                            self.returnBord[number*self.posOrNegB[xx][0]+y][number*self.posOrNegB[xx][1]+x] = '111'           
                except:
                    pass
        self.returnBord[y][x] = self.pice
        
        return(self.returnBord)
    def movePawn(self, x, y, bord):
        self.clearBord()
        self.pice = bord[y][x]         
        if self.pice[0] == 'w':             
            self.oppPiceColor = 'b'         
        else:             
            self.oppPiceColor = 'w'
        
        if self.pice[0] == 'w':
            if bord[y-1][x][0] == self.oppPiceColor:
                self.returnBord[y-1][x] = '111'
            elif bord[y-1][x][0] != self.pice[0]:
                self.returnBord[y-1][x] = '111'
                if bord[y][x][2] == '0':
                    self.returnBord[y-2][x] = '111'
        else:
            if bord[y+1][x][0] == self.oppPiceColor:
                self.returnBord[y+1][x] = '111'
            elif bord[y+1][x][0] != self.pice[0]:
                self.returnBord[y+1][x] = '111'
                if bord[y][x][2] == '0':
                    self.returnBord[y+2][x] = '111'
        

        self.returnBord[y][x] = self.pice
        return(self.returnBord)