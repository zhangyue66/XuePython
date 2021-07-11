class Solution:
    def calculate(self, s: str):
        ans = 0
        stack = []

        for st in s:
            if st.isnumeric():
                stack.append(int(st))
            elif st == "+" or st == "-":
                stack.append(st)
            elif st == "*" or st == "/":




yz = Solution()
s = "3+2*2"
print(yz.calculate(s))