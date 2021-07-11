class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        a_max = 0
        b_max = 0

        i = 0
        while x ** i <= bound:
            i+=1
        a_max = i

        j = 0
        while y ** j <= bound:
            j+=1
        b_max = j

        ans = {}

        for i in range(a_max+1):
            for j in range(b_max+1):
                yz = x**i + y**j
                if yz <= bound and yz not in ans:
                    ans[yz] =1

        res = []

        for key,value in ans.items():
            res.append(key)

        return res

yz = Solution()

x = 3
y = 5

bound = 15

print(yz.powerfulIntegers(x,y,bound))