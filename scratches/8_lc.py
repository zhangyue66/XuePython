class Solution:
    def myAtoi(self, str):
        sign = 0
        res = ""

        for element in str:
            if sign == 0 and res == "" and ord(element) ==45:
                sign =1 # minus sign
                res += "-"
            elif ord(element) in range(48,58):
                res += element


        return int(res)




yz = Solution()

str="     -142asdasd aw213125124-123123"

print(yz.myAtoi(str))