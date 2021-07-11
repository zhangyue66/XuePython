class Solution:
    def shuffle(self, nums, n):
        if len(nums) == 0:
            return []
        else:
            res = []
            n  = len(nums) // 2

            for i in range(n):
                res.append(nums[i])
                res.append(nums[i+n])

            return res



yz = Solution()
nums = [2,5,1,3,4,7]
n = 3
print(yz.shuffle(nums,n))