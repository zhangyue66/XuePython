class Solution:
    def minTimeToVisitAllPoints(self, points):
        if len(points) == 1:
            return 0
        else:
            time = 0

            for i in range(len(points)-1):
                delta_x = abs(points[i][0]-points[i+1][0])
                delta_y = abs(points[i][1]-points[i+1][1])
                if delta_x != delta_y:
                    time += min(delta_x,delta_y)+abs(delta_x-delta_y)
                else:
                    time += delta_x


            return time


yz = Solution()

points = [[1,1],[3,4],[-1,0]]

print(yz.minTimeToVisitAllPoints(points))