class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0:
            return False
        # abs(i-j) <= k
        #abs(nums[i]-nums[j)<= t
        #use bucket idea
        min_num = min(nums)
        max_num = max(nums)
        bucket_cnt = (max_num-min_num)//(t+1)
        bucket = [0]*bucket_cnt

        dict = {}

        for i in range(len(nums)):
            bucket_index = (nums[i]-min_num)//(t+1)

            #check left adjecent bucket
            left = dict.get(bucket_index-1)
            if left != None and abs(nums[i]-left)<=t:
                return True
            #check right adjecent bucket
            right = dict.get(bucket_index+1)
            if right != None and abs(nums[i]-right) <= t:
                return True
            #check in same bucket
            if bucket_index in dict:
                return True
            dict[bucket_index] = nums[i]
            if i >= k:
                del dict[nums[i-k]//(t+1)]


        return False



yz = Solution()
nums = [1,2,3,1]
k = 3
t = 1
print(yz.containsNearbyAlmostDuplicate(nums,k,t))