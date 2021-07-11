class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        else:

            num = 0

            while x != 0 :
                temp = x %10
                num = num*10 + temp
                x = x // 10


            if num == x :
                return True
            else:
                return False


yz = Solution()

x = 1441

print(yz.isPalindrome(x))