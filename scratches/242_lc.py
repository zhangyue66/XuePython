class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        else:
            freq = {}
            for item in s :
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1

            for word in t :
                if word in freq:
                    freq[word] -= 1
                else:
                    freq[word] = 1

            if list(freq.values()).count(0) != len(list(freq.values())):
                #print(list(freq.values()).count(0))
                return False
            else:
                return True


yz = Solution()

s = " a"
t = "a "

print(yz.isAnagram(s,t))