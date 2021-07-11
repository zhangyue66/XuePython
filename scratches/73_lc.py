class Solution:
    def setZeroes(self, matrix):
        zero_row,zero_col = False,False
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True

        for i in range(1,row):
            if matrix[i][0] == 0:
                for j in range(1,col):
                    matrix[i][j] = 0

        for j in range( 1,col):
            if matrix[0][j] == 0:
                for i in range(1,row):
                    matrix[i][j] = 0

        if zero_row:
            for j in range(col):
                matrix[0][j] = 0

        if zero_col:
            for i in range(row):
                matrix[i][0] = 0


        return matrix



yz = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(yz.setZeroes(matrix))