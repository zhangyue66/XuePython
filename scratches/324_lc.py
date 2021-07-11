class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        res = nums
        print(res)

        for i in range(0,len(nums),2):
            if len(res) != 0:
                nums[i] = res.pop(0)
        for i in range(1,len(nums),2):
            if len(res) != 0:
                nums[i] = res.pop(0)





yz = Solution()
nums = [1, 3, 2, 2, 3, 1]
#tk = [1, 3, 2, 2, 3, 1]
print(yz.wiggleSort(nums))

#print(tk[::2])
#print(tk[1::2])