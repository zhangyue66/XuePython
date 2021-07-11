class Solution:
    def generate(self,numRows):
        result = []
        for i in range(numRows):
            result.append([])
            for j in range(i+1):
                if j in (0,i):
                    result[i].append(1)
                else:
                    value = result[i-1][j-1]+result[i-1][j]
                    result[i].append(value)



        return result


yz = Solution()
print(yz.generate(2),end="")