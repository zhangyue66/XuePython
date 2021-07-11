class Solution:
    def countSegments(self, s: str):
        if len(s) == 0 :
            return 0
        else:
            cnt = 0
            for i in range(len(s)):
                if i <= len(s)-2:
                    if s[i] != " " and s[i+1] == " ":
                        cnt += 1
                else:
                    if s[i] != " " and s[i-1] != " ":
                        cnt += 1
            return cnt




s = "Hello, my name is John"

yz = Solution()

print(yz.countSegments(s))