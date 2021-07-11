class Solution:
    def lengthOfLongestSubstring(self, s: str):
        if len(s) ==0:
            return 0
        else:
            yz_set = set(s)
            #the substring can not be longer than n ( biggest is n,everytime n -= 1 if not met)
            n = len(yz_set)

            while n > 1:
                for i in range(len(s)-n+1):
                    yz = s[i:i+n]
                    #print(yz)
                    if yz in s and len(yz) == len(set(yz)):
                        return n
                n -= 1
            return 1




yz = Solution()

s = "pwwkew"

print(yz.lengthOfLongestSubstring(s))