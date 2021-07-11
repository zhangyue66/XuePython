# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# nums = [2,7,11,15,90,91]
# target = 93

class Solution(object):
     def twoSum(self,nums,target):
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i, j]


lc_yz = Solution()

print(lc_yz.twoSum([2, 7, 11, 15],9))