class Solution:
    def addStrings(self, num1: str, num2: str):
        num1,num2 = list(num1),list(num2)

        add = 0

        res = []

        while len(num1) > 0 or len(num2) > 0:
            if len(num1) >0:
                n1 = ord(num1.pop())-ord("0")
            else:
                n1 = 0
            if len(num2) >0 :
                n2 = ord(num2.pop())-ord("0")
            else:
                n2 = 0

            temp = n1 + n2 + add

            res.append(temp % 10)
            add = temp // 10

        if add == 1:
            res.append(add)

        ans = []

        for i in range(len(res)):
            ans.append(str(res[i]))

        yz = ''.join(ans)

        return yz[::-1]







num1 = "123456"

num2 = "789"


yz = Solution()

print(yz.addStrings(num1,num2))

