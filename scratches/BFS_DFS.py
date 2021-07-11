# class Solution(object):
#     def findShortestSubArray(self, nums):
#         left, right, count = {}, {}, {}
#         for i, x in enumerate(nums):
#             if x not in left: left[x] = i
#             right[x] = i
#             count[x] = count.get(x, 0) + 1
#
#         # ans = len(nums)
#         # degree = max(count.values())
#         # for x in count:
#         #     if count[x] == degree:
#         #         ans = min(ans, right[x] - left[x] + 1)
#         #
#         # return ans
#
#         print(left,right,count)
#
#
# nums = [1,2,3,2,5]
#
# yz= Solution()
#
# yz.findShortestSubArray(nums)

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print (s, end = " ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'A')


