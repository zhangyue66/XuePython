class Solution:
    def subsets(self, nums):
        self.res = []

        def backtrack(first,length,cur):
            if len(cur) == k:
                self.res.append(cur[:])
            else:
                for i in range(first,length):
                    cur.append(nums[i])
                    backtrack(i+1,length,cur)
                    cur.pop()

        length = len(nums)

        for k in range(length+1):
            backtrack(0,length,[])

        return self.res






yz = Solution()

nums = [1,2,3]
print(yz.subsets(nums))