class Solution:
    def lengthOfLastWord(self, s):
        if s is None or s == "":
            return 0
        else:
            rev_s = s[::-1]

            i ,j= 0,0

            for i in range(len(rev_s)):
                if rev_s[i] != " ":
                    j += 1
                else:
                    if j == 0:
                        continue
                    else:
                        break

            return j



yz = Solution()

s = "Hello World123  67 "

print(yz.lengthOfLastWord(s))


