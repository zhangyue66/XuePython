class Solution:
    def majorityElement(self, nums):
        # major_count = len(nums)/2
        #
        # for num in nums:
        #     count = 0
        #     for anchor in nums:
        #         if num == anchor:
        #             count +=1
        #         if count > major_count:
        #             return num
        #return sorted(nums)[int(len(nums)/2)]
        count = 1
        index = 0
        for i in range(1,len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
                if count == 0:
                    index = i
                    count = 1
        return nums[index]








nums = [2,2,1,1,1,2,2,8,7,5,6,4,2,3,2,1,3,4,5,3,2,3,4,3,5,3,7,3,9,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,10,99,78,2,78,9,9,9,9,9,9]
#nums = [3,2,3]

yz = Solution()
#print(int(len(nums)/2))
print(yz.majorityElement(nums))