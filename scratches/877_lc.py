class Solution:
    def stoneGame(self, piles):
        n = len(piles)

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(0,n):
            dp[i][i] = piles[i]

        for length in range(2,n+1):#length of subarray
            for i in range(n-length+1):
                j = length+i-1
                dp[i][j] = max(piles[i]-dp[i+1][j],piles[j]-dp[i][j-1])

        return dp[0][n-1]>=0



yz = Solution()
piles = [5,3,4,5,100,1]
print(yz.stoneGame(piles))