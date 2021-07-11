

class Solution:
    def rotate(self, matrix):

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row//2):
            for j in range(i,col-1-i):

                tmp = matrix[i][j]

                matrix[i][j] = matrix[row-1-j][i]

                matrix[row-1-j][i] = matrix[row-1-i][col-1-j]

                matrix[row-1-i][col-1-j] = matrix[j][col-1-i]

                matrix[j][col-1-i] = tmp



        return matrix


matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

yz = Solution()

print(yz.rotate(matrix))