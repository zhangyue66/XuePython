class Solution:
    def minScoreTriangulation(self, A):





        def helper(A):
            if len(A) < 3:
                return

            if len(A) == 3:
                return A[0]*A[1]*A[2]
            else:
                for K in range(2,len(A)):
                    a= helper(A[1:K])
                    b= helper(A[K+1:len(A)-1])
                    return min(a,b)


        yz = helper(A)

        return yz


yz = Solution()
A = [1,2,3,4]
print(yz.minScoreTriangulation(A))