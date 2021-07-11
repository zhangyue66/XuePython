class Solution:
    def countNumbersWithUniqueDigits(self, n):
        choices = [9,9,8,7,6,5,4,3,2,1]
        ans,product = 1,1

        for i in range(n if n <=10 else 10):
            product *= choices[i]
            ans += product

        return ans


yz = Solution()
n = 2
print(yz.countNumbersWithUniqueDigits(n))