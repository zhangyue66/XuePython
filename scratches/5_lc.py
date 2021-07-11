class Solution:
    def longestPalindrome(self, s: str):
        #define a helper() to get the longest palindrom
        #inner to outer
        def helper(strings,l,r):
            while l >= 0 and r < len(strings) and strings[l] == strings[r]:
                l -= 1
                r += 1
            return strings[l+1:r]


        ans = ""
        for i in range(len(s)):
            #ans = max(helper(s,i,i),helper(s,i,i+1),ans,key=len)
            if len(s) % 2 == 1:
                yz = helper(s,i,i)

            elif len(s) %2 == 0 :
                yz = helper(s,i,i+1)


            if len(yz) > len(ans):
                ans = yz

        return ans

yz = Solution()

s = "ac"

print(yz.longestPalindrome(s))