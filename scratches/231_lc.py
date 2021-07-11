class Solution:
    def isPowerOfTwo(self, n):
        if n < 1:
            return False

        else:
            return True if (n & n-1) == 0 else False




yz = Solution()

n = 218

print(yz.isPowerOfTwo(n))