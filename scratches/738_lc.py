class Solution:
    def monotoneIncreasingDigits(self, N):
        ans = []
        n = len(str(N))
        for i in range(n):
            for d in range(1,10):
                yz = ans + [d]*(n-i)
                yz_int = self.convert(yz)
                if yz_int > N:
                    ans.append(d-1)
                    break
            else:
                ans.append(9)

        return self.convert(ans)

    def convert(self,integers):
        strings = [str(integer) for integer in integers]
        a_string = "".join(strings)
        an_integer = int(a_string)
        return an_integer



yz = Solution()
N = 10
#N = 1234
#N = 332
print(yz.monotoneIncreasingDigits(N))