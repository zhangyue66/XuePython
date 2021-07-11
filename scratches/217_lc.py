class Solution:
    def containsDuplicate(self,nums):
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]]=1


        return False

nums = [1,2,3,5,6,3,4,5,6,7,8,9,4,3,43,43,43,223,8]

yz = Solution()

print(yz.containsDuplicate(nums))