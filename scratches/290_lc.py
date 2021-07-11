# dic = {'a':'b','c':'d','e':'f','g':'h'}
#
# yz = dic.values()
#
# if "d" in yz:
#     print("hello!")

class Solution:
    def wordPattern(self, pattern: str, str: str):
        candy = str.split()
        if len(pattern) != len(candy):
            return False
        #print(candy)
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic and candy[i] not in dic.values():
                dic[pattern[i]] = candy[i]
            if pattern[i] not in dic and candy[i]  in dic.values():
                return False
            if pattern[i] in dic and dic[pattern[i]] != candy[i]:
                return False

        return True


pattern = "abba"

str = "dog cat cat d"

yz = Solution()

print(yz.wordPattern(pattern,str))

