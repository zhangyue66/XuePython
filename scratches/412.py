class Solution:
    def fizzBuzz(self, n):
        if n ==0:
            return[]
        elif n ==1:
            return ["1"]
        else:
            ans = []
            for i in range(1,n+1):
                if i % 3 ==0 and i % 5 !=0:
                    ans.append("Fizz")
                elif i % 5 == 0 and i %3 !=0:
                    ans.append("Buzz")
                elif i%5 ==0 and i%3 ==0 :
                    ans.append("FizzBuzz")
                else:
                    ans.append(str(i))

        return ans

yz = Solution()

n = 15

print(yz.fizzBuzz(n))