import math

class Solution:
    def countPrimes(self, n: int):
        cnt = 0
        if n <= 1:
            return 0
        else:

            for i in range(2,n):
                if self.is_Prime(i) == True:
                    cnt += 1

            return cnt


    def is_Prime(self,num):
        if num > 1:
            for i in range(2,int(math.sqrt(num))+1):
                if num % i == 0 :
                    return False
            return True

        else:
            return False



n = 10

yz = Solution()

#print(yz.is_Prime(5))
#print(yz.countPrimes(n))