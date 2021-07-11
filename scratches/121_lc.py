class Solution:
    def maxProfit(self,prices):
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         profit = prices[j]-prices[i]
        #         if profit > 0 and profit > maxProfit:
        #             maxProfit = profit
        # return maxProfit
        max_profit = 0
        min_price = float("inf")
        for price in prices:
            min_price = min(price,min_price)
            max_profit = max(max_profit,price-min_price)

        return max_profit




prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]

yz = Solution()
print(yz.maxProfit(prices))