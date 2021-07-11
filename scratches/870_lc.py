from collections import defaultdict

class Solution:
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)


        dict = defaultdict(list)

        no = []

        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                dict[sortedB[j]].append(a)
                j+=1
            else:
                no.append(a)

        ans = []

        for b in B:
            if b in dict and dict[b] != []:
                ans.append(dict[b].pop())
            else:
                ans.append(no.pop())

        return ans


A = [2,7,11,15]
B = [1,10,4,11]
yz = Solution()
print(yz.advantageCount(A,B))