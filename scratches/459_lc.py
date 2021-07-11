class Solution:
    def repeatedSubstringPattern(self, s: str):
        comp = ""
        for i in range(len(s)):
            comp += s[i]
            if len(comp) > len(s)//2:
                break
            elif len(s) % len(comp) != 0:
                continue
            elif comp * (len(s)//len(comp)) == s:
                return True

        return False


s = "abdcabcabcabc"

yz = Solution()

print(yz.repeatedSubstringPattern(s))



