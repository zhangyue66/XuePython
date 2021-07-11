class Solution:
    def canPartition(self, nums):
        n = len(nums)
        for i in range(1<<n):
            left,right = [],[]
            for j in range(n):
                if (i>>j)&1 == 1:
                    left.append(nums[j])
                else:
                    right.append(nums[j])

            if sum(left) == sum(right):
                return True

        return False




yz = Solution()
nums = [1,2,3,4,5,6,7]
print(yz.canPartition(nums))