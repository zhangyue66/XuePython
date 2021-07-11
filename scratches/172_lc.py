class Solution:
    def trailingZeroes(self, n):
        cnt = 0
        while n != 0:
            cnt += n//5
            n = n//5

        return cnt





yz = Solution()

n = 7

print(yz.trailingZeroes(n))