from itertools import permutations,combinations

class Solution:
    def subsets(self, nums):
        res = [[]]


        if len(nums) == 0:
            return res
        else:
            for i in range(1,len(nums)+1):

                for element in combinations(nums,i):
                    res.append(list(element))


            return res

yz = Solution()

nums = [1,2,3]

# for element in permutations(nums,2):
#     print(list(element))

print(yz.subsets(nums))


