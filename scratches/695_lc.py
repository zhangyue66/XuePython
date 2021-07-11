class Solution:
    def maxAreaOfIsland(self, grid):

        m = len(grid)
        n = len(grid[0])

        self.visited = set()

        def dfs(x,y):

            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] != 1:
                return 0
            if (x,y) in self.visited:
                return 0

            if grid[x][y] == 1:
                self.visited.add((x,y))
                return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
        ans = -float("inf")
        for i in range(m):
            for j in range(n):
                yz = dfs(i,j)
                ans = max(ans,yz)

        return ans

yz = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(yz.maxAreaOfIsland(grid))