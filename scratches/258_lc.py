class Solution:
    def addDigits(self, num):
        if num < 0:
            return 0

        else:
            result = (num-1) % 9 + 1

            return result




yz = Solution()

num = 9

print(yz.addDigits(num))