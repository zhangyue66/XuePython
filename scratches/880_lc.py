class Solution:
    def decodeAtIndex(self, S: str, K: int):
        size = 0

        for s in S:
            if s.isdigit():
                size *= int(s)

            else:
                size += 1

        for s in reversed(S):
            K %= size
            if K == 0 and s.isalpha():
                return s
            if s.isdigit():
                size = size//int(s)
            else:
                size -= 1






yz = Solution()
S = "leet2code3"
K = 10
print(yz.decodeAtIndex(S,K))