# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self,nums,k):
        for i in range(k):
            anchor = nums[len(nums)-1]
            nums.pop(len(nums)-1)
            nums.insert(0,anchor)

        return nums




nums = [1,2,3,4,5,6,7]

k = 3

yz = Solution()

print(yz.rotate(nums,k))