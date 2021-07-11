class Solution:
    def missingNumber(self,nums):
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        else:
            for i in range(len(nums)-1):
                if nums[i]+1 != nums[i+1]:
                    return nums[i]+1






nums = [9,6,4,2,3,5,7,0,1]
#nums = [1]

yz = Solution()
print(yz.missingNumber(nums))