class Solution:
    def leastInterval(self, tasks,n):
        if n == 0 :
            return len(tasks)

        maxi = -float("inf")

        dict = {}

        for task in tasks:
            if task not in dict:
                dict[task] = 1
            else:
                dict[task] += 1

        temp = []
        for k,v in dict.items():
            temp.append(v)
            maxi = max(maxi,v)

        cnt = temp.count(maxi)

        return max(len(tasks),(maxi-1)*(n+1)+cnt)





yz = Solution ()
tasks = ["A","A","A","B","B","B"]
n = 2
print(yz.leastInterval(tasks,n))