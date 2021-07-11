class Solution:
    def thirdMax(self,nums):
        # a=b=c=-float("inf")
        #
        #
        # for num in nums:
        #     if num in [a,b,c] :
        #         continue
        #
        #     if num>a:
        #         num,a = a,num
        #     if num>b:
        #         num,b = b,num
        #     if num>c:
        #         num,c = c,num
        # if c == -float("inf"):
        #     return a
        # return c
        nums = sorted(list(set(nums)))

        if len(nums) <= 2:
            return nums[-1]
        return nums[-3]



nums = [1,2,3,4]

yz = Solution()

print(yz.thirdMax(nums))
nums.sort()

print(nums)