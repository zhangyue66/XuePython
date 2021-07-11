class Solution:
    def maxProduct(self, nums):
        max_int = nums[0]
        min_int = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            tmp = max_int

            max_int = max(nums[i],max_int*nums[i],min_int*nums[i])

            min_int = max(nums[i],tmp * nums[i],min_int*nums[i])

            if max_int > res:
                res = max_int
            return res




nums = [2,3,-2,4]

yz = Solution()

print(yz.maxProduct(nums))