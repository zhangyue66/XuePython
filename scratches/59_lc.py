class Solution:
    def generateMatrix(self, n: int):
        ans = [[0 for i in range(n)] for j in range(n)]
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        i,j = 0,0 #row,column
        direction = 0
        for num in range(1,n**2 + 1):
            ans[i][j] = num
            ni = i + dr[direction]
            nj = j + dc[direction]
            if 0 <= ni < n and 0 <= nj < n and ans[ni][nj] == 0:
                i = ni
                j= nj

            else:
                direction = (direction + 1) % 4
                i += dr[direction]
                j += dc[direction]



        return ans


yz = Solution()
n = 3
print(yz.generateMatrix(n))
