class Solution:
    def camelMatch(self, queries, pattern):
        def uppercase(yzs):
            list1_yz = []
            for yz in yzs:
                if yz.isupper() == True:
                    list1_yz.append(yz)
            return list1_yz

        def match_seq(p,q):
            #a is pattern . b is query in queries
            j = 0
            for i in range(len(q)):
                if j < len(p) and q[i] != p[j]:
                    continue
                elif j< len(p) and q[i] == p[j]:
                    j += 1
                    continue


            if j == len(p):
                return True
            else:
                return False


        res = []

        for query in queries:
            if uppercase(query) == uppercase(pattern) and match_seq(pattern,query) == True:
                res.append(True)
            else:
                res.append(False)

        return res

queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern = "FB"


yz = Solution()

print(yz.camelMatch(queries,pattern))