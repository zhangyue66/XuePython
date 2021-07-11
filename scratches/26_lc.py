class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        else:
            k = 1
            for i in range(len(nums)-1):
                if nums[i] != nums[i+1]:
                    nums[k] = nums[i+1]

                    k += 1


            return k





yz = Solution()

arr = [0,0,1,1,1,2,2,3,3,99]

loop = yz.removeDuplicates(arr)

print(loop)

print(arr[:(loop)])


