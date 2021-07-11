class Solution:
    def search(self, nums, target: int):

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            if target >= nums[0]:
                if nums[mid] >= nums[0] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1
            elif target < nums[0]:
                if nums[mid] >= nums[0] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1




yz = Solution()
nums =[4,5,6,7,0,1,2]
target = 2
print(yz.search(nums,target))