class Solution:
    def singleNumber(self, nums):
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key,value in freq.items():
            if value == 1:
                return key


nums = [4,1,2,1,2]

yz = Solution()


print(yz.singleNumber(nums))