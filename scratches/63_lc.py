class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        def path(m,n):
            if m < 0 or n < 0:
                return 0
            if obstacleGrid[m][n] == 1:
                return 0
            if ans[m][n] != "x":
                return ans[m][n]

            left_path = path(m-1,n)
            top_path = path(m,n-1)

            ans[m][n] = left_path+top_path

            return ans[m][n]

        ans =[["x" for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] =  0
        if ans[0][0] == 0:
            return 0
        else:
            ans[0][0] = 1
            path(m-1,n-1)
            return ans[-1][-1]



yz = Solution()
obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(yz.uniquePathsWithObstacles(obstacleGrid))