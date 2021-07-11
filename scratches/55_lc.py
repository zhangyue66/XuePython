class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #bottom up DP solution o(n**2）
        ans = [False]*len(nums)

        n = len(nums)-1 #last index
        ans[0] = True
        for i in range(len(nums)):
            if ans[i] == True:
                last = min(n,i+nums[i])
                for j in range(i,last+1):
                    if ans[j] == True:
                        continue
                    else:
                        ans[j] = True


        return ans[-1] == True