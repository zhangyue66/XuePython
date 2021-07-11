import math

class Solution:
    def isPowerOfThree(self, n):
        a = math.log(n,3)

        if type(a) != int:
            return a
        else:
            return a


yz = Solution()

n = 9

print(yz.isPowerOfThree(n))