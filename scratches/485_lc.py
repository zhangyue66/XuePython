class Solution:
    def findMaxConsecutiveOnes(self,nums):
        counter = 0
        cnt = 0
        for i in range(len(nums)):
            if nums[i] ==1:
                cnt +=1
                counter = max(counter,cnt)
            else:
                cnt=0

        return counter



nums = [1,0,1,1,0,1]

yz = Solution()

print(yz.findMaxConsecutiveOnes(nums))

