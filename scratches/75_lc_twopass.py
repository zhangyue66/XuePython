class Solution:
    def sortColors(self, nums):

        dict = {0:0,1:0,2:0}

        for num in nums:
            if num == 0:
                dict[0] += 1
            elif num ==1:
                dict[1] += 1
            else:
                dict[2] += 1

        nums = [0]*dict[0]+[1]*dict[1]+[2]*dict[2]

        return nums






yz = Solution()

nums = [2,0,2,1,1,0]

print(yz.sortColors(nums))