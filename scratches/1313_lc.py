class Solution:
    def decompressRLElist(self, nums):
        freqs = []
        vals = []

        for i in range(len(nums)):
            if i % 2 == 0 :
                freqs.append(nums[i])
            elif i % 2 == 1:
                vals.append(nums[i])
        ans = []

        for i in range(len(vals)):
            ans += freqs[i] *[vals[i]]

        return ans



yz = Solution()

nums = [1,2,3,4]

print(yz.decompressRLElist(nums))