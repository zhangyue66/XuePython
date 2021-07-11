class Solution:
    def longestValidParentheses(self, s):
        ans = 0
        cnt = 0
        stack = []
        prev = ""
        for pare in s:
            if pare == "(":
                stack.append(pare)
                cnt += 1
            else: # now seeing ")"
                if  len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                    cnt += 1
                    ans = max(cnt,ans)
                elif stack[-1] == ")"




yz = Solution()
s = "(()"
print(yz.longestValidParentheses(s))