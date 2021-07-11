class Solution:
    def addBinary(self,a,b):
        bin_a = int(a,2)
        bin_b = int(b,2)
        c = str(bin(bin_a+bin_b))

        return c[2:]





a = "1010"
b = "1011"

yz = Solution()

print(yz.addBinary(a,b))