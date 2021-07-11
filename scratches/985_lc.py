class Solution:
    def sumEvenAfterQueries(self, A, queries):
        ans = []
        old_sum  = 0

        for i in range(len(A)):
            if A[i] % 2 == 0:
                old_sum += A[i]

        n = len(queries)

        for i in range(n):

            index = queries[i][1]
            val = queries[i][0]

            if val % 2 == 0 and A[index] %2 == 0:
                A[index] += val
                old_sum += val
                ans.append(old_sum)
            elif val % 2 ==0 and A[index] %2 !=0 :
                A[index] += val
                ans.append(old_sum)
            elif val % 2 != 0 and A[index] %2 != 0:

                old_sum += (val+A[index])
                A[index] += val
                ans.append(old_sum)
            elif val % 2 != 0 and A[index] %2 ==0:
                old_sum -= (A[index])
                A[index] += val
                ans.append(old_sum)

        return ans

yz = Solution()

A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

print(yz.sumEvenAfterQueries(A,queries))