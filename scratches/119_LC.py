class Solution:
    def getRow(self, rowIndex):
        result = []
        for i in range(rowIndex+1):
            result.append([])
            for j in range(i+1):
                if j in (0,i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1]+result[i-1][j])
        return result[rowIndex]




yz = Solution()

print(yz.getRow(3))