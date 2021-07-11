class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) == 0:
            return 0
        else:
            row = len(triangle)
            dp = [0]*(row+1)

            for i in range(row-1,-1,-1):
                for j in range(i+1):
                    dp[j] = triangle[i][j]+min(dp[j],dp[j+1])

            return dp[0]
        #dp [11, 10, 10, 3, 0]

yz = Solution()
triangle = [
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]
print(yz.minimumTotal(triangle))
