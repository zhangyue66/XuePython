import collections

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        elif k == 0:
            dic = collections.Counter(nums)
            res = 0
            for val in dic.values():
                if val >= 2:
                    res += 1
            return res
        else:
            res = 0
            rec = set(nums)
            for key in rec:
                if key+k in rec:
                    res += 1
            return res


nums = [3,1,4,1,5,-1,-3,-5]

k = 2

yz = Solution()


print(yz.findPairs(nums,k))
print(set(nums))




