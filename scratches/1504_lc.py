class Solution:
    def numSubmat(self, mat):
        dp = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]

        m,n = len(mat),len(mat[0])

        for i in range(m):
            for j in range(n):
                if i == 0: #first row
                    if j == 0 :
                        dp[i][j] = mat[i][j]
                    else:

                        dp[i][j] = dp[i][j-1] +mat[i][j]

                elif j == 0: #first column
                    if i == 0:
                        continue
                    else:
                        #print(i,j)
                        dp[i][j] = dp[i-1][j] + mat[i][j]

                else:
                    if mat[i][j] ==0:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]

                    else:
                        dp[i][j] = dp[i-1][j]+dp[i][j-1]+2*(mat[i][j])


        return dp[-1][-1]




mat =  [[0,1,1,0],
        [0,1,1,1],
        [1,1,1,0]]

yz = Solution()
print(yz.numSubmat(mat))