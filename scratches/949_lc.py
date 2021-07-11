import itertools
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        k = sorted(list(itertools.permutations(A)), reverse=True)

        for i in k:
            a, b, c, d = i
            su = (a * 10 + b)
            sd = (c * 10 + d)

            if su < 24 and sd < 60:
                return f"{a}{b}:{c}{d}"

        return ''






yz = Solution()

A  = [1,2,3,4]

print(yz.largestTimeFromDigits(A))