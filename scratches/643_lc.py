class Solution:
    def findMaxAverage(self, nums,k):
        n = len(nums)
        sum_list = sum(nums[:k])
        max_sum = sum_list
        for i in range(1,n-k+1):


            sum_list = sum_list - nums[i-1]+nums[i+k-1]
            max_sum = max(sum_list,max_sum)

        return max_sum/k



nums = [1,12,-5,-6,50,3]
k = 4

yz = Solution()

print(yz.findMaxAverage(nums,k))