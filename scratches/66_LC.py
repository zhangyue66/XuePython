class Solution:
    def plusOne(self,digits):
        # i = len(digits)
        # digits[i-1] += 1
        # if digits[i-1] // 10 != 0 and digits[i-1] > 0:
        #     digits[i-1] = digits[i-1] % 10
        #     digits[i-2] += 1
        #
        # return digits
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if (length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits


yz = Solution()
digits = [1,2]
print(yz.plusOne(digits))