class Solution:
    def divide(self, dividend, divisor):
        neg = ((dividend<0) != (divisor <0))

        res = 0

        while dividend >= divisor:
            temp = divisor
            multi = 1

            while dividend >= temp :
                dividend -= temp
                res += multi
                multi <<= 1
                temp <<= 1

        print(neg)


dividend = 19
divisor = -3

yz = Solution()

print(yz.divide(dividend,divisor))
