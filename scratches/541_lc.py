class Solution:
    def reverseStr(self, s: str, k: int):
        s = list(s)
        for i in range(0,len(s),2*k):
            l,r = i,i+k-1
            if r > len(s)-1:
                r = len(s) -1
            else:
                while l < r:
                    s[l],s[r] = s[r],s[l]
                    l += 1
                    r -= 1

        return ''.join(s)





s = "abcdefghijkh"
k = 2
yz = Solution()

print(yz.reverseStr(s,k))