class Solution:
    def romanToInt(self,s):
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0

        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                sum -= roman_dict[s[i]]
            else:
                sum += roman_dict[s[i]]

        sum += roman_dict[s[-1]]


        return sum


yz = Solution()

s = "MCMXCIV"

print(yz.romanToInt(s))