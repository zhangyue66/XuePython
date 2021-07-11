class Solution:
    def hammingWeight(self, n):
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                cnt +=1
            n /= 2

        return cnt

yz = Solution()
n = 111011
print(yz.hammingWeight(n))