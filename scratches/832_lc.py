class Solution:
    def flipAndInvertImage(self, A):
        ans = [[0 for j in range(len(A[0]))] for i in range(len(A))]

        for i in range(len(A)):
            k = 0
            for j in range(len(A[0])-1,-1,-1):
                yz = A[i][j]
                if yz ==1:
                    yz = 0
                elif yz == 0:
                    yz = 1
                ans[i][k] = yz
                k+=1


        return ans

yz = Solution()

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

print(yz.flipAndInvertImage(A))