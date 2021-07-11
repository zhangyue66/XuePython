class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        cnt = 0
        product = 1

        left = 0

        for right,v in enumerate(nums):
            product *= v
            while product >= k:
                product //= nums[left]
                left += 1
            cnt += (right-left+1)

        return cnt


yz = Solution()
nums = [10, 5, 2, 6]
k = 100
print(yz.numSubarrayProductLessThanK(nums,k))
