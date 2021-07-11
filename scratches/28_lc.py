class Solution:
    def strStr(self, haystack, needle):
        if needle is "":
            return 0
        else:
            hay_l = len(haystack)
            need_l = len(needle)


            for i in range(hay_l-need_l+1):
                if haystack[i:(i+need_l)] == needle:
                    return i
            return -1


yz = Solution()

haystack = "hellofuck"
needle = "fuck"

print(yz.strStr(haystack,needle))
