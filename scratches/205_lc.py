class Solution:
    def isIsomorphic(self, s: str, t: str):
        dic = {}
        for i in range(len(s)):
            validate = dic.values()
            if s[i] not in dic and t[i] not in validate:
                dic[s[i]] = t[i]
            elif s[i] not in dic and t[i]  in validate:
                return False
            elif s[i] in dic:
                if dic[s[i]] != t[i] :
                    return False


        return True

s = "paper"

t = "title"

yz = Solution()

print(yz.isIsomorphic(s,t))

