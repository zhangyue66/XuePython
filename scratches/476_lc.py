class Solution:
    def findComplement(self, num):
        ans = bin(num)[2::]

        yz = ""

        for i in range(len(ans)):
            if ans[i] == "1":
                yz += "0"
            elif ans[i] == "0":
                yz += "1"

        return int("0b"+yz,2)

yz = Solution()

num = 1

print(yz.findComplement(num))

