class Solution:
    def arrayPairSum(self,nums):
        nums.sort()
        a_list = nums[::2]
        b_list = nums[1::2]
        n = len(nums)//2
        sum = 0
        for i in range(n):
            dot= min(a_list[i],b_list[i])
            sum += dot
        return sum


yz = Solution()

nums = [1,2,3,4]
nums.sort()
print(nums)
print(yz.arrayPairSum(nums))

# print(len(nums)//2)