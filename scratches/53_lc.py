class Solution:
    def maxSubArray(self,nums):
        states = [0 for i in range(len(nums))]
        states[0] = nums[0]
        for i in range(1,len(nums)):
            if states[i-1] < 0:
                states[i] = nums[i]
            else:
                states[i] = states[i-1]+nums[i]


        return max(states)


