class Solution:
    def findDisappearedNumbers(self,nums):
        n = len(nums)+1
        a = set([i for i in range(1,n)])
        b = set(nums)
        return list(a-b)



yz = Solution()
nums = []
print(yz.findDisappearedNumbers(nums))
