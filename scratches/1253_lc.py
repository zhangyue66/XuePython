class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum):
        ans = [[0 for i in range(len(colsum))] for j in range(2)]

        for i in range(len(colsum)):
            if colsum[i] == 2:
                ans[0][i] = 1
                ans[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum == 0:
                continue
            else:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0 :
                    ans[1][i] = 1
                    lower -= 1

        if upper > 0 or lower > 0 :
            return [[]]
        return ans





yz =Solution()
upper = 2
lower =1
colsum = [1,1,1]
print(yz.reconstructMatrix(upper,lower,colsum))