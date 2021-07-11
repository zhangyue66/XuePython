class Solution:
    def findCircleNum(self, M):

        N = len(M)

        parent = [i for i in range(N)]

        def find(a):
            if parent[a] == a:
                return a
            return find(parent[a])

        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb :
                parent[pa] = pb


        for i in range(N):
            for j in range(N):
                if i != j and M[i][j] == 1:
                    union(i,j)
        ans = 0

        for i in range(N):
            if parent[i] == i:

                ans += 1

        return ans


yz = Solution()
M = [[1,1,0],
     [1,1,0],
     [0,0,1]]

print(yz.findCircleNum(M))