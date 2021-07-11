class Solution:
    def complexNumberMultiply(self, a: str, b: str) :

        def convert(string):
            first,second = string.split("+")
            second = second[:-1]
            return int(first),int(second)


        ar,ai = convert(a)
        br,bi = convert(b)

        ans_real = ar*br-ai*bi
        ans_imag = ar*bi+br+ai



        #return ans_real,ans_imag  (0, -1)

        return str(ans_real)+"+"+str(ans_imag)+"i"


yz = Solution()
a = "1+-1i"
b = "1+-1i"
print(yz.complexNumberMultiply(a,b))