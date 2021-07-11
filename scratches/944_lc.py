class Solution:
    def minDeletionSize(self, A):
        count = 0
        for col in zip(*A):
            print(col)


yz = Solution()
A = ["zyx","wvu","tsr"]
print(yz.minDeletionSize(A))