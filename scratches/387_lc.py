class Solution:
    def firstUniqChar(self, s):
        if len(s) == 0:
            return None
        else:
            dic = {}
            for i in range(len(s)):
                if s[i] not in dic:
                    dic[s[i]] = i
                else:
                    dic[s[i]] = "yz"
            max_yz = float("inf")
            for key,value in dic.items():
                if value != "yz" and value < max_yz:
                    max_yz = value

            return max_yz

yz = Solution()

s = "loveleetcode"


print(yz.firstUniqChar(s))