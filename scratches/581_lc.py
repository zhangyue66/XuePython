class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)

        low ,high = 0,0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                low = i
                break

        for j in range(len(nums)-1,0,-1):
            if nums[j] != sorted_nums[j]:
                high = j
                break

        if low < high :
            return high - low+1
        else:
            return 0




nums = [1,1,1,1,1]

yz = Solution()

print(yz.findUnsortedSubarray(nums))


