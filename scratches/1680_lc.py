# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         ans = ""
#
#         for i in range(1,n+1):
#             ans += (bin(i))[2::]
#         ans = int(ans,2)
#         return ans%(10**9+7)

import numpy
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        i = 1
        while i <= n:
            ans = ((ans<<(1+int(numpy.log2(i)))%(10**9+7)) + i)

            i += 1

        return ans%(10**9+7)

yz = Solution()
print(yz.concatenatedBinary(n=63556))