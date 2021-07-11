# class Solution:
#     def wordBreak(self, s: str, wordDict):
#         stack = [0]
#         seen = set()
#
#         while stack:
#             cur = stack.pop()
#             if cur in seen:
#                 continue
#             seen.add(cur)
#
#             for word in wordDict:
#                 if s[cur:].startswith(word):
#                     x = len(word)
#
#                     if x == len(s[cur:]):
#                         return True
#                     stack.append(cur+x)
#
#         return False

class Solution:

    def wordSearch(self,s,wordDict):

        if s in self.memo:
            return self.memo[s]
        if s in wordDict:
            self.memo[s] = True
            return True

        for j in range(1,len(s)):
            left = s[0:j]
            right = s[j:]

            if right in wordDict  and self.wordSearch(left,wordDict) == True:
                self.memo[s] = True
                return True

        self.memo[s] = False

        return False


    def wordBreak(self, s: str, wordDict):
        self.memo = {}
        ans = self.wordSearch(s,wordDict)
        return ans







yz = Solution()
s = "bb"
wordDict = ["a","b","bbb","bbbb"]
print(yz.wordBreak(s,wordDict))