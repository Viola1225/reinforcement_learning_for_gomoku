import numpy as np

# game = gomoku()
# game.first([i,j])
#
#
class gomoku(object):
    def __init__(self):
        self.board = np.array([[0]*15]*15)
        self.winner = None
        self.turn = 1


    #the first player
    def first(self,pt):
        if self.winner == None and self.turn == 1:
            if self.board[pt[0],pt[1]]==0:
                self.board[pt[0],pt[1]] = 1
            self.check(pt,1)
        self.turn = -1
        print(self.board)
        
    #the second player
    def second(self,pt):
        if self.winner == None and self.turn == -1:
            if self.board[pt[0],pt[1]]==0:
                self.board[pt[0],pt[1]] = -1
            self.check(pt,-1)
        self.turn = 1
        print(self.board)

    #check if the current play wins
    def check(self,pt, sign):
        low = min(5,14-pt[0])
        up = min(pt[0],5)
        right = min(14-pt[1],5)
        left = max(pt[1],5)
        low_left = min(left,low)
        low_right = min(low,right)
        up_left = min(up,left)
        up_right = min(up,right)
        rows = [[],[],[],[]]
        goal = [sign]*5
        for i in range(-up,low+1):
            rows[0].append(self.board[pt[0]+i,pt[1]])
        for i in range(-left,right+1):
            rows[1].append(self.board[pt[0],pt[1]+i])
        for i in range(-low_left,up_right+1):
            rows[2].append(self.board[pt[0]-i,pt[1]+i])
        for i in range(-up_left,low_right+1):
            rows[3].append(self.board[pt[0]+i,pt[1]+i])
        for i in range(len(rows)):
            for j in range(len(rows[i])-5):
                if rows[i][j:j+5] == goal:
                    print(str(sign)+" wins.")
                    self.winner = sign
                    return 