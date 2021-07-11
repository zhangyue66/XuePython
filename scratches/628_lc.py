class Solution:
    def maximumProduct(self, nums):
        if len(nums) <= 2:
            return 0
        else:
            nums.sort()

            cana = nums[0]*nums[1]*nums[len(nums)-1]

            canb = nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]

            return max(cana,canb)





nums = [1,2,3,4,8,5]

yz = Solution()


print(yz.maximumProduct(nums))