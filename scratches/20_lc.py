# class Solution:
    # def isValid(self, s):
    #     stack1 = []
    #     stack2 = []
    #     stack3 = []
    #
    #     for i in range(len(s)):
    #         if s[i] == "(":
    #             stack1.append(s[i])
    #         elif s[i] == "{":
    #             stack2.append(s[i])
    #         elif s[i] == "[":
    #             stack3.append(s[i])
    #         elif s[i] == ")":
    #             if stack1 ==[]:
    #                 return False
    #             counter = stack1.pop(0)
    #             if counter != "(":
    #                 return False
    #         elif s[i] == "}":
    #             if stack2 ==[]:
    #                 return False
    #             counter = stack2.pop(0)
    #             if counter != "{":
    #                 return False
    #         else:
    #             if stack3 ==[]:
    #                 return False
    #             counter = stack3.pop(0)
    #             if counter != "[":
    #                 return False
    #
    #     return True


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False


        return stack == []


s = "{[]}(}"

yz = Solution()

print(yz.isValid(s))