class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        else:
            counter =1
            answer = []
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    counter +=1
                else:
                    answer.append(counter)
                    counter = 1

                answer.append(counter)
            #print(answer)

            return max(answer)


yz = Solution()

nums = [1,6]

print(yz.findLengthOfLCIS(nums))