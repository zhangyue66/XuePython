class Solution:
    def distributeCandies(self, candies: int, num_people):
        res = [0]*num_people
        n = 1
        while candies>0:
            for i in range(num_people):
                if candies >=  n:
                    res[i] += n
                    candies -= n
                else:
                    res[i] += candies
                    candies = 0

                n += 1

        return res


yz = Solution()
candies = 10
num_people = 3
print(yz.distributeCandies(candies,num_people))