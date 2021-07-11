class Solution:
    def checkRecord(self, s: str):
        if len(s) == 0:
            return False
        else:
            cnt = 0
            for i in range(len(s)):
                if s[i] == 'A':
                    cnt += 1

            if cnt > 1:
                return False
            else:
                if "LLL" in s:
                    return False
                else:
                    return True




yz = Solution()

s = "PPALLL"

print(yz.checkRecord(s))