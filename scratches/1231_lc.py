class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) == 2:
            return True
        else:
            if (coordinates[1][0]-coordinates[0][0]) == 0 :
                for i in range(3,len(coordinates)):
                    if coordinates[i][0]-coordinates[0][0] != 0:
                        return False
                return True
            else:
                k = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
                for i in range(3, len(coordinates)):
                    if (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0]) != k :
                        return False

                return True


yz = Solution()

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

print(yz.checkStraightLine(coordinates))