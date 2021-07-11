class Solution:
    def exist(self, board, word):
        if board is None:
            return False
        else:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    answer = self.dfs(board,i,j,word)
                    if answer is True:
                        return True
            return False


    def dfs(self,board,i,j,word):
        if len(word) == 0:
            return True
        else:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            elif word[0] != board[i][j]:
                return False
            else:
                yz = board[i][j]
                board[i][j] = " "

                res = self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j+1,word[1:])\
                or self.dfs(board,i,j-1,word[1:])

                board[i][j] = yz
                return res







yz = Solution()

board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]


word = "YZ"


print(yz.exist(board,word))