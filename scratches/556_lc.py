class Solution:
    def matrixReshape(self, nums, r, c):
        valid_cnt = r*c
        root_row = len(nums)
        root_col = len(nums[0])

        if valid_cnt != root_col*root_row:
            return nums
        else:
            queue = []

            for i in range(root_row):
                for j in range(root_col):
                    queue.append(nums[i][j])

            new_matrix = []

            for i in range(r):
                a=[]
                for j in range(c):
                    a.append(queue.pop(0))
                new_matrix.append(a)

            return new_matrix

yz = Solution()
nums = [[1,2],[3,4]]
r = 1

c = 4
print(yz.matrixReshape(nums,r,c))


