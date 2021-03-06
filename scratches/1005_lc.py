class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        minus = []
        positive = []

        mini = float("inf")

        for num in A :
            mini = min(mini,num)
            if num < 0 :
                minus.append(num)
            else:
                positive.append(num)

        if len(minus) == 0:
            #meaning all number are positive
            if K % 2 == 0:
                return sum(A)
            else:
                return sum(A)-mini
        else:
            minus.sort()
            positive.sort()
            if K <= len(minus):
                i = 0
                while i != K -1:
                    minus[i] = -minus[i]
                    i +=1
                return sum(minus)+sum(positive)
            else:
                left = K - len(minus)

                if left %2 == 0:
                    return sum(positive)+abs(sum(minus))
                else:
                    for i in range(len(minus)):
                        minus[i] = -minus[i]

                    yz = min(min(minus),min(positive))
                    return sum(positive)+sum(minus) - 2*yz




yz = Solution()
A = [4,2,3]
K = 1
print(yz.largestSumAfterKNegations(A,K))