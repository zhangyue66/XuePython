class Solution:
    def countSquares(self, matrix):
        col,row = len(matrix),len(matrix[0])
        side = min(col,row)
        cnt = 0
        for i in range(side):
            has_0 = 0
            for co in range(col):
                for ro in range(row):
                    if co+i+1 <= col and ro+i+1 <= row:
                        if self.traverseMatrix(i,matrix,co,ro) == False:#has 0
                            has_0 = 1


                        if has_0 == 0:
                            cnt+=1

        return cnt

    def traverseMatrix(self,side,matrix,co,ro):
        for i in range(co,co+side):
            for j in range(ro,ro+side):
                if matrix[i][j] == 0:
                    return False

        return True

yz = Solution()
matrix = \
[
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
]
print(yz.countSquares(matrix))
