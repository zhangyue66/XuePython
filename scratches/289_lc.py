class Solution:
    def gameOfLife(self, board):
        res = [[None for j in range(len(board[0]))] for i in range(len(board))]
        #create a copy of board
        for i in range(len(board)):
            for j in range(len(board[0])):
                res[i][j] = board[i][j]

        for i in range(len(res)):
            for j in range(len(res[0])):
                live_count = self.cnt(i,j,res)
                if res[i][j] == 1 and live_count< 2:
                    board[i][j] = 0
                elif res[i][j] ==1 and live_count ==2 or live_count == 3:
                    board[i][j] = 1
                elif res[i][j] ==1 and live_count> 3:
                    board[i][j] = 0
                elif res[i][j] == 0 and live_count == 3:
                    board[i][j] =1
        print(self.cnt(0,0,res))
        return board

    def cnt(self,i,j,board):
        col,row = len(board),len(board[0])
        count = 0

        if i -1 >=0 and j -1 >=0:
            if board[i-1][j-1] == 1:
                count +=1
        if i -1 >= 0 :
            if board[i-1][j] ==1 :
                count +=1
        if i -1 >= 0 and j+1 < row:
            if board[i-1][j+1] == 1:
                count += 1
        if  j-1 >= 0 :
            if board[i][j-1] == 1:
                count += 1
        if j+1 < row:
            if board[i][j+1] ==1 :
                count += 1
        if i+1 < col and j+1 < row:
            if board[i+1][j+1] ==1:
                count += 1
        if i +1 < col:
            if board[i+1][j] ==1:
                count+=1
        if i+1 < col and j-1 >= 0:
            if board[i+1][j-1] == 1:
                count += 1

        return count







yz = Solution()
board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
print(yz.gameOfLife(board))