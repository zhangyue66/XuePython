from math import sqrt
class Solution:
    def numberOfBoomerangs(self, points):

        ans = 0

        for x1,y1 in points:
            dic = {}
            for x2,y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                else:
                    dis =  sqrt(abs(x1-x2)**2 + abs(y1-y2**2))
                    if dis not in dic.keys():
                        dic[dis] = 1
                    else:
                        ans += dic[dis]
                        dic[dis] += 1


        return ans*2




points = [[0,0],[1,0],[2,0]]

yz = Solution()

print(yz.numberOfBoomerangs(points))