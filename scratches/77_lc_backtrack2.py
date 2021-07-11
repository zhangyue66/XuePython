class Solution:
    def combine(self, n: int, k):
        if k > n :
            return []
        else:
            res = []


            def helper(n,k,res,path,index):
                if len(path) == k:
                    res.append(path)
                    return
                else:
                    for i in range(index,n+1):
                        path.append(i)
                        helper(n,k,res,path,i+1)
                        path.pop()


            helper(n,k,res,[],1)

            return res
yz = Solution()
n = 4
k = 2
print(yz.combine(n,k))