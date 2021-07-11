class Solution:
    def maxProfit(self, prices):
        if len(prices)<=1:
            return 0
        else:
            max_profit = 0

            for i in range(len(prices)-1):
                if prices[i+1] > prices[i]:
                    max_profit += prices[i+1]-prices[i]
            return max_profit


#prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]


yz = Solution()

print(yz.maxProfit(prices))

