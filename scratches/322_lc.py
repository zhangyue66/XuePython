class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf")]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if amount-coin >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)

        #print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1




yz = Solution()
coins = [2,5]
amount = 3
print(yz.coinChange(coins,amount))