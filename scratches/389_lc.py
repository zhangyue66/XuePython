class Solution:
    def findTheDifference(self,s,t):
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
                continue
            if s[i] in dic:
                dic[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in dic :
                return t[j]
            else:
                dic[t[j]] -= 1

                for key,value in dic.items():
                    if value == -1:
                        return key




yz = Solution()

s = "abcd"
t = "abcde"

print(yz.findTheDifference(s,t))