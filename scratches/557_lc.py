class Solution:
    def reverseWords(self, s: str):
        s = s.split(" ")
        yz = "123 "
        for word in s:
            #print(word[::-1])
            yz.join(word)

        return yz


s = "Let's take LeetCode contest"

yz =Solution()

print(yz.reverseWords(s))