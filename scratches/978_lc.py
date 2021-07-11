class Solution:
    def maxTurbulenceSize(self, A):
        alter = []

        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                alter.append(1)
            elif A[i] == A[i+1]:
                alter.append(0)
            else:
                alter.append(-1)

        #[1, 1, -1, 1, -1, 0, 1, -1] alter


        max_len = 1
        j = 0
        for i in range(len(alter)-1):

            if alter[i]*alter[i+1] != -1:
                yz = i-j+1
                max_len = max(max_len,yz)
                j = i+1
            if i == len(alter)-1:
                yz = i-j+1
                max_len = max(max_len,yz)

        print(alter)
        return max_len





yz = Solution()
# A = [9,4,2,10,7,8,8,1,9]
# A= [4,8,12,16]
# A= [100]
A =[0,8,45,88,48,68,28,55,17,24]
print(yz.maxTurbulenceSize(A))


