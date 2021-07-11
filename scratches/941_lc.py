class Solution:
    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        elif A[1] < A[0]:
            return False
        elif A[-1] > A[-2]:
            return False
        else:
            yz = False

            for i in range(len(A)-1):
                if A[i] == A[i+1]:
                    return False
                else:
                    if A[i] > A[i+1]:
                        if yz == True:
                            return False
                    elif A[i] < A[i+1]:
                        if yz == False:
                            yz = True

            return yz





yz = Solution()
A = [3,7,6,4,3,0,1,0]
print(yz.validMountainArray(A))