from itertools import permutations,combinations,combinations_with_replacement
class Solution:
    def threeSum(self, nums):
        if len(nums)<3:
            return
        else:
            ans = []
            combs = list(combinations(nums,3))
            for comb in combs:
                if sum(comb) == 0:
                    ans.append(comb)

            res = []

            for a in ans:
                a = list(a)
                a.sort()
                if a not in res:
                    res.append(a)

            return res




yz = Solution()
nums = [13,9,1,12,-7,-12,7,3,9,6,-7,4,9,5,5,-7,4,11,1,-2,12,3,-12,-15,0,-12,-6,-1,7,-5,-4,-3,12,4,-14,-10,-1,8,1,-6,-1,9,13,-14,-1,-5,-6,-12,-8,2,2,11,13,-3,11,-2,1,-10,4,-15,-8,7,-11,11,-4,-10,-13,3,5,3,12,11,-11,2,12,3,13,13,-2,12,-7,-15,8,-9,-10,-4,-4,6,1,-15,-2,0,-1,2,-3,10,-1,-9,-10,-11,1,-13,-15,5,-3,5,-7,-5,-5,6,14,3,-1,7,1,-4,-12,12,-13,-4,4,0,3,-12,9,-15,6]
print(yz.threeSum(nums))