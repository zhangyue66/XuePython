class Solution:
    def canPartition(self,nums):
        target, n = sum(nums), len(nums)
        if target & 1: return False
        target >>= 1
        dp = [True] + [False]*target
        for num in nums:
            for j in range(target,0,-1):
                if j >= num:
                    dp[j] = dp[j] or dp[j-num]


        return dp[target]




yz = Solution()
nums = [1,2,3,4,5,6,7]
print(yz.canPartition(nums))