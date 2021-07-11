class Solution:
    def longestSubarray(self, nums, limit: int):
        res = 0
        l = 0
        r = len(nums)

        while l < r :
            big = max(nums[l:r])
            small = min(nums[l:r])

            if big - small <= limit:
                res = max(r-l,res)

            else:
                big_index = nums[l:r].index(big)
                small_index = nums[l:r].index(small)

                l = small_index
                r = big_index

        return res


yz = Solution()
nums = [8,2,4,7]
limit = 4
print(yz.longestSubarray(nums,limit))