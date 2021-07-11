#nums = [1,3,5,6] target=2


class Solution:
    def searchInsert(self,nums,target):

        is_found = False
        while is_found is False:
            for i in range(len(nums)):
                while nums[i] >= target:
                    is_found = True
                    return i
            return len(nums)







nums =  [1,3,5,6]

target = 0


yz = Solution()

print(yz.searchInsert(nums,target))