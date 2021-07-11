class Solution:
    def numSubarrayBoundedMax(self, A, L: int, R: int):
        res,dp = 0,0
        prev = -1

        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R :
                #res += dp
                prev = i
                dp = 0
            if A[i] >= L and A[i] <= R:
                dp = i - prev
                res += dp

        return res

yz = Solution()
A = [2, 1, 4, 3]
L = 2
R = 3
print(yz.numSubarrayBoundedMax(A,L,R))