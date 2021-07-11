class Solution:
    # def numIslands(self, grid) -> int:
    #     if grid is None:
    #         return 0
    #     else:
    #         res = 0
    #         def dfs(i,j,grid):
    #             if i <0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
    #                 return
    #             else:
    #                 grid[i][j] = "#"
    #                 dfs(i+1,j,grid)
    #                 dfs(i-1,j,grid)
    #                 dfs(i,j+1,grid)
    #                 dfs(i,j-1,grid)
    #
    #         for i in range(len(grid)):
    #             for j in range(len(grid[0])):
    #                 if grid[i][j] == "1":
    #                     dfs(i,j,grid)
    #                     res += 1
    #
    #         return res
    def numIslands(self, grid) -> int:
        if len(grid) == 0 :
            return 0
        m = len(grid)
        n = len(grid[0])

        parent = [i for i in range(m*n)]

        def find(a):
            if parent[a] == a:
                return a
            xa = parent[a]
            return find(xa)

        def union(a,b):
            xa = find(a)
            xb = find(b)

            if xa != xb:
                parent[xa] = xb


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if 0<= i-1 < m and grid[i-1][j] == "1":
                        union(i*n+j,(i-1)*n+j)
                    if 0 <= i+1 < m and grid[i+1][j] == "1":
                        union(i*n+j,(i+1)*n+j)

                    if 0 <= j-1 < n and grid[i][j-1] == "1":
                        union(i*n+j,i*n+(j-1))

                    if 0 <= j +1 < n and grid[i][j+1] == "1":
                        union(i*n+j,i*n+(j+1))


                    if 0 <= j-1 < n and grid[i][j-1] == "1":
                        union(i*n+j,i*n+(j-1))

                    if 0 <= j +1 < n and grid[i][j+1] == "1":
                        union(i*n+j,i*n+(j+1))

        return len(parent)


