class Solution:
    def compress(self, chars):
        n = len(chars)
        i,cnt = 0,1

        for j in range(1,n):
            if chars[j] == chars[j-1]:
                cnt += 1
            else:
                i += 1
                for k in str(cnt):
                    chars[i] = k
                    i += 1

                cnt = 1

        return i



yz = Solution()

chars = ["a","a","b","b","c","c","c"]

print(yz.compress(chars))

for yz in range(1,7):
    print(yz)
