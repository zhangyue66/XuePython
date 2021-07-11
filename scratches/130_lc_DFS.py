# class Solution:
#     def solve(self, board) -> None:
#         m = len(board)
#         if m ==0:
#             return
#         n = len(board[0])
#
#
#         def dfs(x,y):
#             if x < 0 or x >= n or y < 0 or y >= m or board[y][x] != "O":
#                 return
#             board[y][x] = "G"
#             dfs(x-1,y)
#             dfs(x+1,y)
#             dfs(x,y-1)
#             dfs(x,y+1)
#
#         for y in range(m):
#             dfs(0,y)
#             dfs(n-1,y)
#
#         for x in range(n):
#             dfs(x,0)
#             dfs(x,m-1)
#
#         for y in range(m):
#             for x in range(n):
#                 if board[y][x] == "G":
#                     board[y][x] = "O"
#                 else:
#                     board[y][x] = "X"

class Solution:
    def solve(self, board) -> None:
        m = len(board)
        if m ==0:
            return
        n = len(board[0])

        #first see how many "O" in boarder
        for i in range(n):
            if board[0][i] == "O" :
                board[0][i] == "G"
            if board[m-1][i] == "O":
                board[m-1][i] == "G"

        for j in range(m):
            if board[j][0] == "O":
                board[j][0] == "G"
            if board[j][-1] == "O":
                board[j][-1] == "G"

        def dfs(x,y) :
            if x < 0 or x >= n or y < 0 or y >= m :
                 return
            if board[y][x] == "G":
                return True

            if dfs(x-1,y) or dfs(x+1,y) or dfs(x,y-1) or dfs(x,y+1):
                return True

        for i in range(m):
            for j in range(n):
                if dfs(j,i):
                    board[j][i] == "O"
                else:
                    board[j][i] == "X"






