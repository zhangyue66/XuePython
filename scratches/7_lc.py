class Solution:
    def reverse(self, x: int):
        if x > 2147483647 or x < -2147483648:
            return 0
        else:
            num = 0
            # x = 321
            a = abs(x)

            while a != 0 :
                temp = a % 10
                a = a//10
                num = num * 10 + temp
                if num > 2147483647 or num < -2147483648:
                    return 0

            if x < 0 :
                 return -num
            else:
                return num







x = -123

yz = Solution()

print(yz.reverse(x))