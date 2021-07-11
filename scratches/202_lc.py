class Solution:
    def isHappy(self, n: int):
        if n == 1:
            return True

        else:

            dic = {}
            dic[n] = 1


            while n != 1:
                nums = [int(d) for d in str(n)]
                yz = 0
                for num in nums:
                    yz += num**2
                n = yz
                print(n)
                if n not in dic:
                    dic[n] = 1
                else:
                    return False

            return True



n = 89

yz = Solution()

print(yz.isHappy(n))