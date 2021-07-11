class Solution:
    def myPow(self, x, n):
        if n < 0 :
            n = -n
            x = 1/x
        ans = 1
        while n :
            if n & 1 == 1:
                ans *= x

            x *= x
            n >>= 1

        return ans







yz = Solution()
x = 2
n = 5
print(yz.myPow(x,n))

