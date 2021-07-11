from collections import defaultdict
class Solution:
    def diagonalSort(self, mat):
        m,n = len(mat),len(mat[0])
        dict = defaultdict(list)

        for i in range(m):
            for j in range(n):
                dict[i-j].append(mat[i][j])

        for k,v in dict.items():
            v.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = dict[i-j].pop()

        return mat




yz = Solution()
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

#mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
print(yz.diagonalSort(mat))
