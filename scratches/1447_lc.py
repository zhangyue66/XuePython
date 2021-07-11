class Solution:
    def simplifiedFractions(self, n: int):
        ans = []
        if n == 1:
            return ans
        def gcd(x,y) :
            while y != 0 :
                x , y = y , x % y

            return x

        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(j,i) == 1:
                    ans.append(str(j) + "/" + str(i))

        return ans


yz = Solution()
n = 4
print(yz.simplifiedFractions(n))