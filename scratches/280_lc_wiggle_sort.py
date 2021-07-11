# Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]



class Solution:
    def wiggle_sort(self,nums):
        nums.sort()
        i = 1
        while i+1 < len(nums):
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i += 2

        print(nums)




yz = Solution()
nums = [3,5,2,1,6,4]
print(yz.wiggle_sort(nums))