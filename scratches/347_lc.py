class Solution:
    def topKFrequent(self, nums,k):
        if len(nums) == 0 :
            return []
        else:
            ans = []
            dict = {}
            freq = []

            for i in range(len(nums)):
                if nums[i] not in dict:

                    dict[nums[i]] = 1
                else:
                    dict[nums[i]] += 1

            for key,value in dict.items():
                freq.append(value)
            freq.sort()
            arrs = freq[::-1][:k]

            for key,value in dict.items():
                if value in arrs:
                    ans.append(key)


            return ans








yz = Solution()
nums = [1,2]
k = 2
print(yz.topKFrequent(nums,k))