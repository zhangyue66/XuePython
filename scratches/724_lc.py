class Solution:
    def pivotIndex(self, nums):
        if len(nums) == 0 :
            return -1
        elif len(nums) == 1:
            return 0
        else:
            for i in range(len(nums)):
                if i == 0 :
                    if sum(nums[1:len(nums)]) == 0:
                        return 0
                if i >= 1:
                    if sum(nums[0:i]) == sum(nums[i + 1:len(nums)]):
                        return i
                if i == len(nums)-1:
                    if sum(nums[0:len(nums)-1]) == 0:
                        return i

            return -1

nums = [-1,-1,0,1,1,0]

yz = Solution()

print(yz.pivotIndex(nums))