class Solution:
    def longestPalindrome(self, s):
        dic ={}

        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1

        ans = 0
        mark = 0

        #abcba odd
        #abccba even

        for j in dic.keys():
            if dic[j]%2 == 1:
                mark += 1

            ans += dic[j] //2

        ans = ans *2 +1 if mark >0 else ans*2

        if ans > 0 :
            return ans
        else:
            if mark > 0:
                return 1
            else:
                return 0




s = "abcccdd"

yz = Solution()


print(yz.longestPalindrome(s))