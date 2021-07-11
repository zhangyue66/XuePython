class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

nums = [2,7,9,3,1]
yz = Solution()
print(yz.rob(nums))